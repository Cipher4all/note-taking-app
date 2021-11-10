from django import forms
from .models import MyNote

class CreateNote(forms.ModelForm):
    picture = forms.ImageField(required=False)
    class Meta:
        model = MyNote
        fields = '__all__'

    