from django.db import models
from django.contrib.auth.models import User
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import task_email

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,blank=False, null=False,on_delete=models.CASCADE)
    about = models.TextField(blank=True, null=True)
    mobile_no = models.BigIntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    profile_image = models.ImageField(blank=True, null=True,upload_to = 'images/')

@receiver(post_save, sender=Profile)
def send_welcome_email_signal(sender, instance, created, **kwargs):
        if created:
            task_email.delay(instance.email)
            
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
        


class Talks(models.Model):
    user = models.ForeignKey(User,related_query_name="talks",on_delete=models.CASCADE,)
    body = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User,related_name="likes", blank=True)

    def number_likes(self):
        return self.likes.count()

    
    def __str__(self):
        return( f"({self.created_at:%Y-%m-%d %H:%M:%S}):")
