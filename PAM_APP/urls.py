from django.conf.urls import url
from PAM_APP.views import ListAccounts, ListUsers, AccountDetailView, UserDetailView, CreateAccount, CreateUser,\
    UpdateAccount, UpdateUser, DeleteAccount, DeleteUser

app_name = 'PAM_APP'
# URL name patterns should follow the pattern 'verb_object'
urlpatterns = [
    # ex: /PAM_APP/
    url(r'^$', ListAccounts.as_view(), name='index'),
    # ex: /PAM_APP/?page=34
    # url(r'^page(?P<page>[0-9]+)/$', ListAccounts.as_view(), name='index'),
    # ex: /PAM_APP/users
    url(r'^users/$', ListUsers.as_view(), name='list_users'),
    # ex: /PAM_APP/account/34/detail
    url(r'^account/(?P<pk>[0-9]+)/detail/$', AccountDetailView.as_view(), name='view_account'),
    # ex: /PAM_APP/user/34/detail
    url(r'^user/(?P<pk>[0-9]+)/detail/$', UserDetailView.as_view(), name='view_user'),
    # ex: /PAM_APP/add_account/
    url(r'^create_account/$', CreateAccount.as_view(), name='create_account'),
    # ex: /PAM_APP/add_user/
    url(r'^create_user/$', CreateUser.as_view(), name='create_user'),
    # ex: /PAM_APP/account/34/edit/
    url(r'^account/(?P<pk>[0-9]+)/edit/$', UpdateAccount.as_view(), name='update_account'),
    # ex: /PAM_APP/user/34/edit/
    url(r'^user/(?P<pk>[0-9]+)/edit/$', UpdateUser.as_view(), name='update_user'),
    # ex: /PAM_APP/account/34/delete/
    url(r'^account/(?P<pk>[0-9]+)/delete/$', DeleteAccount.as_view(), name='delete_account'),
    # ex: /PAM_APP/user/34/delete/
    url(r'^user/(?P<pk>[0-9]+)/delete/$', DeleteUser.as_view(), name='delete_user'),
]
