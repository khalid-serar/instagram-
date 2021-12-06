from django import forms
from .models import Profile, Image
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Comment,Image

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=300, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'picture', 'bio']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=300, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')

class  NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'likes','comments']

class CommentsForm(forms.ModelForm):
  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)
    self.fields['comment'].widget=forms.TextInput()
    self.fields['comment'].widget.attrs['placeholder']='Leave a comment...'
  class Meta:
    model = Comment
    fields = ('comment',)