from django.shortcuts import render,redirect,get_object_or_404

from .models import addWard
def index(request):
    wards = addWard.objects.all()   # database se sab wards lao

    context = {
        "wards": wards
    }
    print("WARDS:", wards)
    return render(request, "index.html",context)
# Create your views here.
def add_Ward(request):
    if request.method == "POST":
        wardName = request.POST.get("wardName")
        wardNumber =request.POST.get("wardNumber")
        floor = request.POST.get("floor")
        capacity = request.POST.get("capacity")
        description=request.POST.get("description")
        status=request.POST.get("status")
        department = request.POST.get("department")

        addWard.objects.create(
            wardName=wardName,
            wardNumber=wardNumber,
            floor=floor,
            capacity=capacity,
            description=description,
            status=status,
            department=department
        )
        return redirect('/') 
    return render(request,'Ward/add_ward.html')


def ward_beds(request, id):
    ward = get_object_or_404(addWard, id=id)

    beds = range(1, int(ward.capacity) + 1)

    context = {
        "ward": ward,
        "beds": beds
    }

    return render(request, "Ward/Bed.html", context)