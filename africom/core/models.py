from django.db import models
from africom.services.models import Pricing


# Create your models here.
class RequestQuoteContact(models.Model):
    service = models.CharField(max_length=200, blank=True, null=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    occupation = models.CharField(
        max_length=100, help_text="What you do, i.e., student, software developer, etc."
    )
    package = models.CharField(max_length=1)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name}"
