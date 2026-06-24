from django.db import models

# Create your models here.
class addWard(models.Model):
    wardName = models.CharField(max_length=100)
    wardNumber = models.IntegerField()
    floor=models.CharField(max_length=100)
    capacity=models.IntegerField()
   
    WARD_CHOICES=[
        ("ICU","ICU"),
        ("General","General"),
        ("Private","Private"),
        ("Emergency","Emergency"),
        ("OT","OT"),  
        ("Maternity","Maternity")
    ]
    department = models.CharField(max_length=9, choices=WARD_CHOICES)
    description = models.CharField(max_length=150)
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('maintenance', 'Under Maintenance'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    
    def __str__(self):
        return self.wardName
    
class Bed(models.Model):
    ward = models.ForeignKey(addWard, on_delete=models.CASCADE)
    bed_number = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.ward.wardName} - Bed {self.bed_number}"