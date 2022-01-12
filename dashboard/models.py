from django.db import models


# Create your models here.


class CatalogName(models.Model):  # Название справочников
    name = models.CharField(verbose_name='Имя', max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CatalogData(models.Model):  # Данные справочника
    catalog_name_id = models.ForeignKey(CatalogName, on_delete=models.SET_NULL)
    value = models.CharField(verbose_name='Значение', max_length=255)
    sequence = models.PositiveBigIntegerField(verbose_name='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Contact(models.Model):
    fio = models.CharField(verbose_name='Фио', max_length=100)
    post = models.CharField(verbose_name='Должность', max_length=100)
    organization = models.CharField(verbose_name='Наименование организации', max_length=100)
    department = models.CharField(verbose_name='Отдел', max_length=100)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=12)
    id_telegramm = models.PositiveIntegerField(verbose_name='id телеграмма')
    email = models.EmailField(verbose_name='Email')
    actual_address = models.CharField(verbose_name='Адрес фактический', max_length=255)
    official_address = models.CharField(verbose_name='Адрес юридический', max_length=255)
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class RegistrySendingTravelAgency(models.Model):  # Реестр отправляющих компаний
    contact_id = models.ManyToManyField(Contact)
    name_organization = models.CharField(verbose_name='Название организации', max_length=255)
    account_number = models.BigIntegerField(verbose_name='Номер счета', null=False, blank=True, unique=True)
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class RegistryTransportOrganizations(models.Model):  # Реестр транспортных компаний
    contact_id = models.ManyToManyField(Contact)
    name_organization = models.CharField(verbose_name='Название организации', max_length=255)
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)
    catalog_data_id = models.ManyToManyField(
        CatalogData)  # m-m CatalogData 'Автобусы', 'Флот', 'Л\А'. В разных сочетаниях
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class RegistryFoodOrganizations(models.Model):  # Реестр организация по питанию.
    contact_id = models.ManyToManyField(Contact)
    catalog_data_id = models.ManyToManyField(
        CatalogData)  # m-m CatalogData Варианты кухни (Европейская, Русская, Итальянская, Немецкая, Индийская, нет данных и т.д.) Могут быть в различных сочетаниях
    name_organization = models.CharField(verbose_name='Название организации', max_length=255)
    legal_name_organization = models.Model(verbose_name='Юр. название организации', max_length=255)
    operation_mode = models.CharField(verbose_name='Режим работы', max_length=255)
    capacity = models.SmallIntegerField(verbose_name='Вместимость')
    capacity_comment = models.TextField(verbose_name='Комментарий к вместимости', blank=True, null=True)
    positive_rating = models.SmallIntegerField(verbose_name='Положительный рейтинг')
    negative_rating = models.SmallIntegerField(verbose_name='Отрицательный рейтинг')
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class RegistryHotels(models.Model):  # Реестр отелей
    contact_id = models.ManyToManyField(Contact)
    name_organization = models.CharField(verbose_name='Название организации', max_length=255)
    number_stars_id = models.ForeignKey(CatalogData, on_delete=models.SET_NULL)  # Количество звезд
    location = models.CharField(verbose_name='Локация', max_length=255)
    number_room = models.PositiveSmallIntegerField(verbose_name='Количество номером')
    official_website = models.URLField(verbose_name='Оффициальный website')
    parking = models.CharField(verbose_name='Наличие и стоимость парковки', max_length=255)
    extra_space = models.CharField(verbose_name='Возможность доп места', max_length=255)
    early_check_in = models.DecimalField(verbose_name='Стоимость раннего заезда', max_digits=9, decimal_places=2)
    late_check_out = models.DecimalField(verbose_name='Стоимость позднего заезда', max_digits=9, decimal_places=2)
    conference_room = models.TextField(verbose_name='Характеристики конференц зала + стоимость', blank=True, null=True)
    children = models.PositiveSmallIntegerField(verbose_name='До скольких лет дети бесплатно')
    disabled_people = models.PositiveSmallIntegerField(verbose_name='Количество номеров для инвалидов')
    disabled_people_comment = models.TextField(verbose_name='Комментарий к номера для инвалидов', blank=True, null=True)
    animals = models.CharField(verbose_name='Размещение с животными', max_length=255)
    restaurant = models.CharField(verbose_name='Тип ресторана', max_length=255)
    breakfast_time = models.TimeField(verbose_name='Время завтраков')
    luggage_storage = models.CharField(verbose_name='Камера хранения', max_length=255)
    registration_fee = models.CharField(verbose_name='Рег. сбор', max_length=255)
    connect = models.CharField(verbose_name='Коннекты', max_length=255)
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class RegistryMuseum(models.Model):  # Реестр музеев
    contact_id = models.ManyToManyField(Contact)
    catalog_data_id = models.ManyToManyField(CatalogData)  # m-m CatalogData реестр музеев тип билета + цена на билет'
    name_organization = models.CharField(verbose_name='Название организации', max_length=255)
    online_ticket = models.CharField(verbose_name='Онлайн билет', max_length=255)
    order_adult = models.CharField(verbose_name='Взрослый наряд', max_length=255)
    order_school = models.CharField(verbose_name='Школьный наряд', max_length=255)
    number_group = models.PositiveSmallIntegerField(verbose_name='Количество человек в группе')
    working_hours = models.CharField(verbose_name='Время работы', max_length=255)
    weekend = models.CharField(verbose_name='Выходные', max_length=255)
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class EmployeeData(models.Model):  # Список сотрудников
    contact_id = models.ManyToManyField(Contact)
    fio = models.CharField(verbose_name='Фио сотрудника', max_length=100)
    post_employee_id = models.ForeignKey(CatalogData, on_delete=models.SET_NULL)  # Должность сотрудника
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Group(models.Model):
    name_group = models.CharField(verbose_name='Название группы', max_length=255)
    number_people = models.PositiveSmallIntegerField(verbose_name='Количество человек')
    school_group = models.CharField(verbose_name='Школьная группа', max_length=255)
    paid_status = models.CharField(verbose_name='Статус оплаты', max_length=50)
    registry_sending_travel_agency_id = models.ForeignKey(RegistrySendingTravelAgency, on_delete=models.SET_NULL)
    arrival_date = models.DateTimeField(verbose_name='Дата прибытия')
    departure_date = models.DateTimeField(verbose_name='Дата отъезда')
    manager_id = models.ForeignKey(EmployeeData, on_delete=models.SET_NULL)
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class GroupMuseum(models.Model):
    group_id = models.ForeignKey(Group, on_delete=models.SET_NULL)
    guide_id = models.ForeignKey(EmployeeData, on_delete=models.SET_NULL)
    registry_museum_id = models.ForeignKey(RegistryMuseum, on_delete=models.SET_NULL)
    datetime = models.DateTimeField(verbose_name='Дата, время')
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class GroupHotel(models.Model):
    group_id = models.ForeignKey(Group, on_delete=models.SET_NULL)
    registry_hotels_id = models.ForeignKey(RegistryHotels, on_delete=models.SET_NULL)
    arrival_date = models.DateTimeField(verbose_name='Дата заезда')
    departure_date = models.DateTimeField(verbose_name='Дата выезда')
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class GroupTransport(models.Model):
    group_id = models.ForeignKey(Group, on_delete=models.SET_NULL)
    registry_transport_organizations_id = models.ForeignKey(RegistryTransportOrganizations, on_delete=models.SET_NULL)
    type_tk_id = models.ForeignKey(CatalogData, on_delete=models.SET_NULL)
    submission_address = models.CharField(verbose_name='Адрес подачи', max_length=100)
    submission_time = models.DateTimeField(verbose_name='Дата и время подачи')
    completion_address = models.CharField(verbose_name='Адрес завершения', max_length=100)
    completion_time = models.DateTimeField(verbose_name='Дата и время завершения')
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class GroupFood(models.Model):
    group_id = models.ForeignKey(Group, on_delete=models.SET_NULL)
    registry_food_organizations_id = models.ForeignKey(RegistryFoodOrganizations, on_delete=models.SET_NULL)
    datetime = models.DateTimeField(verbose_name='Дата, время')
    type_meal_id = models.ForeignKey(CatalogData, on_delete=models.SET_NULL)
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
