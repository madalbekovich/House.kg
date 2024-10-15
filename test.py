import json
import re
import os
import sys
import django

sys.path.append(os.path.join(os.path.dirname(__file__), 'core'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

django.setup()

# from apps.house.models import Location

# def clean_coordinate(coord):
#     """Очищает координату от ненужных символов и преобразует в float."""
#     if coord:
#         cleaned_coord = re.sub(r'[^\d.,-]', '', coord).replace(',', '.')
#         try:
#             return float(cleaned_coord)
#         except ValueError:
#             return None
#     return None

# def load_kg_cities(file_path):
#     """
#     Загружает данные городов из JSON файла и сохраняет их в базе данных.
#     """
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             data = json.load(file)

#         if not isinstance(data, list):
#             raise ValueError("JSON file should contain a list of cities.")

#         areas = {}

#         for entry in data:
#             area_name = entry.get('admin_name', '')
#             city_name = entry.get('city', '')
#             lat = clean_coordinate(entry.get('lat', ''))
#             lng = clean_coordinate(entry.get('lng', ''))
#             iso2 = entry.get('iso2', '')
#             admin_name = entry.get('admin_name', )
#             population = entry.get('population', '')

#             if area_name and area_name not in areas:
#                 area = Location.objects.create(city=area_name)
#                 areas[area_name] = area
#                 print(f"Area {area_name} created.")

#             if city_name and area_name in areas:
#                 Location.objects.create(city=city_name, parent=areas[area_name], lat=lat, lng=lng, population=population, admin_name=admin_name, iso2=iso2)
#                 print(f"City {city_name} created under area {area_name}.")

#     except Exception as e:
#         print(f"Error occurred: {e}")

#     print("Данные успешно загружены.")

# if __name__ == "__main__":
#     load_kg_cities('kg.json')


# import random
# from faker import Faker
# from apps.house.models import ResidentialCategory, Location  # Замените your_app на имя вашего приложения
# from apps.house.choices import HOUSING_CLASS, OBJECT_STATE, HEATING_CHOICES, BUILDING_TYPE_CHOICES
# from datetime import datetime, timedelta

# fake = Faker()

# # Получите существующие Locations
# locations = Location.objects.all()

# lat_min, lat_max = 42.810, 42.950  
# lon_min, lon_max = 74.510, 74.640 

# # Генерация 20 объектов ResidentialCategory
# for _ in range(20):
#     complex_name = fake.company()  # Генерация случайного названия комплекса
#     price = random.randint(50000, 150000)  # Генерация случайной цены
#     object_state = random.choice(list(dict(OBJECT_STATE).keys()))  # Случайное состояние объекта
#     ceiling_height = round(random.uniform(2.5, 4.5), 2) if random.choice([True, False]) else None  # Высота потолков
#     type_heating = random.choice(list(dict(HEATING_CHOICES).keys())) if random.choice([True, False]) else None  # Тип отопления
#     type_building = random.choice(list(dict(BUILDING_TYPE_CHOICES).keys())) if random.choice([True, False]) else None  # Тип строения
#     storey = random.randint(1, 50)  # Этажность
#     housing_class = random.choice(list(dict(HOUSING_CLASS).keys()))  # Тип класса
#     lon = round(random.uniform(lon_min, lon_max), 6) 
#     lat = round(random.uniform(lat_min, lat_max), 6) 
#     location = random.choice(locations)  # Случайное местоположение
#     about_complex = fake.paragraph()  # Описание комплекса
#     building_date = fake.date_between(start_date='-50y', end_date='today')  # Дата постройки комплекса
#     due_date = building_date + timedelta(days=random.randint(30, 365*3))  # Дата сдачи

#     ResidentialCategory.objects.create(
#         complex_name=complex_name,
#         price=price,
#         object_state=object_state,
#         ceiling_height=ceiling_height,
#         type_heating=type_heating,
#         type_building=type_building,
#         storey=storey,
#         housing_class=housing_class,
#         lon=lon,
#         lat=lat,
#         location=location,
#         about_complex=about_complex,
#         building_date=building_date,
#         due_date=due_date
#     )

# print("20 жилых комплексов успешно добавлено!")
# 3


from faker import Faker
from apps.accounts.models import User 
from apps.house.models import Property, Location
from django.contrib.gis.geos import Point
from apps.house import choices
fake = Faker()
import random

# # FOR USERS
# image_url = fake.image_url()
# print(image_url)

# for _ in range(100000):
#     name = fake.name()
#     first_name = fake.name()
#     user_email = fake.ascii_email()
#     balance = fake.pyint()
#     date_register  = fake.date_between()
#     code = random.randint(50000, 150000)
#     _avatar = fake.image_url(width=500, height=500)
#     username = fake.unique.user_name()
#     if User.objects.filter(username=username).exists():
#         continue
#     User.objects.create(
#         username=username,
#         name=user_email,
#         is_active=True,
#         date_joined=date_register,
#         code=code,
#         balance=balance,
#         _avatar=_avatar,
#     )
# print("data saved")



lat_min, lat_max = 42.810, 42.950  
lon_min, lon_max = 74.510, 74.640 

for _ in range(10000000):
    user = User.objects.all()
    coordinate_lat = round(random.uniform(lat_min, lat_max), 6)  
    coordinate_lon = round(random.uniform(lon_min, lon_max), 6) 
    type_deal = random.choice(list(dict(choices.TYPE_DEAL).keys())) if 'Sell' else 'Sell'
    type_property = random.choice(list(dict(choices.PROPERTY_TYPE_OPTIONS).keys())) if 'House' else 'House'
    price_for = random.choice(list(dict(choices.PRICE_FOR).keys())) if 'Per meter' else 'Per meter'
    currency = random.choice(list(dict(choices.CURRENCY_TYPE).keys())) if 'USD'  else 'USD' 
    general = random.randint(10, 50)
    description = fake.paragraphs()
    price = fake.pyint(5000, 10000)
    advertiser_type = random.choice(list(dict(choices.ADVERTISER_OPTIONS).keys())) if 'Agent' else 'Agent'
    pictures_properties = fake.image_url()
    # print(coordinate_lon)
    # print(coordinate_lat)
    
    instance = Property.objects.create(
        user=random.choice(user),
        point=Point(coordinate_lon, coordinate_lat),
        type_deal=type_deal,
        type_property=type_property,
        general=general,
        location=Location.objects.first(),
        description=description,
        price=price,
        price_for=price_for,
        currency=currency,
        advertiser_type=advertiser_type,
        active_post=True,
        # pictures_properties={"pictures_properties": [{"pictures": pictures_properties}]}
    )
    instance.save()
    
    # import geocoder

    # g = geocoder.osm([coordinate_lat, coordinate_lon], method='reverse')
    # if g.ok:
    #     print(f"Координаты: {coordinate_lat}, {coordinate_lon} => Место: {g.address}")
    # else:
    #     print(f"Координаты: {coordinate_lat}, {coordinate_lon} не найдены.")