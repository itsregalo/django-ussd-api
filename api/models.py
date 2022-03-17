from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=254)
    adm_no = models.CharField(max_length=15)

    def __str__(self):
        return self.name