from django.contrib.auth import get_user_model
from django.db import models
from carts.models import Cart


# Create your models here.
User = get_user_model()

STATUS_CHOICES = (
    ("started", "started"),
    ("abandoned", "abandoned"),
    ("completed", "completed"),
)


class Order(models.Model):
    # Assign a user to the order
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=120, default="default", unique=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=120, choices=STATUS_CHOICES, default="started")
    # Assign address to the order
    # Add subtotal
    sub_total = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    # Tax
    tax_total = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    # Final Price
    final_total = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.order_id

