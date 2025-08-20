from django import forms
from .models import Post, Uwaga

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'tag', 'image')

    def clean_image(self):
        img = self.cleaned_data.get("image")
        if img and img.size > 2* 1024 * 1024:
            raise forms.ValidationError("Plik jest za duży (powyżej 2mb)")
        return img

class UwagaForm(forms.ModelForm):
    class Meta:
        model = Uwaga
        fields = ('name', 'content', 'severity')
