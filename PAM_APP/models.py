from django.db import models


class Account(models.Model):
    operating_system = 'OS'
    database = 'DB'
    application = 'AP'
    device_type_choices = (
        (operating_system, 'Operating System'),
        (database, 'Database'),
        (application, 'Application')
    )

    high = 3
    medium = 2
    low = 1
    risk_rank_choices = (
        (high, 'High'),
        (medium, 'Medium'),
        (low, 'Low')
    )

    account_name = models.CharField(max_length=255, blank=True, default='')
    username = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    safe = models.CharField(max_length=28, blank=True)
    folder = models.CharField(max_length=255, blank=True)
    device_type = models.CharField(
        max_length=2,
        choices=device_type_choices,
        default=operating_system
    )
    policy_id = models.CharField(max_length=255, blank=True)
    account_id = models.CharField(max_length=25, blank=True)
    last_update_time = models.DateTimeField(auto_now=True)
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

    # def save(self):
    #     self.account_name = self.account_name + '-' + self.address + '-' + self.device_type

    def get_account_name(self):
        return self.username + '-' + self.address + '-' + self.device_type

    def __str__(self):
        return self.username + '-' + self.address
