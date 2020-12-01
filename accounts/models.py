from django.db import models
from django.contrib.auth import get_user_model


MEMBERSHIP_PLANS = (
        ('Free', 'Free'),
        ('Basic Plan', 'Basic Plan'),
        ('Standard Plan', 'Standard Plan'),
        ('Plus Plan', 'Plus Plan'),
    )

User = get_user_model()


# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership = models.CharField(max_length=100, choices=MEMBERSHIP_PLANS, default='Free')
    payments_method = models.CharField(max_length=100, null=False, blank=False)
    number_transactions = models.IntegerField(null=False, blank=False, default=0)
