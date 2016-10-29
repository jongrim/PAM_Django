from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import View, generic

from .models import Account, AccountUser


class ListAccounts(generic.ListView):
    model = Account
    template_name = 'PAM_APP/index.html'
    paginate_by = 3


class CreateAccount(generic.CreateView):
    model = Account
    template_name = 'PAM_APP/create_account.html'
    fields = ['username', 'address', 'device_type', 'database', 'instance', 'safe',
              'folder', 'policy_id', 'risk_rank', 'operational_impact', 'users']


class AccountDetailView(generic.DetailView):
    model = Account
    template_name = 'PAM_APP/account_detail.html'


class UpdateAccount(generic.UpdateView):
    model = Account
    template_name = 'PAM_APP/update_account.html'
    fields = ['username', 'address', 'device_type', 'database', 'instance', 'safe',
              'folder', 'policy_id', 'risk_rank', 'operational_impact', 'users']


class DeleteAccount(generic.DeleteView):
    model = Account
    success_url = reverse_lazy('PAM_APP:index')


class ListUsers(generic.ListView):
    model = AccountUser
    template_name = 'PAM_APP/list_users.html'
    paginate_by = 3


class CreateUser(generic.CreateView):
    model = AccountUser
    template_name = 'PAM_APP/create_user.html'
    fields = ['first_name', 'last_name', 'username', 'email']


class UserDetailView(generic.DetailView):
    model = AccountUser
    template_name = 'PAM_APP/user_detail.html'


class UpdateUser(generic.UpdateView):
    model = AccountUser
    template_name = 'PAM_APP/update_user.html'
    fields = ['first_name', 'last_name', 'username', 'email']


class DeleteUser(generic.DeleteView):
    model = AccountUser
    success_url = reverse_lazy('index')
