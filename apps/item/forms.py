from django import forms

from .models import Item, Comment

class ItemFrom(forms.ModelForm):
    """
    Used at:
        - Submit new article (submit view)
    """
    class Meta:
        model = Item
        fields = ('title', 'url')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
