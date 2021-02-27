from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=50, null=True)
    code = models.CharField(max_length=10, null=True)
    order = models.IntegerField(null=True)
    remarks_1 = models.CharField(max_length=50, null=True)
    remarks_2 = models.CharField(max_length=50, null=True)

    # Slug
    slug = models.SlugField(max_length=50, db_index=True, unique=True, allow_unicode=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #상세페이지 출력
        return reverse('sort_by_client', args=[self.slug])

class Consumed(models.Model):
    part_code = models.CharField(max_length=20, null=True, unique=True)
    part_name = models.CharField(max_length=30, null=True)
    part_img = models.ImageField(upload_to='static/img', default='photos/no_image.png', null=True)
    part_desc = models.CharField(max_length=50, null=True)


    def __str__(self):
        return self.part_code


class Machine(models.Model):
    model_type = models.CharField(max_length=50, null=True)
    part1 = models.ForeignKey(Consumed, to_field='part_code', on_delete=models.SET_NULL, null=True, related_name='part1')
    part1_qty = models.IntegerField(null=True)
    part2 = models.ForeignKey(Consumed, to_field='part_code', on_delete=models.SET_NULL, null=True, related_name='part2')
    part2_qty = models.IntegerField(null=True)
    part3 = models.ForeignKey(Consumed, to_field='part_code', on_delete=models.SET_NULL, null=True, related_name='part3')
    part3_qty = models.IntegerField(null=True)
    part4 = models.ForeignKey(Consumed, to_field='part_code', on_delete=models.SET_NULL, null=True, related_name='part4')
    part4_qty = models.IntegerField(null=True)
    part5 = models.ForeignKey(Consumed, to_field='part_code', on_delete=models.SET_NULL, null=True, related_name='part5')
    part5_qty = models.IntegerField(null=True)
    part6 = models.ForeignKey(Consumed, to_field='part_code', on_delete=models.SET_NULL, null=True, related_name='part6')
    part6_qty = models.IntegerField(null=True)
    part7 = models.ForeignKey(Consumed, to_field='part_code', on_delete=models.SET_NULL, null=True, related_name='part7')
    part7_qty = models.IntegerField(null=True)
    part8 = models.ForeignKey(Consumed, to_field='part_code', on_delete=models.SET_NULL, null=True, related_name='part8')
    part8_qty = models.IntegerField(null=True)
    part9 = models.ForeignKey(Consumed, to_field='part_code', on_delete=models.SET_NULL, null=True, related_name='part9')
    part9_qty = models.IntegerField(null=True)


    def __str__(self):
        return self.model_type





class Bookmark(models.Model):
    # Basic Informations
    # client = models.CharField(max_length=100, null=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, related_name='clients')
    model_type = models.ForeignKey(Machine, on_delete=models.SET_NULL, null=True)
    model_no = models.CharField(max_length=20)

    # Slug
    slug = models.SlugField(max_length=50, db_index=True, unique=True, allow_unicode=True, null=True)


    # Manager & Confirm
    inspector = models.CharField(max_length=50, null=True)
    manager = models.ForeignKey(User, on_delete=models.PROTECT, related_name="manager_bookmark", null=True)
    confirm_bs = models.IntegerField(default=0)
    confirm_news = models.IntegerField(default=0)

    # Datetime
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    # BS results
    col1 = models.IntegerField(default=1)
    col1_txt = models.CharField(max_length=150, default='-', null=True)
    col2 = models.IntegerField(default=1)
    col2_txt = models.CharField(max_length=150, default='-', null=True)
    col3 = models.IntegerField(default=1)
    col3_txt = models.CharField(max_length=150, default='-', null=True)
    col4 = models.IntegerField(default=1)
    col4_txt = models.CharField(max_length=150, default='-', null=True)
    col5 = models.IntegerField(default=1)
    col5_txt = models.CharField(max_length=150, default='-', null=True)
    col6 = models.IntegerField(default=1)
    col6_txt = models.CharField(max_length=150, default='-', null=True)
    col7 = models.IntegerField(default=1)
    col7_txt = models.CharField(max_length=150, default='-', null=True)
    col8 = models.IntegerField(default=1)
    col8_txt = models.CharField(max_length=150, default='-', null=True)
    col9 = models.IntegerField(default=1)
    col9_txt = models.CharField(max_length=150, default='-', null=True)
    col10 = models.IntegerField(default=1)
    col10_txt = models.CharField(max_length=150, default='-', null=True)
    col11 = models.IntegerField(default=1)
    col11_txt = models.CharField(max_length=150, default='-', null=True)
    col12 = models.IntegerField(default=1)
    col12_txt = models.CharField(max_length=150, default='-', null=True)
    col13 = models.IntegerField(default=1)
    col13_txt = models.CharField(max_length=150, default='-', null=True)
    col14 = models.IntegerField(default=1)
    col14_txt = models.CharField(max_length=150, default='-', null=True)
    col15 = models.IntegerField(default=1)
    col15_txt = models.CharField(max_length=150, default='-', null=True)
    col16 = models.IntegerField(default=1)
    col16_txt = models.CharField(max_length=150, default='-', null=True)
    col17 = models.IntegerField(default=1)
    col17_txt = models.CharField(max_length=150, default='-', null=True)
    col18 = models.IntegerField(default=1)
    col18_txt = models.CharField(max_length=150, default='-', null=True)
    col19 = models.IntegerField(default=1)
    col19_txt = models.CharField(max_length=150, default='-', null=True)
    col20 = models.IntegerField(default=1)
    col20_txt = models.CharField(max_length=150, default='-', null=True)
    col21 = models.IntegerField(default=1)
    col21_txt = models.CharField(max_length=150, default='-', null=True)
    col22 = models.IntegerField(default=1)
    col22_txt = models.CharField(max_length=150, default='-', null=True)
    col23 = models.IntegerField(default=1)
    col23_txt = models.CharField(max_length=150, default='-', null=True)
    col24 = models.IntegerField(default=1)
    col24_txt = models.CharField(max_length=150, default='-', null=True)
    col25 = models.IntegerField(default=1)
    col25_txt = models.CharField(max_length=150, default='-', null=True)
    col26 = models.IntegerField(default=1)
    col26_txt = models.CharField(max_length=150, default='-', null=True)
    col27 = models.IntegerField(default=1)
    col27_txt = models.CharField(max_length=150, default='-', null=True)
    col28 = models.IntegerField(default=1)
    col28_txt = models.CharField(max_length=150, default='-', null=True)
    col29 = models.IntegerField(default=1)
    col29_txt = models.CharField(max_length=150, default='-', null=True)
    bs_opinion = models.TextField(default='BS 프로그램에 기준한 점검결과 특이사항이 없습니다.', null=True)
    manager_opinion = models.TextField(default='기타 의견 및 요청항목이 없습니다.', null=True)

    # etc.
    visibility = models.IntegerField(default=1, null=True)
    available_display = models.BooleanField('Display', default=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return "고객명 : " + self.client.name + "시리얼번호 : " + self.model_no + ", 생성일 : " + self.created.strftime("%Y-%m-%d %H:%M:%S")

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
    #    return reverse('detail', args=[self.slug])

