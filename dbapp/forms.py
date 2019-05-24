from django import forms
from dbapp.models import Student

class Studnetform(forms.ModelForm):
    class Meta:
        model=Student
        fields=["Name","age",'image']
