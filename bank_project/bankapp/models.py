from django.db import models

# Create your models here.

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Others'),
]

ACCOUNT_CHOICES = [
    ('S', 'Saving Account'),
    ('C', 'Current Account'),
]

class District(models.Model):
    name=models.CharField(max_length=50, default=True)

    def __str__(self):
        return self.name

class Branch(models.Model):
    district=models.ForeignKey(District, on_delete=models.CASCADE)
    name=models.CharField(max_length=50,default=True)

    def __str__(self):
        return self.name

class MaterialOption(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Form(models.Model):
    name = models.CharField(max_length=100)
    dob=models.DateField(max_length=8)
    age=models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phonenumber=models.CharField(max_length=15)
    email=models.EmailField()
    address=models.CharField(max_length=200)
    district=models.ForeignKey(District,on_delete=models.SET_NULL,blank=True,null=True)
    branch = models.ForeignKey(Branch,on_delete=models.SET_NULL,blank=True,null=True)
    account_type= models. CharField(max_length=1,choices=ACCOUNT_CHOICES)

    def __str__(self):
        return self.name
