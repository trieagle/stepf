from django.contrib.auth import models as auth_models 
from django.db import models

"""attribute in User
username(*), first_name, last_name, email, password, is_staff, is_active,
is_superuser, last_login, date_joined
"""

class Account(models.Model):
    user = models.ForeignKey(auth_models.User, unique=True)
    portrait = models.ImageField('your portrait', upload_to="img/portrait")
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, 
                              choices=GENDER_CHOICES, 
                              blank=True)

    def __unicode__(self):
        return self.user.username

    class Meta:
        ordering = ['user']

# Create your models here.
