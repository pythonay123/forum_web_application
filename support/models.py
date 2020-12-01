from django.db import models
from django.contrib.auth import get_user_model


MAIN_CATEGORIES = (
        ('Account Support', 'Account Support'),
        ('Vendor Support', 'Vendor Support'),
        ('General Support', 'General Support'),
        ('Market Place Support', 'Market Place Support'),
)

ACCOUNT_SUB_CATEGORIES = (
        ('New Account', 'New Account'),
        ('Password Reset', 'Password Reset'),
        ('Close Account', 'Close Account'),
        ('Vendor Account', 'Vendor Account'),
        ('Profile Issues', 'Profile Issues')
    )

VENDOR_SUB_CATEGORIES = (
    ('Vendor Account', 'Vendor Account'),
    ('Products', 'Products'),
    ('Payment Processing', 'Payment Processing'),
    ('Report a Buyer', 'Report a Buyer'),
)

GENERAL_SUB_CATEGORIES = (
    ('Sign in Problems', 'Sign in Problems'),
    ('Escrow Service', 'Escrow Service'),
    ('Report a User', 'Report a User'),
    ('Security Issues', 'Security Issues'),
    ('Registration Issues', 'Registration Issues'),
    ('Forum Issues', 'Forum Issues'),
    ('Miscellaneous', 'miscellaneous'),
)

MARKET_SUB_CATEGORIES = (
    ('Customer Support', 'Customer Support'),
    ('Report a Seller', 'Report a Seller'),
    ('Request a Refund', 'Request a Refund'),
    ('Cryptocurrency Issues', 'cryptocurrency Issues'),
    ('Miscellaneous', 'miscellaneous'),
)

User = get_user_model()


# Create your models here.
class MainSupport(models.Model):
    category_name = models.CharField(max_length=100, choices=MAIN_CATEGORIES, unique=True)

    def __str__(self):
        return self.category_name


class AccountSupportMessage(models.Model):
    main_category = models.ForeignKey(MainSupport, on_delete=models.CASCADE, default=1)
    sub_category = models.CharField(max_length=100, choices=ACCOUNT_SUB_CATEGORIES)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return '{}-{}'.format(self.main_category, self.sub_category)


class VendorSupportMessage(models.Model):
    main_category = models.ForeignKey(MainSupport, on_delete=models.CASCADE, default=2)
    sub_category = models.CharField(max_length=100, choices=VENDOR_SUB_CATEGORIES)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return '{}-{}'.format(self.main_category, self.sub_category)


class GeneralSupportMessage(models.Model):
    main_category = models.ForeignKey(MainSupport, on_delete=models.CASCADE, default=3)
    sub_category = models.CharField(max_length=100, choices=GENERAL_SUB_CATEGORIES)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return '{}-{}'.format(self.main_category, self.sub_category)


class MarketSupportMessage(models.Model):
    main_category = models.ForeignKey(MainSupport, on_delete=models.CASCADE, default=4)
    sub_category = models.CharField(max_length=100, choices=MARKET_SUB_CATEGORIES)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return '{}-{}'.format(self.main_category, self.sub_category)
