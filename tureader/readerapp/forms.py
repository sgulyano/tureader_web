from django.forms import ModelForm
from .models import Reader
class ItemForm(ModelForm):
    class Meta:
        model = Reader
        fields = '__all__'
        exclude = ['id']