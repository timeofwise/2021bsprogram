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
    ver_basic_it = models.CharField(max_length=20, null=True)
    ver_t_it_full = models.CharField(max_length=20, null=True)
    ver_t_it_basic = models.CharField(max_length=20, null=True)
    option_1 = models.BooleanField(default=False, null=True)
    option_2 = models.BooleanField(default=False, null=True)
    option_3 = models.BooleanField(default=False, null=True)
    option_4 = models.BooleanField(default=False, null=True)
    option_5 = models.BooleanField(default=False, null=True)
    option_6 = models.BooleanField(default=False, null=True)
    option_7 = models.BooleanField(default=False, null=True)
    option_8 = models.BooleanField(default=False, null=True)
    option_9 = models.BooleanField(default=False, null=True)
    option_10 = models.BooleanField(default=False, null=True)
    option_11 = models.BooleanField(default=False, null=True)
    option_12 = models.BooleanField(default=False, null=True)
    option_13 = models.BooleanField(default=False, null=True)
    option_14 = models.BooleanField(default=False, null=True)
    option_15 = models.BooleanField(default=False, null=True)
    fixed_cam = models.CharField(max_length=50, null=True)
    flying_cam = models.CharField(max_length=50, null=True)
    fid_cam = models.CharField(max_length=50, null=True)
    conv_direction = models.CharField(max_length=5, null=True)
    conv_max_width_single = models.IntegerField(default=0, null=True)
    conv_max_length_single = models.IntegerField(default=0, null=True)
    conv_max_width_dual = models.IntegerField(default=0, null=True)
    conv_max_length_dual = models.IntegerField(default=0, null=True)
    cpu = models.CharField(max_length=50, null=True)
    feederbase_tape = models.CharField(max_length=50, null=True)
    feederbase_tray = models.CharField(max_length=50, null=True)
    latest_cali_date = models.DateTimeField(null=True)

    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.model_no