from django.db import models

# Create your models here.
class Mode(models.Model):
    mode_name = models.CharField(max_length=20, null = True, blank = False)
    bio = models.TextField(max_length=200, null = True, blank = False)

    def __str__(self):
        return f"{self.mode_name}"
    
class Tier(models.Model):
    tier_level = models.CharField(max_length=20, null = True, blank = False)
    bio = models.TextField(max_length=400,null = True, blank = True)

    def __str__(self):
        return f"{self.tier_level}"
    

