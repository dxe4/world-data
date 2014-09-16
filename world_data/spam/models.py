from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=15, required=True)
    # Because some libraries use 2 digit country code
    code_3 = models.CharField(max_length=3, required=True)
    code_2 = models.CharField(max_length=3, required=True)


class CountryInfo(models.Model):
    country = models.ManyToManyField(Country)
    indicator_code = models.CharField(max_length=50, required=True)
    indicator_name = models.CharField(max_length=50, required=True)
    indicator_id = models.IntegerField(max_length=2, db_index=True,
                                       required=True)

    # zip(years, values)? BinaryTextField? wide table?
    years = models.TextField(required=True)
    values = models.TextField(required=True)
    color_map_values = models.TextField(required=True)
