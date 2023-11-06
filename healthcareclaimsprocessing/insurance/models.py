from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length = 100)
    policy_number = models.CharField(max_length= 100)

class Provider (models.Model):
    name = models.CharField(max_length= 100)
    speciality = models.CharField(max_length= 100)


class InsuranceClaim(models.Model):
    patient = models.ForeignKey(Patient, on_delete= models.CASCADE)
    Provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    claim_amount = models.DecimalField(max_digits= 10, decimal_places= 2)
    submitted_at = models.DateTimeField(auto_now_add = True)
    is_approved = models.BooleanField(default = False)

