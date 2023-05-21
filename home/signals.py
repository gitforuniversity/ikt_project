from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.text import slugify
from home.models import *


@receiver(pre_save, sender = Blog)
def StorieSignal(sender, instance, **kwargs):
    instance.slug = slugify(instance.title)
    return instance