from django.db import models
from django.urls import reverse

# Create your models here.
class Survey(models.Model):
    # 1 Personal Informations
    name = models.CharField(max_length=100, null=True)
    company = models.CharField(max_length=100, null=True)
    mobile = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=100, null=True)
    position = models.CharField(max_length=50, null=True)
    position_other = models.CharField(max_length=50, null=True)

    # 2 BS Evaluation
    q2_overall = models.IntegerField(null=True)
    q2_sw = models.IntegerField(null=True)
    q2_head_anc = models.IntegerField(null=True)
    q2_xy = models.IntegerField(null=True)
    q2_conveyor = models.IntegerField(null=True)
    q2_feederbase = models.IntegerField(null=True)
    q2_illumination = models.IntegerField(null=True)
    q2_air = models.IntegerField(null=True)
    q2_trust = models.CharField(max_length=10, null=True)
    q2_trust_other = models.CharField(max_length=50, null=True)
    q2_after_service = models.CharField(max_length=10, null=True)
    q2_after_service_other = models.CharField(max_length=50, null=True)

    # 3 Concerns & Interests
    q3_1_main_concern = models.CharField(max_length=10, default='-', null=True)
    q3_2_1_future_interest_smart_erp = models.CharField(max_length=10, default='-', null=True)
    q3_2_2_future_interest_factory_automation = models.CharField(max_length=10, default='-', null=True)
    q3_2_3_future_interest_remote_support = models.CharField(max_length=10, default='-', null=True)
    q3_2_4_future_interest_systematical_training = models.CharField(max_length=10, default='-', null=True)
    q3_2_5_future_interest_other = models.CharField(max_length=10, default='-', null=True)
    q3_2_5_other = models.CharField(max_length=50, null=True)








    # Datetime
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return "설문자명 : " + self.name + ", 고객명 : " + self.company + ", 생성일 : " + self.created.strftime("%Y-%m-%d %H:%M:%S")
