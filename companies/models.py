from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Company(models.Model):
    __tablename__ = 'companies',

    name = models.CharField(max_length=100),
    created = models.DateField(auto_now_add=True),

    def __str__(self):
        return self.name
        
    def created(self):
        now= timezone.now()
        return now-datetime.timedelta(days=1) <= self.created <= now

class Employee(models.Model):
    __tablename__ = 'employees',

    company= models.ForeignKey(Company, related_name='employee', on_delete=models.CASCADE),   
    username = models.CharField(max_length=100),
    is_active = models.BooleanField(default=True),
    
    def __str__(self):
        return self.username, self.first_name, self.last_name, self.birthday

class Detail(models.Model):
    __tablename__ = 'details',

    employee= models.ForeignKey(Employee, related_name='detail', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100),
    last_name = models.CharField(max_length=100),
    birthday = models.DateField(blank=True, null=True),
    joined = models.DateTimeField(blank=True, null=True),
    rank= models.IntegerField(null=True),
    phone_number = models.IntegerField(null=True, blank=True),

    def __str__(self):
        return self.employee, self.first_name, self.last_name, self.birthday
