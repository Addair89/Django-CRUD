from django.forms import ModelForm
from .models import Owner

class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = ['name', 'last_played', 'reason_thrown_away']