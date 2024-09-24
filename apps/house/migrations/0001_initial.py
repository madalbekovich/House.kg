# Generated by Django 5.1.1 on 2024-09-23 16:30

import apps.house.choices
import apps.house.validators
import django.core.validators
import django.db.models.deletion
import mptt.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advertiser_type', models.CharField(choices=[('proprietor', 'Собственник'), ('Agent', 'Агент')], max_length=50, verbose_name='От чьего имени подается объявление')),
            ],
            options={
                'verbose_name': 'ContactInfn',
                'verbose_name_plural': 'ContactInfos',
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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('type_deal', models.CharField(choices=[('Sell', 'Продажа'), ('Rental', 'Аренда')], max_length=50, verbose_name='Тип сделки')),
                ('type_property', models.CharField(choices=[('House', 'Дом'), ('Apartment', 'Квартира'), ('Commercial property', 'Коммерческая недвижимость'), ('Land plot', 'Участок'), ('Cottage', 'Дача'), ('Parking/Garage', 'Паркинг/Гараж')], max_length=50, verbose_name='Тип недвижимости')),
                ('room_count', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6 or more', '6 и более'), ('Open plan', 'Свободная планировка')], max_length=50, verbose_name='Количество комнат')),
                ('type_series', models.CharField(choices=[('102 series', '102 серия'), ('104 series', '104 серия'), ('Improved 104 series', '104 серия улучшенная'), ('105 series', '105 серия'), ('Improved 105 series', '105 серия улучшенная'), ('106 series', '106 серия'), ('Improved 106 series', '106 серия улучшенная'), ('Stalinka', 'Сталинка'), ('Khrushchevka', 'Хрущевка'), ('Individual layout', 'Индивид. планировка')], max_length=50, verbose_name='Серия')),
                ('type_building', models.CharField(choices=[('Brick', 'Кирпичный'), ('Panel', 'Панельный'), ('Monolith', 'Монолитный')], max_length=50, verbose_name='Тип строения')),
                ('year_construction', models.IntegerField(blank=True, choices=apps.house.choices.year_choices, default=apps.house.choices.current_year, null=True, verbose_name='Год построения')),
                ('floor_number', models.CharField(max_length=50, verbose_name='Этаж')),
                ('total_floors', models.CharField(max_length=50, verbose_name='из всего этажей')),
                ('general', models.FloatField(max_length=50, verbose_name='общая')),
                ('residential', models.FloatField(blank=True, max_length=50, null=True, verbose_name='жилая')),
                ('kitchen', models.FloatField(blank=True, max_length=50, null=True, verbose_name='кухня')),
                ('type_heating', models.CharField(blank=True, choices=[('Central', 'Центральное'), ('Gas', 'На газе'), ('Electric', 'Электрическое'), ('Mixed', 'Смешанное'), ('Solid fuel', 'На твердом топливе'), ('Liquid fuel', 'На жидком топливе'), ('No heating', 'Без отопления'), ('Autonomous', 'Автономное')], max_length=50, null=True, verbose_name='Тип отопления')),
                ('type_condition', models.CharField(choices=[('Under finishing', 'Под самоотделку'), ('Euro renovation', 'Евроремонт'), ('Good', 'Хорошее'), ('Average', 'Среднее'), ('Not finished', 'Не достроено')], max_length=50, verbose_name='Состояние')),
                ('eni_code', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('^\\d{10}$', code='invalid_eni', message='The UNI code must consist of 10 digits ***')], verbose_name='Код ЕНИ')),
                ('street', models.CharField(blank=True, max_length=50, null=True, verbose_name='Улица')),
                ('house_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='№ дома')),
                ('intersection_with', models.CharField(blank=True, max_length=50, null=True, verbose_name='Пересечение с')),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Широта')),
                ('lon', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Долгата')),
                ('youtube_url', models.URLField(blank=True, help_text='Вставьте ссылку на YouTube видео', null=True, validators=[apps.house.validators.validate_youtube_url], verbose_name='Ссылка на видео')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Цена')),
                ('currency', models.CharField(choices=[('USD', 'Доллар'), ('SOM', 'Сом')], max_length=50, verbose_name='Цена')),
                ('price_for', models.CharField(choices=[('For the whole', 'За все'), ('Per meter', 'За метр')], max_length=50, verbose_name='Цена за')),
                ('installment_type', models.CharField(blank=True, choices=[('Yes', 'Жок'), ('No', 'Нет')], max_length=50, null=True, verbose_name='Возможность рассрочки')),
                ('mortage_type', models.CharField(blank=True, choices=[('Yes', 'Есть'), ('No', 'Нет')], max_length=50, null=True, verbose_name='Возможность ипотеки')),
                ('exchange_type', models.CharField(blank=True, choices=[('Open to options', 'Рассмотрю варианты'), ('With buyers extra payment', 'С доплатой покупателя'), ('With sellers extra payment', 'С доплатой продавца'), ('Key for key', 'Ключ на ключ'), ('No exchange offers', 'Обмен не предлагать'), ('Exchange for a car', 'Обмен на авто')], max_length=50, null=True, verbose_name='Возможность обмена')),
                ('documents', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='documents_property', to='house.documents', verbose_name='Правоустанавливающие документы')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='house.location', verbose_name='Расположение')),
                ('miscellaneous', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='miscellaneous_property', to='house.miscellaneous', verbose_name='Разное')),
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
                ('pictures', models.ImageField(upload_to='house/user/pictures/list/')),
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
                ('building_date', models.DateField(auto_now_add=True, null=True, verbose_name='Дата постройки комплекса')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='house.residentialcategory')),
            ],
            options={
                'verbose_name': 'Жилой комплекс',
                'verbose_name_plural': 'Жилой комплекс',
            },
        ),
        migrations.AddField(
            model_name='property',
            name='complex_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='complex_property', to='house.residentialcategory', verbose_name='Название комплекса'),
        ),
        migrations.AddField(
            model_name='property',
            name='security',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='security_property', to='house.security', verbose_name='Безопасность'),
        ),
    ]
