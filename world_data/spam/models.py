from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=15)
    # Because some libraries use 2 digit country code
    code_3 = models.CharField(max_length=3)
    code_2 = models.CharField(max_length=3)


class CountryInfo(models.Model):
    country = models.ManyToManyField(Country)
    indicator_code = models.CharField(max_length=50)
    indicator_name = models.CharField(max_length=50)
    indicator_id = models.IntegerField(max_length=2, db_index=True)

    # zip(years, values)? BinaryTextField? wide table?
    years = models.TextField()
    values = models.TextField()
    color_map_values = models.TextField()
