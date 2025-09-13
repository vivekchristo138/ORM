from django.db import models
from django.contrib import admin
class cars_DB(models.Model):
    Car_Name=models.CharField(max_length=12)
    Car_Number=models.IntegerField(primary_key=True)
    Company=models.CharField()
    Price=models.FloatField()
    Color=models.CharField()
class cars_DB_Admin(admin.ModelAdmin):
    list_display=["Car_Name","Car_Number","Company","Price","Color"]