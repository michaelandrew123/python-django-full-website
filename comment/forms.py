from django import forms
from comment.models import Comment, Like
 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', 'blog_post']

class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = ['like_status', 'blog_post']