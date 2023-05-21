from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.text import slugify
from home.models import *


@receiver(pre_save, sender = Blog)
def StorieSignal(sender, instance, **kwargs):
    instance.slug = slugify(instance.title)
    return instance

@receiver(pre_save, sender = Activitie)
def StorieSignal(sender, instance, **kwargs):
    instance.slug = slugify(instance.name)
    return instance

@receiver(pre_save, sender = Categorie)
def StorieSignal(sender, instance, **kwargs):
    instance.slug = slugify(instance.name)
    return instance

@receiver(pre_save, sender = Teacher)
def StorieSignal(sender, instance, **kwargs):
    instance.slug = slugify(f'{instance.first_name} {instance.last_name}')
    return instance

@receiver(pre_save, sender = Course)
def StorieSignal(sender, instance, **kwargs):
    instance.slug = slugify(instance.title)
    return instance

@receiver(pre_save, sender = Event)
def StorieSignal(sender, instance, **kwargs):
    instance.slug = slugify(instance.title)
    return instance

@receiver(pre_save, sender = Notice)
def StorieSignal(sender, instance, **kwargs):
    instance.slug = slugify(instance.title)
    return instance

@receiver(pre_save, sender = Research)
def StorieSignal(sender, instance, **kwargs):
    instance.slug = slugify(instance.title)
    return instance

@receiver(pre_save, sender = Scholarship)
def StorieSignal(sender, instance, **kwargs):
    instance.slug = slugify(instance.title)
    return instance
