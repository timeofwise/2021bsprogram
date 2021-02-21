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
    q3_1_main_concern = models.CharField(max_length=80, default='-', null=True)
    q3_21_fi_smart_erp = models.CharField(max_length=10, default='-', null=True)
    q3_22_fi_factory_automation = models.CharField(max_length=10, default='-', null=True)
    q3_23_fi_remote_support = models.CharField(max_length=10, default='-', null=True)
    q3_24_fi_systematical_training = models.CharField(max_length=10, default='-', null=True)
    q3_25_fi_other = models.CharField(max_length=10, default='-', null=True)
    q3_25_other = models.CharField(max_length=50, null=True)
    q3_3_recommend_to_other = models.IntegerField(null=True)

    # 4 agreement and others
    manager_opinion = models.TextField(default='기타 의견 및 요청항목이 없습니다.', null=True)
    policy_agreement = models.CharField(max_length=10, null=True)








    # Datetime
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return "설문자명 : " + self.name + ", 고객명 : " + self.company + ", 생성일 : " + self.created.strftime("%Y-%m-%d %H:%M:%S")
