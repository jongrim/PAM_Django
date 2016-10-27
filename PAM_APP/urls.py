from django.conf.urls import url
from PAM_APP.views import IndexView, AccountDetailView, AddAccount

from . import views

app_name = 'PAM_APP'
urlpatterns = [
    # ex: /PAM_APP/
    url(r'^$', IndexView.as_view(), name='index'),
    # ex: /PAM_APP/34/
    url(r'^account/(?P<pk>[0-9]+)/detail$', AccountDetailView.as_view(), name='account_detail'),
    # ex: /PAM_APP/add_account/
    url(r'^add_os_account/$', AddAccount.as_view(), name='add_account'),
    # ex: /PAM_APP/34/edit/
    url(r'^(?P<account_id>[0-9]+)/edit/$', views.edit, name='edit'),
    # ex: /PAM_APP/34/delete/
    url(r'^(?P<account_id>[0-9]+)/delete/$', views.delete, name='delete'),
    # ex: /PAM_APP/34/remove_account
    url(r'^(?P<account_id>[0-9]+)/remove_account/$', views.remove_account, name='remove_account'),
]
