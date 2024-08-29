from django.db import models
from django.contrib.auth.hashers import check_password as check_password_hashed

class SIGNUP(models.Model):
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=128)

    