from django.shortcuts import render
from django.http import HttpResponse
from .models import*
from .forms import BookingForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            # Get the selected doctor id from the form
            doctor_id = request.POST.get('doc_name', None)

            if doctor_id:
                # Retrieve the Doctor instance using the doctor_id
                doctor_instance = Doctor.objects.get(pk=doctor_id)

                # Set the doc_name field in the form to the Doctor instance
                form.instance.doc_name = doctor_instance

                # Save the form
                form.save()

                return render(request, 'conformation.html')

    form = BookingForm()
    dict_form = {'form': form}
    return render(request, 'booking.html', dict_form)

def doctors(request):
    dict_doc={
        'doc':Doctor.objects.all()
    }
    return render(request, 'doctors.html',dict_doc)

def contact(request):
    return render(request, 'contact.html')
def login(request):
    return render(request, 'login.html')
def logout(request):
    return render(request, 'login.html')

def department(request):
    dict_dept={
        'dept':Department.objects.all()
    }
    return render(request, 'department.html',dict_dept)
def checkadminlogin(request):
    if request.method == "POST":
        name = request.POST["uname"]
        password = request.POST["pwd"]

        # Use Django's built-in authenticate function to check credentials
        user = authenticate(request, username=name, password=password)

        if user is not None:
            if user.is_staff:  # Check if the user is an admin
                login(request, user)
                messages.info(request, "This is the admin TTM page.")
                return render(request, "adminhome.html")
            else:
                messages.info(request, "You do not have admin privileges.")
                return render(request, "loginfail.html")
        else:
            messages.info(request, "Your credentials are not correct.")
            return render(request, "loginfail.html")