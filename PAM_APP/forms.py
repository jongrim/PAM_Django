from django.forms import ModelForm
from PAM_APP.models import Account


class AccountForm(ModelForm):
    class Meta:
        model = Account
        exclude = ['account_name', 'cyberark_account_id']
