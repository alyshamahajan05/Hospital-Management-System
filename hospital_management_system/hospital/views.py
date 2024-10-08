from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Doctor,Patient,Appointment

def About(request):
    return render(request, 'about.html')

def Home(request):
    return render(request, 'home.html')

def Contact(request):
    return render(request, 'contact.html')

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    
    # Counting the number of doctors, patients, and appointments
    d = Doctor.objects.count()
    p = Patient.objects.count()
    a = Appointment.objects.count()
    
    # Pass these counts to the template
    context = {
        'd': d,
        'p': p,
        'a': a
    }
    
    return render(request, 'index.html', context)

def Login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('dashboard')  # Redirect to the home page after successful login
        else:
            error = "yes"
    d = {'error': error}
    return render(request, 'login.html', d)

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')  # Redirect to 'login' which now matches the URL name
    logout(request)
    return redirect('Home')  # Changed from 'admin_login' to 'login'

def View_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc= Doctor.objects.all()
    d = {'doc': doc}
    return render(request, 'view_doctor.html',d)

def Delete_doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = get_object_or_404(Doctor, id=pid)
    doctor.delete()
    return redirect('view_doctor')

def AddDoctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == "POST":
        n = request.POST['Name']
        m = request.POST['Mobile']
        sp = request.POST['special']
        try:
            Doctor.objects.create(Name=n, Mobile=m, special=sp)
            error = "no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request, 'add_doctor.html', d)

def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    doc= Patient.objects.all()
    d = {'doc': doc}
    return render(request, 'view_patient.html',d)

def Delete_patient(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = get_object_or_404(Patient, id=pid)
    patient.delete()
    return redirect('view_patient')

def Add_Patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == "POST":
        n = request.POST['Name']
        m = request.POST['Mobile']
        g = request.POST['gender']
        a = request.POST['address']
        try:
            Patient.objects.create(Name=n, Mobile=m, gender=g, address=a)
            error = "no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request, 'add_patient.html', d)

def Add_Appointment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    
    if request.method == "POST":
        # Use the ids submitted from the form
        do = request.POST.get('doctor')  # This should be the id
        p = request.POST.get('patient')  # This should be the id
        D = request.POST.get('date')
        t = request.POST.get('time')

        try:
            # Fetch doctor and patient by id
            doctor = Doctor.objects.get(id=do)
            patient = Patient.objects.get(id=p)
            
            # Create the appointment
            Appointment.objects.create(doctor=doctor, patient=patient, date=D, time=t)
            error = "no"
        except Doctor.DoesNotExist:
            error = "Doctor does not exist"
        except Patient.DoesNotExist:
            error = "Patient does not exist"
        except Exception as e:
            error = str(e)
    
    context = {'doctor': doctor1, 'patient': patient1, 'error': error}
    return render(request, 'add_appointment.html', context)


def View_Appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    doc= Appointment.objects.all()
    d = {'doc': doc}
    return render(request, 'view_appointment.html',d)


def Delete_appointment(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = get_object_or_404(Appointment, id=pid)
    patient.delete()
    return redirect('view_appointment')




