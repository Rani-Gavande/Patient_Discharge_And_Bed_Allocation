from django.db import models
# Create your models here.
class add_Patient(models.Model):
    Patient_name = models.CharField(max_length=100)
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    ] 
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    Age = models.IntegerField()
    Mobileno =models.IntegerField()
    Email = models.EmailField(max_length=100)
    Address = models.CharField(max_length=150)
    Ward = models.ForeignKey("Ward.addWard", on_delete=models.SET_NULL, null=True)
    bed = models.ForeignKey("Ward.Bed", on_delete=models.SET_NULL, null=True)
    Problem = models.CharField(max_length=150)
    Remarks = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.id} - {self.Patient_name}"
    
class add_Doctor(models.Model):
    Doctor_name = models.CharField(max_length=100)
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    ] 
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    SPE_CHOICES =[
        ("Cardiologist","Cardiologist"),
        ("Dermatologist","Dermatologist"),
        ("Pediatrician","Pediatrician"),
        ("Gynecologist","Gynecologist"),
        ("Orthopedic","Orthopedic"),
        ("Neurologist","Neurologist"),
        ("ENT Specialist","ENT Specialist"),
        ("General Physician","General Physician"),
    ]
    Specialization = models.CharField(max_length=18,choices=SPE_CHOICES)
    Qualification = models.CharField(max_length=100)
    Experience = models.IntegerField(null=True)
    Mobileno =models.IntegerField()
    Email = models.EmailField(max_length=100)
    WARD_CHOICES=[
        ("ICU","ICU"),
        ("General","General"),
        ("Private","Private"),
        ("Emergency","Emergency"),
        ("OT","OT"),  
        ("Maternity","Maternity")
    ]
    Ward = models.CharField(max_length=9, choices=WARD_CHOICES)
    Available_from = models.TimeField(null=True) 
    Available_to = models.TimeField(null=True) 
