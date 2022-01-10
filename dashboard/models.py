from django.db import models

# Create your models here.


class CatalogName(models.Model):  # Название справочников
    name = models.CharField(verbose_name='Имя', max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CatalogData(models.Model):  # Данные справочника
    catalog_name_id = models.ForeignKey(CatalogName, on_delete=models.CASCADE)
    value = models.CharField(verbose_name='Значение', max_length=255)
    squence = models.PositiveBigIntegerField(verbose_name='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class RegistrySendingTravelAgency(models.Model):  # Реестр отправляющих компаний
    name_organization = models.CharField(verbose_name='Название организации', max_length=255, blank=False, null=False)
    account_number = models.BigIntegerField(verbose_name='Номер счета', null=False, blank=False, unique=False)
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class RegistryTransportOrganizations(models.Model):  # Реестр транспортных компаний
    name_organization = models.CharField(verbose_name='Название организации', max_length=255, blank=False, null=False)
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)
    catalog_data_id = models.ManyToManyField(CatalogData)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
