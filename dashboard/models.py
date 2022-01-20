from django.db import models


# Create your models here.


class CatalogName(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Название справочника'
        verbose_name_plural = 'Название справочников'

    def __str__(self):
        return self.name


class CatalogData(models.Model):
    catalog_name_id = models.ForeignKey(CatalogName, verbose_name='Название каталога', on_delete=models.SET_NULL, null=True)
    value = models.CharField(verbose_name='Значение', max_length=255)
    sequence = models.PositiveBigIntegerField(verbose_name='', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Данные справочника'
        verbose_name_plural = 'Данные справочников'

    def __str__(self):
        return f'{self.value} ({self.catalog_name_id.name})'


class Contact(models.Model):
    fio = models.CharField(verbose_name='Фио', max_length=100)
    post = models.CharField(verbose_name='Должность', max_length=100, null=True, blank=True)
    organization = models.CharField(verbose_name='Наименование организации', max_length=100, null=True, blank=True)
    department = models.CharField(verbose_name='Отдел', max_length=100, null=True, blank=True)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=12, null=True, blank=True)
    id_telegramm = models.PositiveIntegerField(verbose_name='id телеграмма', null=True, blank=True)
    email = models.EmailField(verbose_name='Email', null=True, blank=True)
    actual_address = models.CharField(verbose_name='Адрес фактический', max_length=255, null=True, blank=True)
    official_address = models.CharField(verbose_name='Адрес юридический', max_length=255, null=True, blank=True)
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return f'{self.fio} ({self.organization})'


class RegistrySendingTravelAgency(models.Model):
    contact_id = models.ManyToManyField(Contact, verbose_name='Контакты')
    name_organization = models.CharField(verbose_name='Название организации', max_length=255)
    account_number = models.BigIntegerField(verbose_name='Номер счета', null=True, blank=True, unique=True)
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Реестр отправляющих компаний'
        verbose_name_plural = 'Реестр отправляющих компаний'

    def __str__(self):
        return self.name_organization


class RegistryTransportOrganizations(models.Model):
    contact_id = models.ManyToManyField(Contact, verbose_name='Контакты')
    name_organization = models.CharField(verbose_name='Название организации', max_length=255)
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)
    catalog_data_id = models.ManyToManyField(CatalogData, verbose_name='Тип транспортного средства')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Реестр транспортных компаний'
        verbose_name_plural = 'Реестр транспортных компаний'

    def __str__(self):
        return self.name_organization


class RegistryFoodOrganizations(models.Model):
    contact_id = models.ManyToManyField(Contact, verbose_name='Контакты')
    catalog_data_id = models.ManyToManyField(CatalogData, verbose_name='Тип кухни')
    name_organization = models.CharField(verbose_name='Название организации', max_length=255)
    legal_name_organization = models.CharField(verbose_name='Юр. название организации', max_length=255, null=True, blank=True)
    operation_mode = models.CharField(verbose_name='Режим работы', max_length=255, null=True, blank=True)
    capacity = models.SmallIntegerField(verbose_name='Вместимость', null=True, blank=True)
    capacity_comment = models.TextField(verbose_name='Комментарий к вместимости', blank=True, null=True)
    positive_rating = models.SmallIntegerField(verbose_name='Положительный рейтинг', null=True, blank=True)
    negative_rating = models.SmallIntegerField(verbose_name='Отрицательный рейтинг', null=True, blank=True)
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Реестр организаций по питанию'
        verbose_name_plural = 'Реестр организаций по питанию'

    def __str__(self):
        return self.name_organization


class RegistryHotels(models.Model):
    contact_id = models.ManyToManyField(Contact, verbose_name='Контакты')
    name_organization = models.CharField(verbose_name='Название организации', max_length=255)
    number_stars_id = models.ForeignKey(CatalogData, verbose_name='Количество звезд', on_delete=models.SET_NULL, null=True, blank=True)  # Количество звезд
    location = models.CharField(verbose_name='Локация', max_length=255, null=True, blank=True)
    number_room = models.PositiveSmallIntegerField(verbose_name='Количество номером', null=True, blank=True)
    official_website = models.URLField(verbose_name='Оффициальный website', null=True, blank=True)
    parking = models.CharField(verbose_name='Наличие и стоимость парковки', max_length=255, null=True, blank=True)
    extra_space = models.CharField(verbose_name='Возможность доп места', max_length=255, null=True, blank=True)
    early_check_in = models.DecimalField(verbose_name='Стоимость раннего заезда', max_digits=9, decimal_places=2, null=True, blank=True)
    late_check_out = models.DecimalField(verbose_name='Стоимость позднего заезда', max_digits=9, decimal_places=2, null=True, blank=True)
    conference_room = models.TextField(verbose_name='Характеристики конференц зала + стоимость', blank=True, null=True)
    children = models.PositiveSmallIntegerField(verbose_name='До скольких лет дети бесплатно', null=True, blank=True)
    disabled_people = models.PositiveSmallIntegerField(verbose_name='Количество номеров для инвалидов', null=True, blank=True)
    disabled_people_comment = models.TextField(verbose_name='Комментарий к номера для инвалидов', blank=True, null=True)
    animals = models.CharField(verbose_name='Размещение с животными', max_length=255, null=True, blank=True)
    restaurant = models.CharField(verbose_name='Тип ресторана', max_length=255, null=True, blank=True)
    breakfast_time = models.TimeField(verbose_name='Время завтраков', null=True, blank=True)
    luggage_storage = models.CharField(verbose_name='Камера хранения', max_length=255, null=True, blank=True)
    registration_fee = models.CharField(verbose_name='Рег. сбор', max_length=255, null=True, blank=True)
    connect = models.CharField(verbose_name='Коннекты', max_length=255, null=True, blank=True)
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Реестр отелей'
        verbose_name_plural = 'Реестр отелей'

    def __str__(self):
        return self.name_organization


