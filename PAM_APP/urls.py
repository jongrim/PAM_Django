from django.conf.urls import url

from . import views

app_name = 'PAM_APP'
urlpatterns = [
    # ex: /PAM_APP/
    url(r'^$', views.index, name='index'),
    # ex: /PAM_APP/34/
    url(r'^(?P<account_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /PAM_APP/submit/
    url(r'^submit/$', views.submit, name='submit'),
    #ex: /PAM_APP/34/edit/
    url(r'^(?P<account_id>[0-9]+)/edit/$', views.edit, name='edit'),
    #ex: /PAM_APP/34/delete/
    url(r'^(?P<account_id>[0-9]+)/delete/$', views.delete, name='delete')
    # ex: /PAM_APP/submit/add_account/
    # url(r'^submit/add_account/$', views.add_account, name='add_account'),
]
