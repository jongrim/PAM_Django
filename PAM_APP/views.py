from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View, generic

from .models import Account, AccountUser
from .forms import AccountForm


class IndexView(generic.ListView):
    model = Account
    template_name = 'PAM_APP/index.html'
#     TODO figure out how to return the first x number of accounts, and do pagination


class AccountDetailView(generic.DetailView):
    model = Account
    template_name = 'PAM_APP/detail.html'

# def index(request):
#     accounts_qs = Account.objects.all()
#     context = {
#         'accounts_qs': accounts_qs,
#     }
#     return render(request, 'PAM_APP/index.html', context)


def detail(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    return render(request, 'PAM_APP/detail.html', {'account': account})


# def submit(request):
#     if request.method == 'POST':
#         form = AccountForm(request.POST)
#         if form.is_valid():
#             account = form.save()
#             return HttpResponseRedirect(reverse('PAM_APP:detail', args=(account.id,)))
#     else:
#         form = AccountForm()
#     return render(request, 'PAM_APP/submit.html', {'form': form})


class AddAccount(View):
    account_form = AccountForm

    def get(self, request):
        account_form = AccountForm()
        return render(request, 'PAM_APP/submit.html', {'account_form': account_form})

    def post(self, request):
        post_data = request.POST
        account_form = AccountForm(request.POST)
        if account_form.is_valid():
            account = account_form.save()
            user = get_object_or_404(AccountUser, pk=request.POST['users'])
            return HttpResponseRedirect(reverse('PAM_APP:detail', args=(account.id, )))


def edit(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    if request.method == 'POST':
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            account = form.save()
            return HttpResponseRedirect(reverse('PAM_APP:detail', args=(account.id,)))
    else:
        form = AccountForm(instance=account)
        return render(request, 'PAM_APP/edit.html', {'form': form})


def delete(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    return render(request, 'PAM_APP/delete.html', {'account': account})


def remove_account(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    account.delete()
    return HttpResponseRedirect(reverse('PAM_APP:index'))
