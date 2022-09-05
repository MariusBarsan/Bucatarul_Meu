from django.contrib.auth.models import User
from django.db import models


class UserExtend(User):
    gender_options = (('male', 'Male') , ('female','Female'))
    email_confirmation = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=14)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
