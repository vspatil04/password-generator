from django.db import models

class GeneratedPassword(models.Model):
    password = models.CharField(max_length=128)
    length = models.IntegerField()
    include_numbers = models.BooleanField()
    include_special_chars = models.BooleanField()
    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.password
   
