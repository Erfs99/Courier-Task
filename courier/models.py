from django.db import models
from rest_framework.exceptions import bad_request


class DeliveryDetails(models.Model):
    
    TYPE = [
        ('perishable', 'Perishable'),
        ('fragile', 'Fragile'),
        ('document', 'Document'),
        ('others', 'Others'),
    ]
    courier_man= models.ForeignKey('CourierMan', on_delete=models.CASCADE)
    receiver= models.ForeignKey('Receiver', on_delete=models.CASCADE)
    package_name= models.CharField(max_length=60)
    price= models.DecimalField(max_digits=6, decimal_places=2)
    package_type= models.CharField(max_length=20,choices=TYPE)
    package_weight= models.IntegerField()
    from_address= models.CharField(max_length=150)
    date_booked= models.DateTimeField(auto_now_add=True)
    date= models.DateField()

    def __str__(self):
        return str(self.courier_man) + self.package_name



class DeliveryStatus(models.Model):

    STATUS=[
        ('Delivered','Delivered'),
        ('Dispatched','Dispatched'),
        ('Processing','Processing')
    ]
    courier_man= models.ForeignKey('CourierMan', on_delete=models.CASCADE)
    details= models.OneToOneField(DeliveryDetails,on_delete=models.CASCADE)
    # courier_location=
    remarks= models.TextField(blank=True,null=True)
    status= models.CharField(max_length=20,choices=STATUS)
    


    def save(self,*args,**kwargs):
        """
        overriding save method to check if package has been delivered or not 
        and if delivered the price will be added to salary
        """
        if self.status == 'Delivered':
            try:
                courier=CourierMan.objects.get(name=self.courier_man.name)
                courier.salary += self.details.price 
                courier.reduction_salary = 0     
                courier.save()
            except:
                pass
        super(DeliveryStatus,self).save(*args,**kwargs)

    def __str__(self):
        return str(self.details)



class CourierMan(models.Model):

    name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    mobile= models.CharField(max_length=30)
    national_id= models.CharField(max_length=40)
    salary= models.DecimalField(max_digits=6, decimal_places=2, blank=True,null=True ,default=0)
    additional_salary= models.DecimalField(max_digits=6, decimal_places=2, default=0,blank=True,null=True)
    reduction_salary= models.DecimalField(max_digits=6, decimal_places=2 ,default =0,blank=True,null=True)

    def __str__(self):
        return self.name + self.last_name



class Address(models.Model):

    country= models.CharField(max_length=50)
    city= models.CharField(max_length=50)
    street= models.CharField(max_length=50)
    postcode= models.CharField(max_length=45)
    additional_info= models.TextField()

    def __str__(self):
        return self.postcode


class Receiver(models.Model):
    name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    mobile= models.CharField(max_length=30)
    address= models.OneToOneField(Address,on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class DailySalary(models.Model):
    courier_man= models.ForeignKey(CourierMan, on_delete=models.CASCADE)
    date= models.DateField()
    salary= models.DecimalField(max_digits=6, decimal_places=2, blank=True,null=True ,default=0)

    class Meta:
        unique_together=('date','courier_man')

    def __str__(self):
        return str(self.courier_man)


class WeeklySalary(models.Model):
    courier_man= models.ForeignKey(CourierMan, on_delete=models.CASCADE)
    from_date= models.DateField()
    to_date= models.DateField()
    salary= models.DecimalField(max_digits=6, decimal_places=2, blank=True,null=True ,default=0)

    def __str__(self):
        return str(self.courier_man)
