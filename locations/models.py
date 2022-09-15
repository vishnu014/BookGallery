from django.db import models

# Create your models here.

class Districts(models.Model):
    district_name=models.CharField(max_length=200,unique=True)
    population=models.PositiveIntegerField()
    first_dose_rate=models.PositiveIntegerField()
    second_dose_rate=models.PositiveIntegerField()

    def __str__(self):
        return self.district_name

# district=Districts(district_name="tvm",population=120000,first_dose_rate=70,second_dose_rate=40)
# district.save()

# districts=Districts.object.all()
# from django.db.models import Avg,Sum,Max,Min
# population_max=Districts.objects.all().aggregate(max("population"))
