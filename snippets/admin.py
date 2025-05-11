from django.contrib import admin
from .models import CodeSnippet, Language, Comment

admin.site.register(CodeSnippet)
admin.site.register(Language)
admin.site.register(Comment)