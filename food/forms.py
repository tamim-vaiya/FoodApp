from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'item_desc', 'item_price', 'item_image']

        widgets = {
            'item_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter item name',
                'maxlength': '200',
            }),
            'item_desc': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter item description',
                'maxlength': '200',
                'rows': 3,
                'style': 'resize: none;',
            }),
            'item_price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter item price',
                'min': '0',
            }),
            'item_image': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter image URL',
            }),
        }
        labels = {
            'item_name': 'Item Name',
            'item_desc': 'Description',
            'item_price': 'Price',
            'item_image': 'Image URL',
        }