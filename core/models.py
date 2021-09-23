from django.db import models
from django.db.models.fields import CharField

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField('First Name', max_length=40)
    last_name = models.CharField('Last Name', max_length=40)
    number = CharField('Number',max_length=15)
    email = models.EmailField('E-mail', max_length=40)
    subject = models.CharField('Subject', max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.first_name