from django.shortcuts import render,redirect,get_object_or_404
from teffyapp.models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from enum import Enum
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.utils import timezone
from datetime import date, datetime
# Create your views here.

class Messages(Enum):
    SUCCESS = 1
    ERROR = 2
    WARNING = 3
    INFO = 4 

def success_message() -> str:
    return "Success message from success function"

def error_message() -> str:
    return "Error message from error function"

def warning_message() -> str:
    return "Warning message from warning function"

def info_message() -> str:
    return "Info message from info function"

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)  
           
            return redirect("/main/")  
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect("/login/")  
    return render(request, "login.html")


def user_logout(request):
    logout(request)
    return redirect("/login/")

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        email = request.POST.get("email")
        if User.objects.filter(username__iexact=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("/register/")
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("/register/")
        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()
        messages.success(request, "Successfully Registered! Please login.")
        return redirect("/login/")  
    return render(request, "register.html")

def forms(request):
    if request.method == "POST":
       
        name = request.POST.get("name")
        address = request.POST.get("address")
        occupation = request.POST.get("occupation")
        gender = request.POST.get("gender")
        mobile_number = request.POST.get("mobile_number")
        email = request.POST.get("email")
        perfect_body = request.POST.get("perfect_body")
        body_type = request.POST.get("body_type")
        goal = request.POST.get("goal")
        body_you_want = request.POST.get("body_you_want")
        level_of_body_fat = request.POST.get("level_of_body_fat")
        problem_areas = request.POST.get("problem_areas")
        diets = request.POST.get("diets")
        water_you_drink_daily = request.POST.get("water_you_drink_daily")
        eat_or_dividie_foods_or_beverages = request.POST.get("eat_or_dividie_foods_or_beverages")
        event_coming_up = request.POST.get("event_coming_up")
        height = request.POST.get("height")
        current_weight = request.POST.get("current_weight")
        target_weight = request.POST.get("target_weight")
        level_of_fitness = request.POST.get("level_of_fitness")
        status = request.POST.get("status", 'new')  

        print("Form Data:", { 
            "name": name,
            "status": status,
        })

        
        personal_info = PersonalInformation(
            name=name,
            address=address,
            occupation=occupation,
            gender=gender,
            mobile_number=mobile_number,
            email=email,
            perfect_body=perfect_body,
            body_type=body_type,
            goal=goal,
            body_you_want=body_you_want,
            level_of_body_fat=level_of_body_fat,
            problem_areas=problem_areas,
            diets=diets,
            water_you_drink_daily=water_you_drink_daily,
            eat_or_dividie_foods_or_beverages=eat_or_dividie_foods_or_beverages,
            event_coming_up=event_coming_up,
            height=height,
            current_weight=current_weight,
            target_weight=target_weight,
            level_of_fitness=level_of_fitness,
            status=status,  
        )
        personal_info.save()

        return redirect(request.path)

    return render(request, "forms.html")


def main(request):
    member_count = PersonalInformation.objects.count() 
    sales = Sales.objects.count()
    purchase = Purchase.objects.count()
    messages.success(request,"WELCOME")
    return render(request, 'main-page.html', {'member_count': member_count, "sales":sales, "purchase":purchase})

def expense(request):
    return render(request,"expense-page.html")

def follow_up(request):
    return render(request,"follow-up page.html")

def plan(request):
    return render(request,"plan-page.html")

def price(request):
    return render(request,"price-page.html")

def workplan(request):
    return render(request,"workplan.html")

def personal_info_list(request):
    all_data = PersonalInformation.objects.all()
    return render(request, 'new-leads.html', {'all_data': all_data})
    
def getone_lead(request, id):
    obj = PersonalInformation.objects.get(id=id)
    data = obj.gym()

    if obj.id:
        data = obj.gym()
        print("ID is available:", obj.id)
    else:
        print("ID is not available")
        return redirect('error_page')  
    
    if request.method == "POST":
        
        name = request.POST.get("name")
        address = request.POST.get("address")
        occupation = request.POST.get("occupation")
        gender = request.POST.get("gender")
        mobile_number = request.POST.get("mobile_number")
        email = request.POST.get("email")
        perfect_body = request.POST.get("perfect_body")
        body_type = request.POST.get("body_type")
        goal = request.POST.get("goal")
        body_you_want = request.POST.get("body_you_want")
        level_of_body_fat = request.POST.get("level_of_body_fat")
        problem_areas = request.POST.get("problem_areas")
        diets = request.POST.get("diets")
        water_you_drink_daily = request.POST.get("water_you_drink_daily")
        eat_or_dividie_foods_or_beverages = request.POST.get("eat_or_dividie_foods_or_beverages")
        event_coming_up = request.POST.get("event_coming_up")
        height = request.POST.get("height")
        current_weight = request.POST.get("current_weight")
        target_weight = request.POST.get("target_weight")
        level_of_fitness = request.POST.get("level_of_fitness")
        status = request.POST.get("status")

 
        if name:
            obj.name = name
        if address:
            obj.address = address
        if occupation:
            obj.occupation = occupation
        if gender:
            obj.gender = gender
        if mobile_number:
            obj.mobile_number = mobile_number
        if email:
            obj.email = email
        if perfect_body:
            obj.perfect_body = perfect_body
        if body_type:
            obj.body_type = body_type
        if goal:
            obj.goal = goal
        if body_you_want:
            obj.body_you_want = body_you_want
        if level_of_body_fat:
            obj.level_of_body_fat = level_of_body_fat
        if problem_areas:
            obj.problem_areas = problem_areas
        if diets:
            obj.diets = diets
        if water_you_drink_daily:
            obj.water_you_drink_daily = water_you_drink_daily
        if eat_or_dividie_foods_or_beverages:
            obj.eat_or_dividie_foods_or_beverages = eat_or_dividie_foods_or_beverages
        if event_coming_up:
            obj.event_coming_up = event_coming_up
        if height:
            obj.height = height
        if current_weight:
            obj.current_weight = current_weight
        if target_weight:
            obj.target_weight = target_weight
        if level_of_fitness:
            obj.level_of_fitness = level_of_fitness

        # Always update status
        if status:
            obj.status = status

        obj.save()
        messages.success(request, "Data updated successfully")
        return redirect(f'/leads/{obj.id}/') 
    
    return render(request, "one-leads.html", data)


def update_status(request, id):
    if request.method == 'POST':
        lead = PersonalInformation.objects.get(id=id)
        status = request.POST.get('status')
        lead.status = status
        lead.save()

        messages.success(request, f"Status updated to {status} successfully.")

        if status == 'new':
            return redirect('new_leads')
        elif status == 'converted':
            return redirect('converted_leads')
        elif status == 'not_converted':
            return redirect('not_converted_leads')
        elif status == 'pending':
            return redirect('pending_leads')
        elif status == 'follow_up':
            return redirect('follow_up_leads')

    return redirect('new_leads')

def new_leads(request):
    all_data = PersonalInformation.objects.filter(status='new') 
    return render(request, 'new-leads.html', {'all_data': all_data, 'status_title': 'New'})

def converted_leads(request):
    if request.method == "POST":
        lead_id = request.POST.get('lead_id')
        service_id = request.POST.get('services')  

        lead = PersonalInformation.objects.get(id=lead_id)
        selected_service = Service.objects.get(id=service_id)  
        lead.services = selected_service  
        lead.save()

        return redirect('converted_leads')

    all_data = PersonalInformation.objects.filter(status='converted')
    available_services = Service.objects.all()

    return render(request, 'converted_leads.html', {
        'all_data': all_data,
        'status_title': 'Converted',
        'available_services': available_services,
    })


def not_converted_leads(request):
    all_data = PersonalInformation.objects.filter(status='not_converted')
    return render(request, 'not_converted_leads.html', {'all_data': all_data, 'status_title': 'Not Converted'})

def pending_leads(request):
    all_data = PersonalInformation.objects.filter(status='pending')
    return render(request, 'pending_leads.html', {'all_data': all_data, 'status_title': 'Pending'})

def follow_up_leads(request):
    all_data = PersonalInformation.objects.filter(status='follow_up')
    return render(request, 'follow_up_leads.html', {'all_data': all_data, 'status_title': 'Follow Up'})

def delete_lead(request, id):
    lead = PersonalInformation.objects.get(id=id)
    lead.delete()
    messages.success(request, "Lead deleted successfully.")
    return redirect('new_leads') ############

def user_management(request):
    if request.method == "POST":
        profile_user_id = request.POST.get("profile_user_id")
        username = request.POST.get("name")
        password = request.POST.get("password")
        group = request.POST.get("group")

        if not username or not password or not group:
            messages.error(request, "All fields are required.")
            return redirect("/user_management/")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("/user_management/")

      
        if UserProfile.objects.filter(profile_user_id=profile_user_id).exists():
            messages.error(request, "Profile User ID already exists.")
            return redirect("/user_management/")

       
        user = User.objects.create_user(username=username)
        user.set_password(password)

        if group == "admin":
            user.is_superuser = True
        elif group == "staff":
            user.is_staff = True
            user.is_superuser = False

        user.save()

      
        if not profile_user_id:
            user_count = UserProfile.objects.count() + 1
            profile_user_id = f"USER-{user_count}"

       
        UserProfile.objects.create(
            user=user,
            profile_user_id=profile_user_id,
            group=group,
        )

        messages.success(request, "User successfully added.")
        return redirect("/user_management/")

   
    user_count = UserProfile.objects.count() + 1
    profile_user_id = f"USER-{user_count}"
    data = UserProfile.objects.all()

   
    is_admin = request.user.is_superuser
    is_staff = request.user.is_staff

    context = {
        "data": data,
        "profile_user_id": profile_user_id,
        "is_admin": is_admin,
        "is_staff": is_staff,
    }

    return render(request, "user-management.html", context)


def edit_user(request, user_id):
    user_profile = UserProfile.objects.get(profile_user_id = user_id)
    if request.method == 'POST':
        username = request.POST.get('name')
        group = request.POST.get('group')
        password = request.POST.get('password')
        print(user_profile)


        if not username or not group:
            messages.error(request, "Username and Group fields cannot be empty.")
            return redirect('edit_user', user_id=user_id)
        
        user_profile.user.username = username
        user_profile.group = group
        if password:
            user_profile.user.set_password(password)
        user_profile.user.save()
        user_profile.save()

        messages.success(request, "User details successfully updated.")
        return redirect('user_management')

    return render(request, 'edit-user.html', {'user_profile': user_profile})


def delete_user(request, user_id):
    user_profile = UserProfile.objects.get(profile_user_id = user_id)
    user_profile.user.delete()  
    user_profile.delete()       
    
    messages.success(request, "User successfully deleted.")
    return redirect('user_management')


def report_view(request):
    today = timezone.now().date()  

    
    first_day_of_month = date(today.year, today.month, 1)

    
    new_leads_today = PersonalInformation.objects.filter(created_date__date=today, status='new').count()
    converted_leads_today = PersonalInformation.objects.filter(created_date__date=today, status='converted').count()
    not_converted_leads_today = PersonalInformation.objects.filter(created_date__date=today, status='not_converted').count()
    follow_up_leads_today  = PersonalInformation.objects.filter(created_date__date=today, status='follow_up').count()
    pending_leads_today = PersonalInformation.objects.filter(created_date__date=today, status='pending').count()

   
    new_leads_this_month = PersonalInformation.objects.filter(
        created_date__date__gte=first_day_of_month,
        created_date__date__lte=today,
        status='new'
    ).count()

    converted_leads_this_month = PersonalInformation.objects.filter(
        created_date__date__gte=first_day_of_month,
        created_date__date__lte=today,
        status='converted'
    ).count()

    not_converted_leads_this_month = PersonalInformation.objects.filter(
        created_date__date__gte=first_day_of_month,
        created_date__date__lte=today,
        status='not_converted'
    ).count()

    follow_up_leads_this_month = PersonalInformation.objects.filter(
        created_date__date__gte=first_day_of_month,
        created_date__date__lte=today,
        status='not_converted'
    ).count()

    pending_leads_this_month = PersonalInformation.objects.filter(
        created_date__date__gte=first_day_of_month,
        created_date__date__lte=today,
        status='not_converted'
    ).count()


    context = {
        'new_leads_today': new_leads_today,
        'new_leads_this_month': new_leads_this_month,
        'converted_leads_today': converted_leads_today,
        'converted_leads_this_month': converted_leads_this_month,
        'not_converted_leads_today':not_converted_leads_today,
        'not_converted_leads_this_month' : not_converted_leads_this_month,
        'follow_up_leads_today': follow_up_leads_today,
        'follow_up_leads_this_month' : follow_up_leads_this_month,
        'pending_leads_today' : pending_leads_today,
        'pending_leads_this_month' : pending_leads_this_month

    }

    return render(request, 'reports.html', context)


def services(request):
    if request.method == "POST":
        service_name = request.POST.get('service_name')
        prices = request.POST.get("price")
        duration = request.POST.get("duration")

        if service_name:
            Service.objects.create(name=service_name, prices=prices, duration=duration)
            return redirect('services')  

    all_services = Service.objects.all()  
    return render(request, 'manage-services.html', {'services': all_services})


def delete_service(request, service_id):
    service = Service.objects.get(id=service_id)
    service.delete()
    return redirect('services')

def assign_service(request, id):
    if request.method == "POST":
     
        service_id = request.POST.get("service")
       
        service = Service.objects.filter(id=service_id).first()
        lead = PersonalInformation.objects.filter(id=id).first()

        if service and lead:
            lead.services = service
            lead.save()
            messages.success(request, "Service successfully assigned!")
        else:
            messages.error(request, "Invalid service or lead.")

        return redirect('converted_leads')



def overall_services(request):
        client_details = PersonalInformation.objects.filter(status='converted')
        print("Number of clients:", client_details.count())
        for client in client_details:
            print(f"Client: {client.name}, Service: {client.services.name if client.services else 'No Service'}")
        services = Service.objects.all()

        context = {
            "client_details": client_details, 
            "services_taken": services,
        }
        return render(request, "overall-service.html", context)

