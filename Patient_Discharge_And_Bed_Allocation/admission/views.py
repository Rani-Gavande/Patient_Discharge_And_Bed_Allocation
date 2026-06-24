from django.shortcuts import render,redirect
from .models import add_Patient,add_Doctor
from Ward.models import addWard
def index(request):
    wards = addWard.objects.all()   # database se wards lao

    context = {
        "wards": wards
    }
    return render(request, 'index.html',context)

def add_doctor(request):
     if request.method == "POST":
        Doctor_name = request.POST.get("Doctor_name")
        Gender =request.POST.get("Gender")
        Specialization = request.POST.get("Specialization") 
        Qualification = request.POST.get("Qualification")
        Experience = request.POST.get("Experience")
        Ward=request.POST.get("Ward")
        Mobileno =request.POST.get('Mobileno')
        Email=request.POST.get("Email")
        Available_from = request.POST.get('Available_from')
        Available_to =request.POST.get('Available_to')
        
        add_Doctor.objects.create(
            Doctor_name=Doctor_name,
            Gender=Gender,
            Specialization=Specialization,
            Qualification=Qualification,
            Experience=Experience,
            Ward=Ward,
            Mobileno=Mobileno,
            Email=Email,
            Available_from=Available_from,
            Available_to=Available_to,
        )
        return redirect('/') 
     return render(request,'admission/index.html')

def add_patient(request):
    if request.method == "POST":
        Patient_name = request.POST.get("Patient_name")
        Gender =request.POST.get("Gender")
        Age=request.POST.get("Age")
        Ward_id = request.POST.get("Ward")
        ward = addWard.objects.get(id=Ward_id)
        Mobileno =request.POST.get('Mobileno')
        Email=request.POST.get("Email")
        Address=request.POST.get("Address")
        Problem=request.POST.get("Problem")
        Remarks=request.POST.get("Remarks")
        add_Patient.objects.create(
            Patient_name=Patient_name,
            Gender=Gender,
            Age=Age,
            Address=Address,
            Mobileno=Mobileno,
            Email=Email,
            Ward=ward,
            Problem=Problem,
            Remarks=Remarks
        )
        return redirect('/') 
    return render(request,'admission/index.html')

def add_ward(request):
    return render(request,'add_ward.html')

