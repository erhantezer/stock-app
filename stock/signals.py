from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Stock, Product

@receiver(pre_save, sender=Stock)
def calculate_total_price(sender, instance, **kwargs):
    if not instance.price_total:
        