# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import datetime


class FileDbf(models.Model):
    file = models.FileField(upload_to='files/dbf/', verbose_name='Путь к файлу')
    date = models.DateTimeField(default=datetime.now(), verbose_name='Дата загрузки')

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

    def __str__(self):
        dt = self.date
        return 'Файл: '+ str(self.file) + '. Дата загрузки: ' + dt.strftime("%d.%m.%Y")


class Oper(models.Model):
    hkod = models.CharField(max_length=50, blank=True, null=True, primary_key=True)
    name_o = models.CharField(max_length=254, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    notksg = models.FloatField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'oper'
        verbose_name = 'Операция'
        verbose_name_plural = 'Операции'

    def __str__(self):
        return 'Код: '+ str(self.hkod)  +  str(self.name_o)
