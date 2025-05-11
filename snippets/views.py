from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.core.paginator import Paginator
from .models import CodeSnippet, Language
from .forms import CodeSnippetForm, CommentForm, SnippetSearchForm


def snippet_list(request):
    snippets = CodeSnippet.objects.filter(is_public=True).order_by('-created_at')
    languages = Language.objects.all()
    
    paginator = Paginator(snippets, 12)  # Show 12 snippets per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    search_form = SnippetSearchForm()
    
    return render(request, 'snippets/snippet_list.html', {
        'page_obj': page_obj,
        'languages': languages,
        'search_form': search_form,
    })


def snippet_search(request):
    search_form = SnippetSearchForm(request.GET)
    snippets = CodeSnippet.objects.filter(is_public=True)
    
    if search_form.is_valid():
        query = search_form.cleaned_data.get('query')
        language = search_form.cleaned_data.get('language')
        
        if query:
            snippets = snippets.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(code__icontains=query)
            )
        
        if language:
            snippets = snippets.filter(language=language)
    
    paginator = Paginator(snippets, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'snippets/snippet_search.html', {
        'page_obj': page_obj,
        'search_form': search_form,
        'query': request.GET.get('query', ''),
    })


def snippet_detail(request, slug):
    snippet = get_object_or_404(CodeSnippet, slug=slug)
    
    # Increment the view counter
    snippet.views += 1
    snippet.save()
    
    # If snippet is private and user is not the author, forbid access
    if not snippet.is_public and (not request.user.is_authenticated or request.user != snippet.author):
        return HttpResponseForbidden("You don't have permission to view this snippet")
    
    comments = snippet.comments.all()
    comment_form = CommentForm()
    
    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.snippet = snippet
            new_comment.author = request.user
            new_comment.save()
            messages.success(request, 'Your comment has been added!')
            return redirect('snippet-detail', slug=slug)
    
    return render(request, 'snippets/snippet_detail.html', {
        'snippet': snippet,
        'comments': comments,
        'comment_form': comment_form,
    })


@login_required
def snippet_create(request):
    if request.method == 'POST':
        form = CodeSnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.author = request.user
            snippet.save()
            messages.success(request, 'Your code snippet has been created!')
            return redirect('snippet-detail', slug=snippet.slug)
    else:
        form = CodeSnippetForm()
    
    return render(request, 'snippets/snippet_form.html', {
        'form': form,
        'title': 'Create New Snippet',
    })


@login_required
def snippet_update(request, slug):
    snippet = get_object_or_404(CodeSnippet, slug=slug)
    
    # Check if the user is the author of the snippet
    if request.user != snippet.author:
        return HttpResponseForbidden("You don't have permission to edit this snippet")
    
    if request.method == 'POST':
        form = CodeSnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your code snippet has been updated!')
            return redirect('snippet-detail', slug=snippet.slug)
    else:
        form = CodeSnippetForm(instance=snippet)
    
    return render(request, 'snippets/snippet_form.html', {
        'form': form,
        'title': 'Edit Snippet',
    })


@login_required
def snippet_delete(request, slug):
    snippet = get_object_or_404(CodeSnippet, slug=slug)
    
    # Check if the user is the author of the snippet
    if request.user != snippet.author:
        return HttpResponseForbidden("You don't have permission to delete this snippet")
    
    if request.method == 'POST':
        snippet.delete()
        messages.success(request, 'Your code snippet has been deleted!')
        return redirect('snippet-list')
    
    return render(request, 'snippets/snippet_confirm_delete.html', {'snippet': snippet})


def language_snippets(request, slug):
    language = get_object_or_404(Language, slug=slug)
    snippets = CodeSnippet.objects.filter(language=language, is_public=True).order_by('-created_at')
    
    paginator = Paginator(snippets, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'snippets/language_snippets.html', {
        'language': language,
        'page_obj': page_obj,
    })