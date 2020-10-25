from django import forms
import re
from .models import Visitor, Item, CarouselImg
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class AdminForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'

class VisitorForm(forms.ModelForm):
    username = forms.CharField(max_length= 20, required=True, widget=forms.TextInput(attrs={'class':'form-control col-11 col-lg-10 i_username', 'id':'i_username'}))
    password = forms.CharField(max_length= 20, required=True, widget=forms.PasswordInput(attrs={'class':'form-control col-11 col-lg-10 i_pass'}))
    user_id = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'class':'form-control col-11 col-lg-10 i_user_id'}))
    
    class Meta:
        model = Visitor
        fields = ('username', 'password', 'user_id')

class ItemForm(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control col-11 col-lg-6'}))

    class Meta:
        model = Item
        fields = ('title', )
        
class ImgForm(forms.ModelForm):
    img = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control col-11 col-lg-6'}))
    
    class Meta:
        model = CarouselImg
        fields = ('img', )