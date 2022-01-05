from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from courier.models import DeliveryDetails,DeliveryStatus

@receiver(post_save,sender=DeliveryDetails)
def DeliveryStatusSignal(sender,instance,created,*args,**kwargs):
    """
    package status changes to dispatched until receiver gets the package
    """
    if created:
        DeliveryStatus.objects.create(courier_man=instance.courier_man,details=instance,status='Dispatched')
    else:
        pass

