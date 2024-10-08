# Generated by Django 5.1.1 on 2024-10-07 13:21

import apps.house.choices
import apps.house.validators
import django.contrib.gis.db.models.fields
import django.core.validators
import django.db.models.deletion
import django_admin_geomap
import hashid_field.field
import mptt.fields
import versatileimagefield.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Communication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_light', models.BooleanField(default=False, verbose_name='Свет')),
                ('has_gas', models.BooleanField(default=False, verbose_name='Газ')),
                ('has_internet', models.BooleanField(default=False, verbose_name='Интернет')),
                ('has_heating', models.BooleanField(default=False, verbose_name='Отопление')),
                ('has_water', models.BooleanField(default=False, verbose_name='Вода')),
                ('has_phone', models.BooleanField(default=False, verbose_name='Телефон')),
                ('has_sewage', models.BooleanField(default=False, verbose_name='Канализация')),
            ],
            options={
                'verbose_name': 'Коммуникации',
                'verbose_name_plural': 'Коммуникации',
            },
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_contract', models.BooleanField(blank=True, default=False, null=True, verbose_name='договор купли-продажи')),
                ('deed_of_gift', models.BooleanField(blank=True, default=False, null=True, verbose_name='договор дарения')),
                ('share_agreement', models.BooleanField(blank=True, default=False, null=True, verbose_name='договор долевого участия')),
                ('technical_passport', models.BooleanField(blank=True, default=False, null=True, verbose_name='технический паспорт')),
                ('commissioning_certificate', models.BooleanField(blank=True, default=False, null=True, verbose_name='акт ввода в эксплуатацию')),
                ('red_book', models.BooleanField(blank=True, default=False, null=True, verbose_name='красная книга')),
                ('green_book', models.BooleanField(blank=True, default=False, null=True, verbose_name='зеленая книга')),
                ('certificate_of_right', models.BooleanField(blank=True, default=False, null=True, verbose_name='свидетельство о праве на наследство')),
            ],
            options={
                'verbose_name': 'Правоустанавливающие документы',
                'verbose_name_plural': 'Правоустанавливающие документы',
            },
        ),
        migrations.CreateModel(
            name='Miscellaneous',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plastic_windows', models.BooleanField(blank=True, default=False, null=True, verbose_name='пластиковые окна')),
                ('improved', models.BooleanField(blank=True, default=False, null=True, verbose_name='улучшенная')),
                ('studio_kitchen', models.BooleanField(blank=True, default=False, null=True, verbose_name='кухня-студия')),
                ('new_plumbing', models.BooleanField(blank=True, default=False, null=True, verbose_name='новая сантехника')),
                ('air_conditioner', models.BooleanField(blank=True, default=False, null=True, verbose_name='кондиционер')),
                ('isolated_rooms', models.BooleanField(blank=True, default=False, null=True, verbose_name='комнаты изолированы')),
                ('built_in_kitchen', models.BooleanField(blank=True, default=False, null=True, verbose_name='встроенная кухня')),
                ('pantry', models.BooleanField(blank=True, default=False, null=True, verbose_name='кладовка')),
                ('quiet_courtyard', models.BooleanField(blank=True, default=False, null=True, verbose_name='тихий двор')),
                ('convenient_for_business', models.BooleanField(blank=True, default=False, null=True, verbose_name='удобно под бизнес')),
            ],
            options={
                'verbose_name': 'Разное',
                'verbose_name_plural': 'Разное',
            },
        ),
        migrations.CreateModel(
            name='Security',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('window_bars', models.BooleanField(blank=True, default=False, null=True, verbose_name='Решетки на окнах')),
                ('alarm_system', models.BooleanField(blank=True, default=False, null=True, verbose_name='Сигнализация')),
                ('intercom', models.BooleanField(blank=True, default=False, null=True, verbose_name='домофон')),
                ('video_intercom', models.BooleanField(blank=True, default=False, null=True, verbose_name='видеодомофон')),
                ('code_lock', models.BooleanField(blank=True, default=False, null=True, verbose_name='кодовый замок')),
                ('video_surveillance', models.BooleanField(blank=True, default=False, null=True, verbose_name='видеонаблюдение')),
                ('concierge', models.BooleanField(blank=True, default=False, null=True, verbose_name='консьерж')),
            ],
            options={
                'verbose_name': 'Безопасность',
                'verbose_name_plural': 'Безопасность',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255)),
                ('lat', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('lng', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('population', models.IntegerField(blank=True, null=True)),
                ('iso2', models.CharField(blank=True, max_length=2, null=True)),
                ('capital', models.CharField(blank=True, max_length=50, null=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='house.location')),
            ],
            options={
                'verbose_name': 'Городы',
                'verbose_name_plural': 'Городы',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', hashid_field.field.HashidAutoField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', min_length=25, prefix='', primary_key=True, serialize=False)),
                ('type_deal', models.CharField(choices=[('Sell', 'Продажа'), ('Rental', 'Аренда')], max_length=50, verbose_name='Тип сделки')),
                ('type_property', models.CharField(choices=[('House', 'Дом'), ('Apartment', 'Квартира'), ('Commercial property', 'Коммерческая недвижимость'), ('Land plot', 'Участок'), ('Cottage', 'Дача'), ('Parking/Garage', 'Паркинг/Гараж')], max_length=50, verbose_name='Тип недвижимости')),
                ('room_count', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6 or more', '6 и более'), ('Open plan', 'Свободная планировка')], max_length=50, null=True, verbose_name='Количество комнат')),
                ('type_series', models.CharField(blank=True, choices=[('102 series', '102 серия'), ('104 series', '104 серия'), ('Improved 104 series', '104 серия улучшенная'), ('105 series', '105 серия'), ('Improved 105 series', '105 серия улучшенная'), ('106 series', '106 серия'), ('Improved 106 series', '106 серия улучшенная'), ('Stalinka', 'Сталинка'), ('Khrushchevka', 'Хрущевка'), ('Individual layout', 'Индивид. планировка')], max_length=50, null=True, verbose_name='Серия')),
                ('type_building', models.CharField(blank=True, choices=[('Brick', 'Кирпичный'), ('Panel', 'Панельный'), ('Monolith', 'Монолитный')], max_length=50, null=True, verbose_name='Тип строения')),
                ('year_construction', models.IntegerField(blank=True, choices=apps.house.choices.year_choices, default=apps.house.choices.current_year, null=True, verbose_name='Год построения')),
                ('floor_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Этаж')),
                ('total_floors', models.CharField(blank=True, max_length=50, null=True, verbose_name='из всего этажей')),
                ('general', models.FloatField(max_length=50, verbose_name='общая')),
                ('residential', models.FloatField(blank=True, max_length=50, null=True, verbose_name='жилая')),
                ('kitchen', models.FloatField(blank=True, max_length=50, null=True, verbose_name='кухня')),
                ('ceiling_height', models.CharField(blank=True, max_length=50, null=True, verbose_name='Высота потолков')),
                ('land_area', models.IntegerField(blank=True, null=True, verbose_name='Площадь учатска')),
                ('type_heating', models.CharField(blank=True, choices=[('Central', 'Центральное'), ('Gas', 'На газе'), ('Electric', 'Электрическое'), ('Mixed', 'Смешанное'), ('Solid fuel', 'На твердом топливе'), ('Liquid fuel', 'На жидком топливе'), ('No heating', 'Без отопления'), ('Autonomous', 'Автономное')], max_length=50, null=True, verbose_name='Тип отопления')),
                ('type_condition', models.CharField(blank=True, choices=[('Under finishing', 'Под самоотделку'), ('Euro renovation', 'Евроремонт'), ('Good', 'Хорошее'), ('Average', 'Среднее'), ('Not finished', 'Не достроено')], max_length=50, null=True, verbose_name='Состояние')),
                ('eni_code', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('^\\d{10}$', code='invalid_eni', message='The UNI code must consist of 10 digits ***')], verbose_name='Код ЕНИ')),
                ('street', models.CharField(blank=True, max_length=50, null=True, verbose_name='Улица')),
                ('house_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='№ дома')),
                ('intersection_with', models.CharField(blank=True, max_length=50, null=True, verbose_name='Пересечение с')),
                ('point', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('youtube_url', models.URLField(blank=True, help_text='Вставьте ссылку на YouTube видео', null=True, validators=[apps.house.validators.validate_youtube_url], verbose_name='Ссылка на видео')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('currency', models.CharField(choices=[('USD', 'Доллар'), ('SOM', 'Сом')], max_length=50, verbose_name='Цена')),
                ('price_for', models.CharField(choices=[('For the whole', 'За все'), ('Per meter', 'За метр')], max_length=50, verbose_name='Цена за')),
                ('installment_type', models.CharField(blank=True, choices=[('Yes', 'Жок'), ('No', 'Нет')], max_length=50, null=True, verbose_name='Возможность рассрочки')),
                ('mortage_type', models.CharField(blank=True, choices=[('Yes', 'Есть'), ('No', 'Нет')], max_length=50, null=True, verbose_name='Возможность ипотеки')),
                ('exchange_type', models.CharField(blank=True, choices=[('Open to options', 'Рассмотрю варианты'), ('With buyers extra payment', 'С доплатой покупателя'), ('With sellers extra payment', 'С доплатой продавца'), ('Key for key', 'Ключ на ключ'), ('No exchange offers', 'Обмен не предлагать'), ('Exchange for a car', 'Обмен на авто')], max_length=50, null=True, verbose_name='Возможность обмена')),
                ('advertiser_type', models.CharField(choices=[('proprietor', 'Собственник'), ('Agent', 'Агент')], max_length=50, verbose_name='От чьего имени подается объявление')),
                ('phone_connection', models.CharField(blank=True, choices=[('Available', 'Есть'), ('Possible connection', 'Возможно подключение'), ('Not available', 'Нет')], max_length=100, null=True)),
                ('drinking_water', models.CharField(blank=True, choices=[('central_water_supply', 'Центральное водоснабжение'), ('possible_connection', 'Возможно подведение'), ('well', 'Скважина'), ('no', 'Нет')], max_length=100, null=True)),
                ('sewage', models.CharField(blank=True, choices=[('central', 'Центральная'), ('possible_connection', 'Возможно подведение'), ('septic', 'Септик'), ('no', 'Нет')], max_length=100, null=True)),
                ('electricity', models.CharField(blank=True, choices=[('yes', 'Есть'), ('possible_connection', 'Возможно подведение'), ('no', 'Нет')], max_length=100, null=True)),
                ('disposition_object', models.CharField(blank=True, choices=[('in_city', 'В городе'), ('along_road', 'Вдоль трассы'), ('in_hills', 'В предгорьях'), ('in_suburbs', 'В пригороде'), ('near_water', 'Возле водоема'), ('in_summer_cottage_area', 'В дачном массиве')], max_length=100, null=True, verbose_name='Расположение обьекта')),
                ('bathroom', models.CharField(blank=True, choices=[('Separate', 'Раздельный'), ('Combined', 'Совмещенный'), ('2 or more bathrooms', '2 с/у и более'), ('No bathroom', 'Нет')], max_length=100, null=True)),
                ('parking', models.CharField(blank=True, choices=[('Parking', 'Паркинг'), ('Garage', 'Гараж'), ('Nearby guarded parking', 'Рядом охраняемая стоянка')], max_length=100, null=True)),
                ('balkony', models.CharField(blank=True, choices=[('Balcony', 'Балкон'), ('Glazed balcony', 'Застекленный балкон'), ('Loggia', 'Лоджия'), ('No balcony', 'Нет')], max_length=100, null=True)),
                ('front_door', models.CharField(blank=True, choices=[('Wooden', 'Деревянная'), ('Metal', 'Металлическая'), ('Armored', 'Бронированная'), ('No door', 'Нет')], max_length=100, null=True)),
                ('furniture', models.CharField(blank=True, choices=[('Fully furnished', 'Полностью меблирована'), ('Partially furnished', 'Частично меблирована'), ('Unfurnished', 'Пустая')], max_length=100, null=True)),
                ('gas', models.CharField(blank=True, choices=[('Main pipeline', 'Магистральный'), ('Autonomous', 'Автономный'), ('Possible connection', 'Возможно подключение'), ('No gas', 'Нет')], max_length=100, null=True)),
                ('internet', models.CharField(blank=True, choices=[('ADSL', 'ADSL'), ('Wired', 'Проводной'), ('Fiber optic', 'Оптика')], max_length=100, null=True)),
                ('floor', models.CharField(blank=True, choices=[('Linoleum', 'Линолеум'), ('Parquet', 'Паркет'), ('Laminate', 'Ламинат'), ('Wood', 'Дерево'), ('Carpet', 'Ковролин'), ('Tile', 'Плитка'), ('Cork flooring', 'Пробковое')], max_length=100, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=16, null=True, verbose_name='Второй Номер телефона пользователя')),
                ('views', models.PositiveIntegerField(blank=True, default=1)),
                ('active_post', models.BooleanField(default=True, verbose_name='Активный пост')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('communication', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='house.communication', verbose_name='Коммуникации')),
                ('documents', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='documents_property', to='house.documents', verbose_name='Правоустанавливающие документы')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='house.location', verbose_name='Расположение')),
                ('miscellaneous', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='miscellaneous_property', to='house.miscellaneous', verbose_name='Разное')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Недвижимость',
                'verbose_name_plural': 'Недвижимость',
            },
        ),
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pictures', versatileimagefield.fields.VersatileImageField(upload_to='house/user/pictures/list/')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties_pictures', to='house.property')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
            },
        ),
        migrations.CreateModel(
            name='ResidentialCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complex_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название комплекса')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('object_state', models.CharField(choices=[('scheduled', 'запланирован'), ('under construction', 'строится'), ('finalized', 'завершен'), ('commissioned', 'сдан в эксплуатацию'), ('frozen', 'заморожен')], max_length=50, verbose_name='Состояние обьекта')),
                ('ceiling_height', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Высота потолков')),
                ('type_heating', models.CharField(blank=True, choices=[('Central', 'Центральное'), ('Gas', 'На газе'), ('Electric', 'Электрическое'), ('Mixed', 'Смешанное'), ('Solid fuel', 'На твердом топливе'), ('Liquid fuel', 'На жидком топливе'), ('No heating', 'Без отопления'), ('Autonomous', 'Автономное')], max_length=50, null=True, verbose_name='Тип отопления')),
                ('type_building', models.CharField(blank=True, choices=[('Brick', 'Кирпичный'), ('Panel', 'Панельный'), ('Monolith', 'Монолитный')], max_length=50, null=True, verbose_name='Тип строения')),
                ('storey', models.IntegerField(validators=[django.core.validators.MaxValueValidator(50)], verbose_name='Этажность')),
                ('housing_class', models.CharField(choices=[('econom', 'эконом'), ('comfort', 'комфорт'), ('business', 'бизнес'), ('premuim', 'премуим')], max_length=50, verbose_name='Тип класса')),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('about_complex', models.TextField(blank=True, null=True, verbose_name='Об объекте')),
                ('media', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('building_date', models.DateField(auto_now_add=True, null=True, verbose_name='Дата постройки комплекса')),
                ('due_date', models.DateField(verbose_name='Дата сдачи')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='house.location', verbose_name='Расположение обьекта')),
            ],
            options={
                'verbose_name': 'Жилой комплекс',
                'verbose_name_plural': 'Жилой комплекс',
                'ordering': ['id'],
            },
            bases=(models.Model, django_admin_geomap.GeoItem),
        ),
        migrations.AddField(
            model_name='property',
            name='complex_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='complex_property', to='house.residentialcategory', verbose_name='Название комплекса'),
        ),
        migrations.AddField(
            model_name='property',
            name='security',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='security_property', to='house.security', verbose_name='Безопасность'),
        ),
    ]