class RegistryMuseum(models.Model):
    contact_id = models.ManyToManyField(Contact, verbose_name='Контакты')
    catalog_data_id = models.ManyToManyField(CatalogData, verbose_name='Тип билета')
    name_organization = models.CharField(verbose_name='Название организации', max_length=255)
    online_ticket = models.CharField(verbose_name='Онлайн билет', max_length=255, null=True, blank=True)
    order_adult = models.CharField(verbose_name='Взрослый наряд', max_length=255, null=True, blank=True)
    order_school = models.CharField(verbose_name='Школьный наряд', max_length=255, null=True, blank=True)
    number_group = models.PositiveSmallIntegerField(verbose_name='Количество человек в группе', null=True, blank=True)
    working_hours = models.CharField(verbose_name='Время работы', max_length=255, null=True, blank=True)
    weekend = models.CharField(verbose_name='Выходные', max_length=255, null=True, blank=True)
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Реестр музеев'
        verbose_name_plural = 'Реестр музеев'

    def __str__(self):
        return self.name_organization


class EmployeeData(models.Model):
    contact_id = models.ManyToManyField(Contact, verbose_name='Контакты')
    fio = models.CharField(verbose_name='Фио сотрудника', max_length=100)
    post_employee_id = models.ForeignKey(CatalogData, verbose_name='Должность сотрудника', on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Список сотрудников'
        verbose_name_plural = 'Список сотрудников'

    def __str__(self):
        return f'{self.fio} ({self.post_employee_id.value})'


class Group(models.Model):
    color = [
        ('red', 'Красный'),
        ('blue', 'Синий'),
        ('orange', 'Оранжевый'),
        ('black', 'Черный'),
        ('green', 'Зеленый'),
    ]
    name_group = models.CharField(verbose_name='Название группы', max_length=255)
    color_group = models.CharField(verbose_name='Цвет выделения', max_length=6, choices=color, default='green')
    number_people = models.PositiveSmallIntegerField(verbose_name='Количество человек')
    school_group = models.CharField(verbose_name='Школьная группа', max_length=255, null=True, blank=True)
    paid_status = models.CharField(verbose_name='Статус оплаты', max_length=50)
    registry_sending_travel_agency_id = models.ForeignKey(RegistrySendingTravelAgency, verbose_name='Агенство по отправке', on_delete=models.SET_NULL, null=True)
    arrival_date = models.DateTimeField(verbose_name='Дата прибытия')
    departure_date = models.DateTimeField(verbose_name='Дата отъезда')
    manager_id = models.ForeignKey(EmployeeData, verbose_name='Менеджер', on_delete=models.SET_NULL, null=True)
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return f'{self.name_group} ({self.arrival_date})'


class GroupMuseum(models.Model):
    group_id = models.ForeignKey(Group, verbose_name='Группа', on_delete=models.SET_NULL, null=True)
    guide_id = models.ForeignKey(EmployeeData, verbose_name='Гид', on_delete=models.SET_NULL, null=True)
    registry_museum_id = models.ForeignKey(RegistryMuseum, verbose_name='Музей', on_delete=models.SET_NULL, null=True)
    datetime = models.DateTimeField(verbose_name='Дата, время')
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Музей группы'
        verbose_name_plural = 'Музеи групп'

    def __str__(self):
        return f'{self.registry_museum_id.name_organization} ({self.group_id.name_group})'


class GroupHotel(models.Model):
    group_id = models.ForeignKey(Group, verbose_name='Группа', on_delete=models.SET_NULL, null=True)
    registry_hotels_id = models.ForeignKey(RegistryHotels, verbose_name='Отель', on_delete=models.SET_NULL, null=True)
    arrival_date = models.DateTimeField(verbose_name='Дата заезда')
    departure_date = models.DateTimeField(verbose_name='Дата выезда')
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Отель группы'
        verbose_name_plural = 'Отели групп'

    def __str__(self):
        return f'{self.registry_hotels_id.name_organization} ({self.group_id.name_group})'


class GroupTransport(models.Model):
    group_id = models.ForeignKey(Group, verbose_name='Группа', on_delete=models.SET_NULL, null=True)
    registry_transport_organizations_id = models.ForeignKey(RegistryTransportOrganizations, verbose_name='Транспортная организация', on_delete=models.SET_NULL, null=True)
    type_tk_id = models.ForeignKey(CatalogData, verbose_name='Тип ТК', on_delete=models.SET_NULL, null=True)
    submission_address = models.CharField(verbose_name='Адрес подачи', max_length=100)
    submission_time = models.DateTimeField(verbose_name='Дата и время подачи')
    completion_address = models.CharField(verbose_name='Адрес завершения', max_length=100)
    completion_time = models.DateTimeField(verbose_name='Дата и время завершения')
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Транспорт группы'
        verbose_name_plural = 'Транспорт групп'

    def __str__(self):
        return f'{self.registry_transport_organizations_id.name_organization} ({self.group_id.name_group})'


class GroupFood(models.Model):
    group_id = models.ForeignKey(Group, verbose_name='Группа', on_delete=models.SET_NULL, null=True)
    registry_food_organizations_id = models.ForeignKey(RegistryFoodOrganizations, verbose_name='Организация по питанию', on_delete=models.SET_NULL, null=True)
    datetime = models.DateTimeField(verbose_name='Дата, время')
    type_meal_id = models.ForeignKey(CatalogData, verbose_name='Тип питания', on_delete=models.SET_NULL, null=True)
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Питание группы'
        verbose_name_plural = 'Питание групп'

    def __str__(self):
        return f'{self.registry_food_organizations_id.name_organization} ({self.group_id.name_group})'
