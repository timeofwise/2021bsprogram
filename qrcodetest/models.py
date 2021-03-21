from django.db import models

# Create your models here.

class qr_info(models.Model):
    model_name = models.CharField(max_length=10, null=True)
    model_no = models.CharField(max_length=10, null=True, unique=True)
    ver_sw = models.CharField(max_length=30, null=True)
    ver_mmi = models.CharField(max_length=20, null=True)
    ver_rt = models.CharField(max_length=20, null=True)
    ver_opti = models.CharField(max_length=20, null=True)
    ver_it = models.CharField(max_length=20, null=True)
    option_1 = models.BooleanField(default=False, null=True)
    option_2 = models.BooleanField(default=False, null=True)
    option_3 = models.BooleanField(default=False, null=True)
    option_4 = models.BooleanField(default=False, null=True)
    option_5 = models.BooleanField(default=False, null=True)

    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.model_no