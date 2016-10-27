from django.db import models
from django.urls import reverse


class AccountUser(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=35)
    username = models.CharField(max_length=35, unique=True)
    email = models.EmailField(max_length=75, default='user@gmail.com')

    def get_absolute_url(self):
        return reverse('PAM_APP:view_user', kwargs={'pk': self.pk})

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Account(models.Model):
    high = 3
    medium = 2
    low = 1
    risk_rank_choices = (
        (high, 'High'),
        (medium, 'Medium'),
        (low, 'Low')
    )

    operating_system = 'OS'
    database = 'DB'
    application = 'AP'
    network = 'NT'
    device_type_choices = (
        (operating_system, 'Operating System'),
        (database, 'Database'),
        (application, 'Application'),
        (network, 'Network')
    )

    account_name = models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    device_type = models.CharField(
        max_length=2,
        choices=device_type_choices,
        default='OS'
    )
    database = models.CharField(max_length=30, blank=True)
    instance = models.CharField(max_length=30, blank=True)
    safe = models.CharField(max_length=28, blank=True)
    folder = models.CharField(max_length=255, blank=True)
    policy_id = models.CharField(max_length=255, blank=True)
    cyberark_account_id = models.CharField(max_length=25, blank=True)
    last_update_time = models.DateTimeField(auto_now=True, editable=False)
    risk_rank = models.PositiveSmallIntegerField(
        blank=True,
        choices=risk_rank_choices,
        default=1
    )
    operational_impact = models.PositiveSmallIntegerField(
        blank=True,
        choices=risk_rank_choices,
        default=1
    )
    overall_score = models.PositiveSmallIntegerField(blank=True, default=1)
    users = models.ManyToManyField(AccountUser, blank=True)

    def get_account_name(self):
        return self.username + '-' + self.address + '-' + self.device_type

    def get_absolute_url(self):
        return reverse('PAM_APP:view_account', kwargs={'pk': self.pk})

    def __str__(self):
        return self.username + '-' + self.address
