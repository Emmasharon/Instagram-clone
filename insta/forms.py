from .models import Profile,Post, Comment
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['pic','caption']
        exclude = ['profile','like']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post','username','date','count']