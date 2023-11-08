from django.db import models
from django.contrib.auth.models import User

class DeveloperProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    company_info = models.TextField(blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    website = models.URLField(blank=True, null=True)
    established_date = models.DateField(blank=True, null=True)
    total_projects = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.company_name