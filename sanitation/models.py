from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings


class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    phone_number = models.CharField(default=None,max_length=10)
    id_number =models.CharField(max_length=10,default=None,primary_key=True)


import datetime




class Payment(models.Model):
    name = models.CharField(max_length = 65, blank=True)
    account = models.CharField(max_length = 65, blank=True)
    phone_Number= models.CharField(max_length=15)
    amount = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    conversation_id = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.name

    def save_payment(self):
        self.save() 

    @classmethod
    def search_by_phone_Number(cls,search_term):
        payment = cls.objects.filter(phone_Number__icontains=search_term)
        return payment  


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
# M-pesa Payment models
class MpesaCalls(BaseModel):
    ip_address = models.TextField()
    caller = models.TextField()
    merchant_id = models.TextField(null=False,default="")
    checkout_request_id=models.TextField(null=False,default="")
    conversation_id = models.TextField()
    content = models.TextField()
    class Meta:
        verbose_name = 'Mpesa Call'
        verbose_name_plural = 'Mpesa Calls'

class MpesaCallBacks(BaseModel):
    ip_address = models.TextField()
    caller = models.TextField() 
    merchant_id = models.TextField(null=False,default="")
    checkout_request_id=models.TextField(null=False,default="")
    conversation_id = models.TextField()
    content = models.TextField()
    class Meta:
        verbose_name = 'Mpesa Call Back'
        verbose_name_plural = 'Mpesa Call Backs'

class MpesaPayment(BaseModel):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    type = models.TextField()
    reference = models.TextField()
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.TextField()
    organization_balance = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        verbose_name = 'Mpesa Payment'
        verbose_name_plural = 'Mpesa Payments'
    def __str__(self):
        return self.first_name        

class Toilet(models.Model):
    toilet_tag= models.TextField(max_length=30, null=False, default="")
    user_id_number = models.ForeignKey(Profile,on_delete=models.CASCADE, null=False)
    location=models.CharField(max_length = 65, blank=True)


    def save_toilet(self):
        self.save()

    def __str__(self):

        
        return self.toilet_tag    






class Bills(models.Model):

    amount=models.IntegerField(blank=True)
    phone_number=models.TextField(default=0)
    reference=models.TextField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    conversation_id = models.CharField(max_length=100, null=True)




    @classmethod
    def search_by_phone_number(cls,search_term):
        bills = cls.objects.filter(phone_number__icontains=search_term)
        return bills   

    def save_bills(self):


        self.save()
 

        self.save()

    @classmethod
    def search_by_phone_number(cls,search_term):
        bills = cls.objects.filter(phone_number__icontains=search_term)
        return bills   

##Authenticatio/
