from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control ml-1 shadow-none textarea'}))

    class Meta:
        model = Comment
        fields = ('content',)
