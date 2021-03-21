from django import forms
from .models import qr_info

class GetQRForm(forms.ModelForm):
    class Meta:
        model = qr_info
        fields = [
            'model_name',
            'model_no',
            'ver_sw',
            'ver_mmi',
            'ver_rt',
            'ver_opti',
            'ver_it',
            'option_1'
        ]