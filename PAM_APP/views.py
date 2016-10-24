from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Account
from .forms import AccountForm


def index(request):
    accounts_qs = Account.objects.all()
    context = {
        'accounts_qs': accounts_qs,
    }
    return render(request, 'PAM_APP/index.html', context)


def detail(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    return render(request, 'PAM_APP/detail.html', {'account': account})


def submit(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save()
            return HttpResponseRedirect(reverse('PAM_APP:detail', args=(account.id,)))
    else:
        form = AccountForm()
    return render(request, 'PAM_APP/submit.html', {'form': form})


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
    if request.method == 'POST':
        deletion = account.delete()
        return HttpResponseRedirect('PAM_APP:index')
    else:
        return render(request, 'PAM_APP/delete.html', {'account': account})


# def add_account(request):
#     new_account = Account(
#         username=request.POST['username'],
#         address=request.POST['address'],
#         device_type=request.POST['device_type']
#     )
#     new_account.save()
#     return HttpResponseRedirect(reverse('PAM_APP:detail', args=(new_account.id,)))
