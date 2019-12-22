from django import forms
from .models import Booklist


class AddForm(forms.ModelForm):
    class Meta:
        model = Booklist
        fields = ('position', 'name_ru', 'name_eng', 'autor', 'genre', 'publication_date', 'link')
