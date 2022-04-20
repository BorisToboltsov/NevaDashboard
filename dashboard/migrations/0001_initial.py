# Generated by Django 3.2 on 2022-04-20 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255, verbose_name='Значение')),
                ('sequence', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Данные справочника',
                'verbose_name_plural': 'Данные справочников',
            },
        ),
        migrations.CreateModel(
            name='CatalogName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Имя')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Название справочника',
                'verbose_name_plural': 'Название справочников',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=100, verbose_name='Фио')),
                ('post', models.CharField(blank=True, max_length=100, null=True, verbose_name='Должность')),
                ('organization', models.CharField(blank=True, max_length=100, null=True, verbose_name='Наименование организации')),
                ('department', models.CharField(blank=True, max_length=100, null=True, verbose_name='Отдел')),
                ('phone_number', models.CharField(blank=True, max_length=12, null=True, verbose_name='Номер телефона')),
                ('id_telegramm', models.PositiveIntegerField(blank=True, null=True, verbose_name='id телеграмма')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('actual_address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес фактический')),
                ('official_address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес юридический')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='EmployeeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=100, verbose_name='Фио сотрудника')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('contact_id', models.ManyToManyField(to='dashboard.Contact', verbose_name='Контакты')),
                ('post_employee_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.catalogdata', verbose_name='Должность сотрудника')),
            ],
            options={
                'verbose_name': 'Список сотрудников',
                'verbose_name_plural': 'Список сотрудников',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_group', models.CharField(choices=[('red', 'Красный'), ('blue', 'Синий'), ('orange', 'Оранжевый'), ('black', 'Черный'), ('green', 'Зеленый')], default='green', max_length=6, verbose_name='Цвет выделения')),
                ('type_group', models.CharField(choices=[('school', 'Школьная'), ('autogroup', 'Автогруппа'), ('vip', 'VIP')], max_length=9, verbose_name='Тип группы')),
                ('paid_status', models.CharField(choices=[('full', 'Полная'), ('not', 'Нет'), ('partial', 'Частичная')], max_length=8, verbose_name='Статус оплаты')),
                ('arrival_date_group', models.DateField(verbose_name='Дата прибытия')),
                ('arrival_time_group', models.TimeField(verbose_name='Время прибытия')),
                ('departure_date_group', models.DateField(verbose_name='Дата отъезда')),
                ('departure_time_group', models.TimeField(verbose_name='Время отъезда')),
                ('arrival', models.CharField(blank=True, max_length=255, null=True, verbose_name='Прибытие')),
                ('departure', models.CharField(blank=True, max_length=255, null=True, verbose_name='Отправление')),
                ('number_ru', models.CharField(max_length=50, verbose_name='Номер RU')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('manager_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.employeedata', verbose_name='Менеджер')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
        ),
        migrations.CreateModel(
            name='RegistryTransportOrganizations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_organization', models.CharField(max_length=255, verbose_name='Название организации')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('catalog_data_id', models.ManyToManyField(to='dashboard.CatalogData', verbose_name='Тип транспортного средства')),
                ('contact_id', models.ManyToManyField(to='dashboard.Contact', verbose_name='Контакты')),
            ],
            options={
                'verbose_name': 'Реестр транспортных компаний',
                'verbose_name_plural': 'Реестр транспортных компаний',
            },
        ),
        migrations.CreateModel(
            name='RegistrySendingTravelAgency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_organization', models.CharField(max_length=255, verbose_name='Название организации')),
                ('account_number', models.BigIntegerField(blank=True, null=True, unique=True, verbose_name='Номер счета')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('contact_id', models.ManyToManyField(to='dashboard.Contact', verbose_name='Контакты')),
            ],
            options={
                'verbose_name': 'Реестр отправляющих компаний',
                'verbose_name_plural': 'Реестр отправляющих компаний',
            },
        ),
        migrations.CreateModel(
            name='RegistryMuseum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_organization', models.CharField(max_length=255, verbose_name='Название организации')),
                ('online_ticket', models.CharField(blank=True, max_length=255, null=True, verbose_name='Онлайн билет')),
                ('order_adult', models.CharField(blank=True, max_length=255, null=True, verbose_name='Взрослый наряд')),
                ('order_school', models.CharField(blank=True, max_length=255, null=True, verbose_name='Школьный наряд')),
                ('number_group', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Количество человек в группе')),
                ('working_hours', models.CharField(blank=True, max_length=255, null=True, verbose_name='Время работы')),
                ('weekend', models.CharField(blank=True, max_length=255, null=True, verbose_name='Выходные')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('catalog_data_id', models.ManyToManyField(to='dashboard.CatalogData', verbose_name='Тип билета')),
                ('contact_id', models.ManyToManyField(to='dashboard.Contact', verbose_name='Контакты')),
            ],
            options={
                'verbose_name': 'Реестр музеев',
                'verbose_name_plural': 'Реестр музеев',
            },
        ),
        migrations.CreateModel(
            name='RegistryHotels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_organization', models.CharField(max_length=255, verbose_name='Название организации')),
                ('location', models.CharField(blank=True, max_length=255, null=True, verbose_name='Локация')),
                ('number_room', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Количество номером')),
                ('official_website', models.URLField(blank=True, null=True, verbose_name='Оффициальный website')),
                ('parking', models.CharField(blank=True, max_length=255, null=True, verbose_name='Наличие и стоимость парковки')),
                ('extra_space', models.CharField(blank=True, max_length=255, null=True, verbose_name='Возможность доп места')),
                ('early_check_in', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='Стоимость раннего заезда')),
                ('late_check_out', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='Стоимость позднего заезда')),
                ('conference_room', models.TextField(blank=True, null=True, verbose_name='Характеристики конференц зала + стоимость')),
                ('children', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='До скольких лет дети бесплатно')),
                ('disabled_people', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Количество номеров для инвалидов')),
                ('disabled_people_comment', models.TextField(blank=True, null=True, verbose_name='Комментарий к номера для инвалидов')),
                ('animals', models.CharField(blank=True, max_length=255, null=True, verbose_name='Размещение с животными')),
                ('restaurant', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тип ресторана')),
                ('breakfast_time', models.TimeField(blank=True, null=True, verbose_name='Время завтраков')),
                ('luggage_storage', models.CharField(blank=True, max_length=255, null=True, verbose_name='Камера хранения')),
                ('registration_fee', models.CharField(blank=True, max_length=255, null=True, verbose_name='Рег. сбор')),
                ('connect', models.CharField(blank=True, max_length=255, null=True, verbose_name='Коннекты')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('contact_id', models.ManyToManyField(to='dashboard.Contact', verbose_name='Контакты')),
                ('number_stars_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.catalogdata', verbose_name='Количество звезд')),
            ],
            options={
                'verbose_name': 'Реестр отелей',
                'verbose_name_plural': 'Реестр отелей',
            },
        ),
        migrations.CreateModel(
            name='RegistryFoodOrganizations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_organization', models.CharField(max_length=255, verbose_name='Название организации')),
                ('legal_name_organization', models.CharField(blank=True, max_length=255, null=True, verbose_name='Юр. название организации')),
                ('operation_mode', models.CharField(blank=True, max_length=255, null=True, verbose_name='Режим работы')),
                ('capacity', models.SmallIntegerField(blank=True, null=True, verbose_name='Вместимость')),
                ('capacity_comment', models.TextField(blank=True, null=True, verbose_name='Комментарий к вместимости')),
                ('positive_rating', models.SmallIntegerField(blank=True, null=True, verbose_name='Положительный рейтинг')),
                ('negative_rating', models.SmallIntegerField(blank=True, null=True, verbose_name='Отрицательный рейтинг')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('catalog_data_id', models.ManyToManyField(to='dashboard.CatalogData', verbose_name='Тип кухни')),
                ('contact_id', models.ManyToManyField(to='dashboard.Contact', verbose_name='Контакты')),
            ],
            options={
                'verbose_name': 'Реестр организаций по питанию',
                'verbose_name_plural': 'Реестр организаций по питанию',
            },
        ),
        migrations.CreateModel(
            name='GroupTransport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_address', models.CharField(max_length=100, verbose_name='Адрес подачи')),
                ('submission_time', models.DateTimeField(verbose_name='Дата и время подачи')),
                ('completion_address', models.CharField(max_length=100, verbose_name='Адрес завершения')),
                ('completion_time', models.DateTimeField(verbose_name='Дата и время завершения')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('group_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.group', verbose_name='Группа')),
                ('registry_transport_organizations_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.registrytransportorganizations', verbose_name='Транспортная организация')),
                ('type_tk_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.catalogdata', verbose_name='Тип ТК')),
            ],
            options={
                'verbose_name': 'Транспорт группы',
                'verbose_name_plural': 'Транспорт групп',
            },
        ),
        migrations.CreateModel(
            name='GroupMuseum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(verbose_name='Дата, время')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('group_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.group', verbose_name='Группа')),
                ('guide_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.employeedata', verbose_name='Гид')),
                ('registry_museum_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.registrymuseum', verbose_name='Музей')),
            ],
            options={
                'verbose_name': 'Музей группы',
                'verbose_name_plural': 'Музеи групп',
            },
        ),
        migrations.CreateModel(
            name='GroupHotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival_date_hotel', models.DateField(verbose_name='Дата заезда')),
                ('departure_date_hotel', models.DateField(verbose_name='Дата выезда')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('group_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.group', verbose_name='Группа')),
                ('registry_hotels_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.registryhotels', verbose_name='Отель')),
            ],
            options={
                'verbose_name': 'Отель группы',
                'verbose_name_plural': 'Отели групп',
            },
        ),
        migrations.CreateModel(
            name='GroupFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(verbose_name='Дата, время')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('group_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.group', verbose_name='Группа')),
                ('registry_food_organizations_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.registryfoodorganizations', verbose_name='Организация по питанию')),
                ('type_meal_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.catalogdata', verbose_name='Тип питания')),
            ],
            options={
                'verbose_name': 'Питание группы',
                'verbose_name_plural': 'Питание групп',
            },
        ),
        migrations.CreateModel(
            name='GroupDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_people', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Количество человек')),
                ('number_people_school', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Количество школьников')),
                ('number_people_adult', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Количество взрослых')),
                ('number_people_escort', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Количество сопровождающих')),
                ('number_people_driver', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Количество водителей')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('group_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.group', verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'День группы группы',
                'verbose_name_plural': 'Дни группы группы',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='registry_sending_travel_agency_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.registrysendingtravelagency', verbose_name='Агенство по отправке'),
        ),
        migrations.AddField(
            model_name='catalogdata',
            name='catalog_name_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.catalogname', verbose_name='Название каталога'),
        ),
    ]
