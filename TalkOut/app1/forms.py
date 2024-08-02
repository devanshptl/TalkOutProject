from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Talkform(forms.ModelForm):
    body = forms.CharField(required=True,
    widget=forms.widgets.Textarea(
        attrs={
            "placeholder": "Write talks here..",
            "class":"form-control"
        }
    ),
    label="",
    )

    class Meta:
        model = Talks
        exclude = ('user','likes','dislikes', )



class createprofileform(forms.ModelForm):
    profile_image = forms.ImageField(label='Profile Pic',required=False)
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Enter your email',"class":"form-control"}))
    mobile_no = forms.CharField(label='Mobile Number', max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Enter your mobile number',"class":"form-control"}))
    about = forms.CharField(label='About',max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter description',"class":"form-control"}))
    class Meta:
        model = Profile
        exclude = ('user',)

    

class SignUpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
	    super(SignUpForm, self).__init__(*args, **kwargs)

	    