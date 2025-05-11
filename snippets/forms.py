from django import forms
from .models import CodeSnippet, Comment, Language

class CodeSnippetForm(forms.ModelForm):
    class Meta:
        model = CodeSnippet
        fields = ['title', 'description', 'code', 'language', 'is_public']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'code': forms.Textarea(attrs={'class': 'code-editor', 'rows': 15}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'body': 'Comment',
        }


class SnippetSearchForm(forms.Form):
    query = forms.CharField(required=False, label='Search', 
                           widget=forms.TextInput(attrs={'placeholder': 'Search snippets...'}))
    language = forms.ModelChoiceField(
        queryset=Language.objects.all(),
        required=False,
        empty_label="All Languages"
    )