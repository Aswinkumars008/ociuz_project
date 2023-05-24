from django import forms
from .models import Data
    
class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = '__all__'
        labels = {
           
        'name':'Employee Name', 
        'email' :'Email',
        'phone' :'Phone',
        'designation' :'Designation', 
        'address' : 'Address', 
        
        }
        