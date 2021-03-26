from django.db import models

# Create your models here.

class IdentifierTable(models.Model):
    reqid = models.CharField(max_length=10,unique=True)
    

    def __str__(self):
        return self.reqid


class InquiryTable(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254, unique=True)
    ReqId = models.ForeignKey(IdentifierTable,on_delete=models.CASCADE)
    CountryCode = models.IntegerField(max_length=10)
    mobileNo = models.IntegerField(max_length=10)
    message = models.CharField(max_length=512)
    date = models.DateField()

    def __str__(self):
        return self.email
    
   


