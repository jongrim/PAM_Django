from django.forms import ModelForm
from PAM_APP.models import Account


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'address', 'device_type', 'risk_rank', 'operational_impact']
