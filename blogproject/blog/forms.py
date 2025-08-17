from django import forms
from .models import Post, Uwaga

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')

class UwagaForm(forms.ModelForm):
    class Meta:
        model = Uwaga
        fields = ('name', 'content', 'severity')
