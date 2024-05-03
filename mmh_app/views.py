from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *

# Create your views here.

def home(request):
    key = request.session.get('session_key')
    if key:
        try:
            user = HomeOwner.objects.get(phone=key)
        except:
            user = Manager.objects.get(phone=key)
        return render(request, 'home.html', {'user':user})
    else:
        return render(request, 'home.html')



def owner_login(request):
    if request.method == "POST":
        phone = request.POST['phone']
        password  = request.POST['password']
        obj = HomeOwner.objects.filter(phone=phone, password=password)
        if obj:
            request.session['session_key'] = phone
            messages.success(request, 'Logged In')
            return redirect('home')
        else:
            messages.error(request, 'Wrong Credentials')
            return render(request, 'owner_login.html')
    else:
        return render(request, 'owner_login.html')
    


def manager_login(request):
    if request.method == "POST":
        phone = request.POST['phone']
        password  = request.POST['password']
        obj = Manager.objects.filter(phone=phone, password=password)
        if obj:
            request.session['session_key'] = phone
            messages.success(request, 'Logged In')
            return redirect('home')
        else:
            messages.error(request, 'Wrong Credentials')
            return render(request, 'manager_login.html')
    else:
        return render(request, 'manager_login.html')
    

def owner_register(request):
    if request.method == "POST":
        phone = request.POST['phone']
        password  = request.POST['password']
        name = request.POST['name']
        email  = request.POST['email']

        obj = HomeOwner()
        obj.name = name
        obj.phone = phone
        obj.email = email
        obj.password = password
        obj.save()
        return redirect('owner_login')
    else:
        return render(request, 'owner_register.html')
    

def logout(request):
    request.session.flush()
    return redirect('home')




def create_service_request(request):
    key = request.session.get('session_key')
    if key:
        try:
            user = HomeOwner.objects.get(phone=key)
        except:
            user = Manager.objects.get(phone=key)
    architects = Architect.objects.all()
    contractors = Contractor.objects.all()
    suppliers = Supplier.objects.all()
    
    if request.method == 'POST':
        homeowner_phone = request.session.get('session_key') 
        homeowner = HomeOwner.objects.get(phone=homeowner_phone) 
        architech_id = request.POST.get('architech')
        contractor_id = request.POST.get('contractor')
        supplier_id = request.POST.get('supplier')
        service_type = request.POST.get('service_type')
        
        service_request = ServiceRequest.objects.create(
            homeowner=homeowner,
            architech_id=architech_id,
            contractor_id=contractor_id,
            supplier_id=supplier_id,
            service_type=service_type,
            status='Pending' 
        )
        messages.success(request, "Service Reuqested")
        return redirect('response') 
    
    return render(request, 'create_service_request.html', {
        'architects': architects,
        'contractors': contractors,
        'suppliers': suppliers,
        'user':user
    })




def service_requests(request):
    key = request.session.get('session_key')
    if key:
        try:
            user = HomeOwner.objects.get(phone=key)
        except:
            user = Manager.objects.get(phone=key)

    requests = ServiceRequest.objects.all()

    if request.method == 'POST':
        request_id = request.POST.get('request_id')
        selected_request = ServiceRequest.objects.get(id=request_id)

        timeline = request.POST.get('timeline')
        budget = request.POST.get('budget')
        status = request.POST.get('status')
        progress = request.POST.get('progress')

        project_management_entry, created = ProjectManagement.objects.get_or_create(
            projectID=selected_request.id,
            defaults={
                'homeowner': selected_request.homeowner,
                'architech': selected_request.architech,
                'contractor': selected_request.contractor,
                'supplier': selected_request.supplier,
                'timeline': timeline,
                'budget': budget,
                'progress': progress 
            }
        )

        project_management_entry.architech = selected_request.architech
        project_management_entry.contractor = selected_request.contractor
        project_management_entry.supplier = selected_request.supplier
        project_management_entry.timeline = timeline
        project_management_entry.budget = budget
        project_management_entry.progress = progress
        project_management_entry.save()

        selected_request.status = status
        selected_request.save()

        return redirect('service_requests') 

    return render(request, 'service_requests.html', {'requests': requests, 'user':user})



def response(request):
    key = request.session.get('session_key')
    user = None
    if key:
        try:
            user = HomeOwner.objects.get(phone=key)
        except HomeOwner.DoesNotExist:
            try:
                user = Manager.objects.get(phone=key)
            except Manager.DoesNotExist:
                pass

    if user:
        requests = ServiceRequest.objects.filter(homeowner=user)
        project_managements = []
        for req in requests:
            try:
                project_management = ProjectManagement.objects.get(projectID=req.id)
                project_managements.append(project_management)
            except ProjectManagement.DoesNotExist:
                project_managements.append(None)

        zipped_data = zip(requests, project_managements)
        return render(request, 'response.html', {'zipped_data': zipped_data, 'user': user})
    else:
        return render(request, 'response.html', {'user': None})
    


def management(request):
    key = request.session.get('session_key')
    user = None
    if key:
        try:
            user = HomeOwner.objects.get(phone=key)
        except HomeOwner.DoesNotExist:
            try:
                user = Manager.objects.get(phone=key)
            except Manager.DoesNotExist:
                pass
    cont = Contractor.objects.all()
    arc = Architect.objects.all()
    sup = Supplier.objects.all()
    context = {
        'c':cont,
        'a':arc,
        's':sup,
        'user':user,
    }
    return render(request, 'management.html', context)


def feedback(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        remark = request.POST['remark']
        obj = Feedback()
        obj.name = name
        obj.email = email
        obj.remark = remark
        obj.save()
        messages.success(request, 'Feedback Recorded')
        return redirect('home')
    else:
        return redirect('home')
    

def feedbacks(request):
    key = request.session.get('session_key')
    user = None
    if key:
        try:
            user = HomeOwner.objects.get(phone=key)
        except HomeOwner.DoesNotExist:
            try:
                user = Manager.objects.get(phone=key)
            except Manager.DoesNotExist:
                pass
    obj = Feedback.objects.all()
    return render(request, 'feedbacks.html', {'f':obj, 'user':user})




def design(request, phone):
    arobj = Architect.objects.get(phone=phone)
    obj = Design.objects.filter(architect = arobj)
    return render(request, 'designs.html', {'obj':obj})


def project(request, phone):
    ctobj = Contractor.objects.get(phone=phone)
    obj = Projects.objects.filter(contractor = ctobj)
    return render(request, 'projects.html', {'obj':obj})


def catalogue(request, phone):
    ctobj = Supplier.objects.get(phone=phone)
    obj = Catalogue.objects.filter(supplier = ctobj)
    return render(request, 'catalogue.html', {'obj':obj})