from django.db import models

# Create your models here.
class Specialty(models.Model):
    name=models.CharField(max_length=128)
    code=models.CharField(max_length=128)
    start_date=models.DateField()
    is_active=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
    
class Teacher(models.Model):
    first_name=models.CharField(max_length=56)
    last_name=models.CharField(max_length=56)
    degree=models.CharField(max_length=56)
    teaches_in=models.ForeignKey(Specialty, on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name
    
