# Ex02 Django ORM Web Application
## Date: 13/09/2025

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py
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

admin.py
from django.contrib import admin
from.models import cars_DB,cars_DB_Admin
admin.site.register(cars_DB,cars_DB_Admin)

```


## OUTPUT
![alt text](<Screenshot (2).png>)


## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
