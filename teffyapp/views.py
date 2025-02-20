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
from django.db.models import Sum, F
from django.utils.timezone import now  
from django.utils.timezone import localtime
from datetime import datetime , timedelta
from django.http import HttpResponseRedirect, HttpResponse, Http404
from decimal import Decimal
import calendar
from openpyxl import Workbook
from openpyxl.styles import Alignment
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


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
            # messages.success(request, "WELCOME TO THE PAGE")
           
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


def add_leads(request):
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

    return render(request, "adding-leads.html")


def main(request):
    # Get today's date
    today = timezone.now().date()

    pending_members = AddMember.objects.annotate(
        pending_amount=F('total_amount') - F('current_installment_amount')
    ).filter(pending_amount__gt=0)

    # Today's enrollments
    today_enrollments = PersonalInformation.objects.filter(
        status='converted', 
        assigned_date__year=today.year,
        assigned_date__month=today.month,
        assigned_date__day=today.day
    ).count()

    today_add_members_count = AddMember.objects.filter(
        enrollment_date__year=today.year,
        enrollment_date__month=today.month,
        enrollment_date__day=today.day
    ).count()

    daily_enrollments = today_enrollments + today_add_members_count

    # Lead counts
    member_count = PersonalInformation.objects.filter(status='converted').count()
    all_member_count = PersonalInformation.objects.count() + AddMember.objects.count()
    not_converted_count = PersonalInformation.objects.filter(status='not_converted').count()
    pending_leads_count = PersonalInformation.objects.filter(status="pending").count()
    new_leads_count = PersonalInformation.objects.filter(status="new").count()
    total_members = AddMember.objects.count()

    # Other counts
    staffs_count = UserProfile.objects.all().count()
    stocks_count = Stock.objects.all().count()
    returns_count = Returns.objects.all().count()

    # Sales count
    sales = Sales.objects.filter(sale_date__year=today.year, sale_date__month=today.month).count()
    today_sales = Sales.objects.filter(
        sale_date__year=today.year,
        sale_date__month=today.month,
        sale_date__day=today.day
    ).count()

    # Purchase count
    purchase = Purchase.objects.filter(purchase_date__year=today.year, purchase_date__month=today.month).count()
    today_purchase = Purchase.objects.filter(
        purchase_date__year=today.year,
        purchase_date__month=today.month,
        purchase_date__day=today.day
    ).count()

    # Follow-up leads
    follow_up = PersonalInformation.objects.filter(status='follow_up').count()
    today_follow_up = PersonalInformation.objects.filter(
        status="follow_up", 
        assigned_date__year=today.year,
        assigned_date__month=today.month,
        assigned_date__day=today.day
    ).count()

    # Monthly enrollments
    converted_count = PersonalInformation.objects.filter(
        status='converted', 
        assigned_date__year=today.year, 
        assigned_date__month=today.month
    ).count()

    enrolled_count = AddMember.objects.filter(
        enrollment_date__year=today.year, 
        enrollment_date__month=today.month
    ).count()
    
    total_enrollments = converted_count + enrolled_count

    # Renewals
    today_renewals = Renew.objects.filter(
        renew_date__year=today.year,
        renew_date__month=today.month,
        renew_date__day=today.day
    ).count()

    renewals = Renew.objects.filter(
        renew_date__year=today.year,
        renew_date__month=today.month
    ).count()

    # Expiry Dates
    expiry_date = Renew.objects.filter(
        expiry_date__year=today.year,
        expiry_date__month=today.month
    ).count()

    today_expiry_date = Renew.objects.filter(
        expiry_date__year=today.year,
        expiry_date__month=today.month,
        expiry_date__day=today.day
    ).count()

    # Revenue Calculation (Sum of Payment Amounts)
    total_revenue = Payments.objects.aggregate(total=Sum('amount_paid'))['total'] or 0
    today_revenue = Payments.objects.filter(date_paid__date=today).aggregate(total=Sum('amount_paid'))['total'] or 0

    # Total expense calculation
    total_expense = Expense.objects.aggregate(total=Sum(F('price') * F('quantity')))['total'] or 0
    today_expense = Expense.objects.filter(date_spent=today).aggregate(total=Sum(F('price') * F('quantity')))['total'] or 0

    # Total profit calculation
    total_profit = total_revenue - total_expense
    today_profit = today_revenue - today_expense

    # Overdue follow-ups
    overdue_follow_ups = PersonalInformation.objects.filter(
        follow_up_date__lte=today, status="follow_up"
    )

    # **Pass everything as context**
    context = {
        "member_count": member_count,
        "sales": sales,
        "purchase": purchase,
        "follow_up": follow_up,
        "all_member_count": all_member_count,
        "total_enrollments": total_enrollments,
        "renewals": renewals,
        "daily_enrollments": daily_enrollments,
        "today_renewals": today_renewals,
        "today_sales": today_sales,
        "today_purchase": today_purchase,
        "today_follow_up": today_follow_up,
        "expiry_date": expiry_date,
        "today_expiry_date": today_expiry_date,
        # "today_revenue": today_revenue,
        "not_converted_count": not_converted_count,
        "pending_leads_count": pending_leads_count,
        "new_leads_count": new_leads_count,
        "staffs_count": staffs_count,
        "stocks_count": stocks_count,
        "returns_count": returns_count,
        "overdue_follow_up_count": overdue_follow_ups.count(),
        "overdue_follow_ups": overdue_follow_ups,
        # 'today_profit':today_profit,
        # 'today_expense':today_expense,
        'total_members':total_members,
        "pending_members": pending_members,  # Pass to the dashboard
        "pending_count": pending_members.count(),

        "total_revenue": total_revenue,
        "today_revenue": today_revenue,
        "total_expense": total_expense,
        "today_expense": today_expense,
        "total_profit": total_profit,
        "today_profit": today_profit,
    }

    # Success message
    messages.success(request, "WELCOME TO TEFFY FITNESS")

    # Render the response
    return render(request, 'main-page.html', context)


def expense(request):
    return render(request,"expense-page.html")

def follow_up(request):
    return render(request,"follow-up page.html")

def plan(request):
    if request.method == "POST":
        plan_name = request.POST.get('plan_name')
        price = request.POST.get('price')
        duration = request.POST.get('duration')
        # batch = request.POST.get('batch')

        if plan_name and price and duration:
            Plan.objects.create(plan_name=plan_name, price=price, duration=duration,)
            return redirect('plan')  
        
    all_plans = Plan.objects.all()
    return render(request, "plan-page.html", {'all_plans': all_plans})

def edit_plan(request, plan_id):
    obj = Plan.objects.get(id=plan_id)

    if request.method == "POST":
        plan_name = request.POST.get('plan_name')
        price = request.POST.get('price')
        duration = request.POST.get('duration')
        batch = request.POST.get('batch')

        if plan_name:
            obj.plan_name = plan_name
        if price:
            obj.price = price
        if duration:
            obj.duration = duration
        if batch:
            obj.batch = batch

        obj.save()
        return redirect(f'/plan/{obj.id}/')  

    data = obj.plan()
    return render(request, "edit-plan.html", data)

def assign_plan(request, id):
    if request.method == "POST":
        plan_id = request.POST.get("plan")  # Ensure correct field name
        print(f"Received Plan ID: {plan_id}")  # Debugging
        
        plan = Plan.objects.filter(id=plan_id).first()
        lead = PersonalInformation.objects.filter(id=id).first()
        print(f"Lead: {lead}, Plan: {plan}")  # Debugging

        if plan and lead:
            print(f"Assigning Plan {plan.plan_name} to Lead {lead.id}")  # Debugging
            lead.plan_leads = plan
            lead.save()
            messages.success(request, "Plan successfully assigned!")
        else:
            messages.error(request, "Invalid Plan or Lead.")

        return redirect('converted_leads')  # Ensure the page refreshes


# def price(request):
#     return render(request,"price-page.html")

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

def update_followup_date(request, id):
    """Update follow-up date when changed in the dropdown"""
    if request.method == "POST":
        lead = get_object_or_404(PersonalInformation, id=id)
        follow_up_date = request.POST.get("follow_up_date")

        if follow_up_date:
            lead.follow_up_date = follow_up_date
            lead.save()
            messages.success(request, f"Follow-up date updated for {lead.name}")

    return redirect("follow_up_leads")  # Redirect back to leads page


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
    # add_members = AddMember.objects.all()
    return render(request, 'new-leads.html', {'all_data': all_data, 'status_title': 'New',})

def converted_leads(request):
    if request.method == "POST":
        lead_id = request.POST.get('lead_id')
        service_id = request.POST.get('services')
        plan_id = request.POST.get('plan_leads')

        lead = PersonalInformation.objects.get(id=lead_id)
        selected_service = Service.objects.get(id=service_id)
        selected_plan = Plan.objects.get(id=plan_id)

        # Assign service and plan
        lead.services = selected_service
        lead.plan_leads = selected_plan
        lead.status = "converted"  # Ensure status is updated

        lead.save()

        # Ensure no automatic AddMember creation
        if AddMember.objects.filter(email=lead.email).exists():
            print(f"Lead {lead.name} is already a member, skipping AddMember creation.")

        return redirect('converted_leads')

    all_data = PersonalInformation.objects.filter(status='converted')
    available_services = Service.objects.all()
    plans = Plan.objects.all()

    return render(request, 'converted_leads.html', {
        'all_data': all_data,
        'status_title': 'Converted',
        'available_services': available_services,
        'plans': plans,
    })

def not_converted_leads(request):
    if request.method == "POST":
        lead_id = request.POST.get("lead_id")  # Get the lead ID from the form
        lead = get_object_or_404(PersonalInformation, id=lead_id)

        # Update the status
        lead.status = request.POST.get("status")

        # If the status is 'pending', store the reason; otherwise, clear it
        if lead.status == "pending":
            lead.reason = request.POST.get("reason", "")
        else:
            lead.reason = ""

        lead.save()
        return redirect("pending_leads")  # Refresh the page after updating
    all_data = PersonalInformation.objects.filter(status='not_converted')
    return render(request, 'not_converted_leads.html', {'all_data': all_data, 'status_title': 'Not Converted'})

def pending_leads(request):
    if request.method == "POST":
        lead_id = request.POST.get("lead_id")  # Get the lead ID from the form
        lead = get_object_or_404(PersonalInformation, id=lead_id)

        # Update the status
        lead.status = request.POST.get("status")

        # If the status is 'pending', store the reason; otherwise, clear it
        if lead.status == "pending":
            lead.reason = request.POST.get("reason", "")
        else:
            lead.reason = ""

        lead.save()
        return redirect("pending_leads")  # Refresh the page after updating

    # Get all leads with 'pending' status
    all_data = PersonalInformation.objects.filter(status="pending")
    return render(request, "pending_leads.html", {"all_data": all_data, "status_title": "Pending"})

def follow_up_leads(request):
    all_data = PersonalInformation.objects.filter(status='follow_up')
    return render(request, 'follow_up_leads.html', {'all_data': all_data, 'status_title': 'Follow Up'})

def delete_lead(request, id):
    lead = PersonalInformation.objects.get(id=id)
    lead.delete()
    messages.success(request, "Lead deleted successfully.")
    return redirect('converted_leads') ############

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
            profile_user_id = f"TFS-{user_count}"

       
        UserProfile.objects.create(
            user=user,
            profile_user_id=profile_user_id,
            group=group,
        )

        messages.success(request, "User successfully added.")
        return redirect("/user_management/")

   
    user_count = UserProfile.objects.count() + 1
    profile_user_id = f"TFS-{user_count}"
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

def view_all_staffs(request):
    admins = UserProfile.objects.filter(group="admin")
    staff = UserProfile.objects.filter(group="staff")

    context = {
        "admins": admins,
        "staff": staff,
    }
    return render(request, "view-all-staffs.html", context)

def services(request):
    if request.method == "POST":
        service_name = request.POST.get('service_name')
        prices = request.POST.get("price")
        duration = request.POST.get("duration")
        group = request.POST.get("group")
        sessions = request.POST.get("sessions")


        if service_name:
            Service.objects.create(name=service_name, prices=prices, duration=duration, group=group, sessions=sessions)
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


def payment(request, client_id):
    client = get_object_or_404(PersonalInformation, id=client_id)
    
    # Get the service price if it exists
    service_price = client.services.prices if client.services else 0  

    # Get the membership price if a membership plan exists
    membership_price = client.plan_leads.price if client.plan_leads else 0  

    # Calculate the total price (service price + membership price)
    total_price = service_price + membership_price

    # Get the total amount already paid by the client
    total_amount_paid = Payments.objects.filter(payments=client).aggregate(Sum('amount_paid'))['amount_paid__sum'] or 0

    # Calculate pending amount
    pending_amount = total_price - total_amount_paid

    if request.method == 'POST':
        amount_paid = float(request.POST.get('amount_paid', 0))
        payment_mode = request.POST.get('payment_mode')

        if amount_paid > 0 and payment_mode:
            new_pending_amount = pending_amount - amount_paid  

            # Save payment details
            Payments.objects.create(
                payments=client,
                name=client,
                amount_paid=amount_paid,
                pending_amount=new_pending_amount,
                payment_mode=payment_mode,
                date_paid=now(),  
            )
            messages.success(request, "Payment submitted successfully!")
            return redirect('payment_page', client_id=client_id)
        
    # Get payment history
    payment_history = Payments.objects.filter(payments=client)

    return render(request, 'payment.html', {
        'client': client,
        'service_price': service_price,
        'membership_price': membership_price,  # Pass membership price to template
        'total_price': total_price,  # Total price (Service + Membership)
        'total_amount_paid': total_amount_paid,
        'pending_amount': pending_amount,
        'payment_history': payment_history,
    })

def expenses(request):
    current_year = datetime.now().year
    current_month = datetime.now().month

    years = list(range(current_year - 5, current_year + 1))

    months = {
        1: "January", 2: "February", 3: "March", 4: "April",
        5: "May", 6: "June", 7: "July", 8: "August",
        9: "September", 10: "October", 11: "November", 12: "December"
    }

    selected_year = int(request.GET.get("year", current_year))
    selected_month = int(request.GET.get("month", current_month))

    expenses = Expense.objects.filter(date_spent__year=selected_year, date_spent__month=selected_month)
    total_monthly_expenses = expenses.aggregate(Sum("price"))["price__sum"] or 0

    return render(request, "new-expense.html", {
        "expenses": expenses,
        "total_monthly_expenses": total_monthly_expenses,
        "years": years,
        "months": months,
        "selected_year": selected_year,
        "selected_month": selected_month,
    })


def add_expense(request):
    if request.method == 'POST':
        expense_name = request.POST.get('expense_name')
        price = request.POST.get('price')
        date_spent = request.POST.get('date_spent')
        quantity = request.POST.get('quantity')

        expense = Expense(expense_name=expense_name, price=price, date_spent=date_spent, quantity=quantity)
        expense.save()

        return redirect('expenses')  # Redirect to the expenses page after adding
    return render(request, 'your_template.html')  # Use your actual template name


def delete_expense(request, expense_id):
    expense = Expense.objects.get(id=expense_id)
    expense.delete()
    return redirect('expenses')

def view_expense(request,expense_id):
    obj = Expense.objects.get(id=expense_id)
    data = obj.expense()

    if request.method == "POST":
        expense_name = request.POST.get('expense_name')
        price = request.POST.get('price')
        date_spent = request.POST.get('date_spent')

        if expense_name:
            obj.expense_name = expense_name

        if price:
            obj.price = price

        if date_spent:
            obj.date_spent = date_spent

        obj.save()

        return redirect(f'/expenses/{obj.id}/')
    
    return render(request, "view-expense.html",data) 
        


def purchase(request):
    if request.method == "POST":
        # Get data from form
        product_name = request.POST.get("product_name")
        brand = request.POST.get("brand")
        quantity = request.POST.get("quantity")
        amount = request.POST.get("amount")
        purchase_date = request.POST.get("purchase_date")

        if product_name and brand and quantity and amount and purchase_date:
            Purchase.objects.create(product_name=product_name, brand=brand, quantity=quantity, amount=amount, purchase_date=purchase_date)
            return redirect('purchase')

    # Check if purchase_date is being retrieved correctly
    purchase = Purchase.objects.all()
    for item in purchase:
        print(item.purchase_date)  # Log to console or check output
    return render(request, "purchase.html", {"purchase": purchase})

def edit_purchase(request, purchase_id):
    obj = Purchase.objects.get(id = purchase_id)
    if request.method == "POST":
        product_name = request.POST.get("product_name")
        brand = request.POST.get("brand")
        quantity = request.POST.get("quantity")
        amount = request.POST.get("amount")
        purchase_date = request.POST.get("purchase_date")

        if product_name:
            obj.product_name = product_name
        if brand:
            obj.brand = brand
        if quantity:
            obj.quantity = quantity
        if amount:
            obj.amount = amount
        if purchase_date:
            obj.purchase_date = purchase_date

        obj.save()
        return redirect('purchase') 
    data = {"purchase": obj}
    return render(request, "edit-purchase.html", data)

def delete_purchase(request, purchase_id):
    purchase = Purchase.objects.get(id=purchase_id)
    purchase.delete()
    return redirect('purchase')

def sales(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        customer = request.POST.get('customer')
        quantity = request.POST.get('quantity')
        sale_price = request.POST.get('sale_price')
        sale_date = request.POST.get('sale_date')

        if product_name and customer and quantity and sale_price and sale_date:
            try:
                product = Purchase.objects.get(product_name=product_name)
                
                Sales.objects.create(
                    product=product,  
                    customer=customer,  
                    quantity=quantity,
                    sale_price=sale_price,
                    sale_date = sale_date,
                )
                return redirect('sales')

            except Purchase.DoesNotExist:
                return render(request, 'sales.html', {'error': 'Product not found.'})

    purchased_products = Purchase.objects.values('product_name').distinct()
    sales = Sales.objects.all()
    return render(request, 'sales.html', {'sales': sales, 'purchased_products': purchased_products})

def edit_sales(request, sales_id):
    obj = Sales.objects.get(id=sales_id)
    if request.method == "POST":
        product_name = request.POST.get('product_name')
        customer = request.POST.get('customer')
        quantity = request.POST.get('quantity')
        sale_price = request.POST.get('sale_price')
        sale_date = request.POST.get('sale_date')
        if product_name:
            purchase_obj = Purchase.objects.get(product_name=product_name)
            obj.product = purchase_obj 
        if customer:
            obj.customer = customer

        if quantity:
            obj.quantity = quantity

        if sale_price:
            obj.sale_price = sale_price
        
        if sale_date:
            obj.sale_date = sale_date

        obj.save()  
        return redirect('sales')  

    purchased_products = Purchase.objects.all()
    data = {
        "sales": obj,
        "purchased_products": purchased_products,  
    }
    return render(request, "edit-sales.html", data)

def delete_sales(request,sales_id):
    sales = Sales.objects.get(id=sales_id)
    sales.delete()
    return redirect ('sales')

def stocks(request):
    stock_info = []
    products = Purchase.objects.all()
    for product in products:
        total_purchased = Purchase.objects.filter(id=product.id).values('quantity').first()['quantity']
        total_sold = Sales.objects.filter(product=product).aggregate(Sum('quantity'))['quantity__sum'] or 0
        total_returend = Returns.objects.filter(product=product).aggregate(Sum('quantity'))['quantity__sum'] or 0
        available_stock = total_purchased - total_sold + total_returend
        stock_info.append({'product_name': product.product_name, 'available_stock': available_stock})
    return render(request, 'stocks.html', {'available_stocks': stock_info})


def returns(request):
    purchased_products = Purchase.objects.all()
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        quantity = request.POST.get('quantity')
        customer = request.POST.get('customer')
        reason = request.POST.get('reason')
        product = Purchase.objects.filter(product_name=product_name).first()

        if product:
            Returns.objects.create(product=product, product_name=product_name, quantity=quantity, reason=reason, customer=customer)
            return redirect('returns')  
    return_info = []
    returns = Returns.objects.all()
    for ret in returns:
        product_name = ret.product.product_name 
        total_returned = Returns.objects.filter(product=ret.product).aggregate(Sum('quantity'))['quantity__sum'] or 0  
        return_info.append({'product_name': product_name, 'total_returned': total_returned, 'reason': ret.reason,   'quantity': ret.quantity, 'customer':ret.customer })
    
    return render(request, "returns.html", {'return_details': return_info, 'purchased_products': purchased_products  })
    

def new_reports(request):
    leads = []
    if request.method == "POST":
        from_date = request.POST.get("from_date")
        to_date = request.POST.get("to_date")
        status = request.POST.get("status")
        print(leads)

        if from_date:
            from_date = datetime.strptime(from_date, "%Y-%m-%d").date()
        if to_date:
            to_date = datetime.strptime(to_date, "%Y-%m-%d").date()  
        if from_date and to_date:
            leads = Report.objects.filter(created_date__range=(from_date, to_date))
            if status:
                leads = PersonalInformation.objects.filter(category=status).count()
      

    return render(request, "new-reports.html", {"leads": leads})
    

def renew_member_list(request):
    all_data = PersonalInformation.objects.filter(status='converted')
    members_data = AddMember.objects.all()
    today = date.today()

    for client in all_data:
        service_duration = client.services.duration if client.services else None
        
        if client.assigned_date and service_duration:
            try:
                value, unit = service_duration.split()
                value = int(value)

                if "month" in unit.lower():
                    expiry_date = client.assigned_date + relativedelta(months=value)
                    
                    # Calculate days until expiry
                    days_until_expiry = (expiry_date - today).days
                    
                    # Set notification status
                    if days_until_expiry < 0:
                        notification_status = "Expired"
                    elif days_until_expiry <= 7:
                        notification_status = "Expires this week!"
                    elif days_until_expiry <= 15:
                        notification_status = "Expires in 2 weeks"
                    elif days_until_expiry <= 30:
                        notification_status = "Expires in 1 month"
                    else:
                        notification_status = "Active"
                    
                    client.expiry_date = expiry_date
                    client.notification_status = notification_status
                    client.days_remaining = days_until_expiry if days_until_expiry > 0 else 0
                    
                else:
                    client.expiry_date = "Invalid Duration"
                    client.notification_status = "Error"
                    client.days_remaining = 0
            except ValueError:
                client.expiry_date = "Invalid Duration"
                client.notification_status = "Error"
                client.days_remaining = 0
        else:
            client.expiry_date = "No Service Duration"
            client.notification_status = "No Plan"
            client.days_remaining = 0

        client.renewal_date = client.renewal_date or "Not Renewed Yet"

    return render(request, "renew_member_list.html", {
        "all_data": all_data,
        "today": today,
    })
def renew_member_page(request, member_id):
    member = get_object_or_404(AddMember, id=member_id)
    if request.method == "POST":
        renewal_date = request.POST.get("renewal_date")
        member.renewal_date = renewal_date
        member.save()
        messages.success(request, "Membership renewed successfully!")
        return redirect("renew_member_list")
    return render(request, "renew_member_page.html", {"member": member})



def renew_member_page(request, member_id):
    # Fetch the member's details using their ID
    member = get_object_or_404(PersonalInformation, id=member_id)

    if request.method == "POST":
        # Get the renewal date from the form input
        renewal_date = request.POST.get("renewal_date")
        
        # Update the renewal date for the member
        member.renewal_date = renewal_date
        member.save()

        # Show success message and redirect
        messages.success(request, "Membership renewed successfully!")
        return redirect("renew_member_list")

    return render(request, "renew_member_page.html", {"member": member})



def save_renewal_date(request, client_id):
    client = get_object_or_404(PersonalInformation, id=client_id)
    
    if request.method == 'POST':
        renewal_date_str = request.POST.get('renewal_date')
        
        # Convert the string to a date object
        renewal_date = datetime.strptime(renewal_date_str, '%Y-%m-%d').date()
        
        # Save the renewal date to the model
        client.renewal_date = renewal_date
        client.save()

        messages.success(request, "Renewal date updated successfully!")
        return redirect('renew_member_list')

    return render(request, 'renew_member_page.html', {'client': client})


def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date() if date_str else None
    except ValueError:
        return None  # Handle invalid date formats

def add_member(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        mobile_number = request.POST.get('mobile_number')
        aadhar_number = request.POST.get('aadhar_number')
        uploaded_file = request.FILES.get('filename')
        email = request.POST.get('email')
        date_of_birth = parse_date(request.POST.get('date_of_birth', ''))
        location = request.POST.get('location')
        source = request.POST.get('source')
        occupation = request.POST.get('occupation')
        emergency_number = request.POST.get('emergency_number')
        registration_amount = request.POST.get('reg_amount')
        conveniance_fees = float(request.POST.get('conveniance_fees', 0))

        # Ensure total_amount is a valid number (Default to 0 if empty)
        total_amount = request.POST.get('total_amount', '0')
        total_amount = float(total_amount) if total_amount.replace('.', '', 1).isdigit() else 0.0

        # Convert dates safely
        enrollment_date = parse_date(request.POST.get('enrollment_date', ''))
        activation_date = parse_date(request.POST.get('activation_date', ''))
        expiry_date = parse_date(request.POST.get('expiry_date', ''))
        payment_date = parse_date(request.POST.get('payment_date', ''))

        current_installment_amount = request.POST.get('current_installment_amount')
        payment_mode = request.POST.get('payment_mode')
        sold_by_id = request.POST.get('sold_by')
        select_membership_plan_id = request.POST.get("select_membership_plan")

        # Handle discount field: If empty, set to 0
        discount = request.POST.get('discount', '0')
        discount = float(discount) if discount.replace('.', '', 1).isdigit() else 0.0
        discount_type = request.POST.get('discount_type')

        # Convert IDs safely
        service_id = request.POST.get('service')
        batch_id = request.POST.get('group')
        cost_of_plan_id = request.POST.get('cost_of_plan')
        total_session_id = request.POST.get('total_session')

        service = Service.objects.filter(id=int(service_id)).first() if service_id and service_id.isdigit() else None
        batch = Service.objects.filter(id=int(batch_id)).first() if batch_id and batch_id.isdigit() else None
        cost_of_plan = Service.objects.filter(id=int(cost_of_plan_id)).first() if cost_of_plan_id and cost_of_plan_id.isdigit() else None
        total_session = Service.objects.filter(id=int(total_session_id)).first() if total_session_id and total_session_id.isdigit() else None
        select_membership_plan = Plan.objects.filter(id=int(select_membership_plan_id)).first() if select_membership_plan_id and select_membership_plan_id.isdigit() else None

        # Get the UserProfile object for sold_by
        sold_by = UserProfile.objects.filter(id=int(sold_by_id)).first() if sold_by_id and sold_by_id.isdigit() else None

        # Validate required fields
        if not name or not gender or not mobile_number or not aadhar_number or not email:
            messages.error(request, "Required fields are missing")
            return redirect('add_member')

        if not sold_by:
            messages.error(request, "Sold By field is required")
            return redirect('add_member')

        # Save the member
        member = AddMember(
            name=name,
            gender=gender,
            mobile_number=mobile_number,
            aadhar_number=aadhar_number,
            uploaded_file=uploaded_file,
            email=email,
            date_of_birth=date_of_birth,
            location=location,
            source=source,
            occupation=occupation,
            emergency_number=emergency_number,
            registration_amount=registration_amount,
            service=service,
            batch=batch,
            cost_of_plan=cost_of_plan,
            total_session=total_session,
            conveniance_fees=conveniance_fees,
            total_amount=total_amount,
            enrollment_date=enrollment_date,
            activation_date=activation_date,
            expiry_date=expiry_date,
            current_installment_amount=current_installment_amount,
            payment_mode=payment_mode,
            payment_date=payment_date,
            sold_by=sold_by,
            discount=discount,
            discount_type=discount_type,
            select_membership_plan=select_membership_plan,
        )

        member.save()
        messages.success(request, "Member added successfully!")
        return redirect('display_add_members')

    available_services = Service.objects.all()
    group = Service.objects.all()
    sale_by = UserProfile.objects.all()
    membership_plan = Plan.objects.all()

    return render(request, 'add-members.html', {
        'available_services': available_services,
        'group': group,
        'sale_by': sale_by,
        'membership_plan': membership_plan,
    })



def display_add_members(request):
    add_members = AddMember.objects.all()
    return render(request, "display-all-add-members.html", {"add_members": add_members})


def view_add_members(request, id):
    obj = get_object_or_404(AddMember, id=id)  # Ensures a 404 if not found
    # member = AddMember.objects.get(id=1)  # Replace with actual ID
    # print(member.cost_of_plan)  # Should return a Service object or None
    # print(member.cost_of_plan.name if member.cost_of_plan else "No Plan Assigned")
    # service = Service.objects.first()  # Get a valid service
    # member.cost_of_plan = service
    # member.save()

    if request.method == "POST":
        obj.name = request.POST.get('name', obj.name)
        obj.gender = request.POST.get('gender', obj.gender)
        obj.mobile_number = request.POST.get('mobile_number', obj.mobile_number)
        obj.aadhar_number = request.POST.get('aadhar_number', obj.aadhar_number)
        obj.email = request.POST.get('email', obj.email)
        obj.date_of_birth = request.POST.get('date_of_birth', obj.date_of_birth)
        obj.location = request.POST.get('location', obj.location)
        obj.source = request.POST.get('source', obj.source)
        obj.occupation = request.POST.get('occupation', obj.occupation)
        obj.emergency_number = request.POST.get('emergency_number', obj.emergency_number)
        obj.registration_amount = request.POST.get('reg_amount', obj.registration_amount)
        obj.service = request.POST.get('service', obj.service)
        obj.batch = request.POST.get('group', obj.batch)
        obj.cost_of_plan = request.POST.get('cost_of_plan', obj.cost_of_plan)
        obj.total_session = request.POST.get('total_session', obj.total_session)
        obj.conveniance_fees = request.POST.get('conveniance_fees', obj.conveniance_fees)
        obj.total_amount = request.POST.get('total_amount', obj.total_amount)
        obj.enrollment_date = request.POST.get('enrollment_date', obj.enrollment_date)
        obj.activation_date = request.POST.get('activation_date', obj.activation_date)
        obj.expiry_date = request.POST.get('expiry_date', obj.expiry_date)
        obj.current_installment_amount = request.POST.get('current_installment_amount', obj.current_installment_amount)
        obj.payment_mode = request.POST.get('payment_mode', obj.payment_mode)
        obj.payment_date = request.POST.get('payment_date', obj.payment_date)
        obj.sold_by = request.POST.get('sold_by', obj.sold_by)
        obj.discount = request.POST.get('discount', obj.discount)
        obj.discount_type = request.POST.get('discount_type', obj.discount_type)
        obj.select_membership_plan = request.POST.get('select_membership_plan', obj.select_membership_plan)

        # File Upload
        uploaded_file = request.FILES.get('filename')
        if uploaded_file:
            obj.uploaded_file = uploaded_file

        obj.save()
        messages.success(request, "Data updated successfully")
        return redirect(f'/display_add_members/{obj.id}/')

    return render(request, "view-each-add-members.html", {"member": obj})

def delete_added_members(request,id):
    delete_added_members = AddMember.objects.get(id=id)
    delete_added_members.delete()
    return redirect('display_add_members')

def bill(request):
    return render(request,"bill.html")


def view_all_clients(request):
    leads = PersonalInformation.objects.all()
    print(leads)
    add_members = AddMember.objects.all()
    print(add_members)

    return render(request, "all-clients.html", {'leads': leads, 'add_members': add_members})


from django.http import HttpResponse
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill
from openpyxl.utils import get_column_letter
from datetime import datetime
from django.shortcuts import render
from django.core.exceptions import BadRequest
from django.db.models import Q
from .models import AddMember, PersonalInformation, Payments, Sales, Purchase, Expense

def download_report(request):
    try:
        # Get filter parameters
        from_date = request.GET.get('from_date')
        to_date = request.GET.get('to_date')
        status = request.GET.get('status')

        if not all([from_date, to_date, status]):
            return HttpResponse("Please provide all required parameters", status=400)

        # Create workbook
        wb = Workbook()
        ws = wb.active

        # Define styles
        header_font = Font(bold=True, color="FFFFFF")
        header_fill = PatternFill(start_color="366092", end_color="366092", fill_type="solid")

        # Configure report structure
        report_config = {
            "combined_leads_members": {
                "title": "Leads & Members Report",
                "headers": [
                    "Name", "Gender", "Mobile Number", "Email", "Location",
                    "Occupation", "Source", "Service", "Membership Plan",
                    "Registration Amount", "Enrollment Date", "Expiry Date", "Type"
                ],
                "queryset": list(AddMember.objects.filter(enrollment_date__range=[from_date, to_date])) +
                            list(PersonalInformation.objects.filter(created_date__range=[from_date, to_date]))
            },
            "payments": {
                "title": "Payments Report",
                "headers": ["Member Name", "Amount Paid", "Pending Amount", "Payment Mode", "Date Paid", "Created Date"],
                "queryset": Payments.objects.filter(date_paid__range=[from_date, to_date])
            },
            "sales": {
                "title": "Sales Report",
                "headers": ["Product Name", "Customer", "Quantity", "Sale Price", "Discount", "Sale Date", "Total Amount"],
                "queryset": Sales.objects.filter(sale_date__range=[from_date, to_date])
            },
            "purchases": {
                "title": "Purchases Report",
                "headers": ["Item Name", "Supplier", "Quantity", "Purchase Price", "Purchase Date"],
                "queryset": Purchase.objects.filter(purchase_date__range=[from_date, to_date])
            },
            "expenses": {
                "title": "Expenses Report",
                "headers": ["Expense Name", "Price", "Quantity", "Date Spent"],
                "queryset": Expense.objects.filter(date_spent__range=[from_date, to_date])
            },
        }

        # Validate requested report type
        if status not in report_config:
            return HttpResponse("Invalid report type", status=400)

        # Get report details
        config = report_config[status]
        ws.title = config["title"]
        headers = config["headers"]
        queryset = config["queryset"]

        # Apply headers
        for col, header in enumerate(headers, 1):
            cell = ws.cell(row=1, column=col, value=header)
            cell.font = header_font
            cell.fill = header_fill
            cell.alignment = Alignment(horizontal="center")
            ws.column_dimensions[get_column_letter(col)].width = 18

        row = 2  # Start from second row after headers

        # Process data for combined Leads & Members
        if status == "combined_leads_members":
            for item in queryset:
                data = [
                    getattr(item, "name", ""),
                    getattr(item, "gender", ""),
                    getattr(item, "mobile_number", ""),
                    getattr(item, "email", ""),
                    getattr(item, "location", "N/A") if isinstance(item, AddMember) else "N/A",
                    getattr(item, "occupation", ""),
                    getattr(item, "source", ""),
                    getattr(item.service, "name", "N/A") if isinstance(item, AddMember) else 
                    (getattr(item.services, "name", "N/A") if getattr(item, "services", None) else "N/A"),
                    getattr(item.select_membership_plan, "plan_name", "N/A") if isinstance(item, AddMember) else 
                    (getattr(item.plan_leads, "plan_name", "N/A") if getattr(item, "plan_leads", None) else "N/A"),
                    getattr(item, "registration_amount", "N/A") if isinstance(item, AddMember) else "N/A",
                    getattr(item, "enrollment_date", "N/A") if isinstance(item, AddMember) else "N/A",
                    getattr(item, "expiry_date", "N/A") if isinstance(item, AddMember) else "N/A",
                    "Member" if isinstance(item, AddMember) else "Lead"
                ]
                for col, value in enumerate(data, 1):
                    cell = ws.cell(row=row, column=col, value=value)
                    cell.alignment = Alignment(horizontal="center")
                row += 1

        # Process Payments
        elif status == "payments":
            for item in queryset:
                data = [
                    getattr(item.name, 'name', '') if getattr(item, 'name', None) else '',
                    getattr(item, 'amount_paid', ''),
                    getattr(item, 'pending_amount', ''),
                    getattr(item, 'payment_mode', ''),
                    str(getattr(item, 'date_paid', '')),
                    str(getattr(item, 'created_date', ''))
                ]
                for col, value in enumerate(data, 1):
                    ws.cell(row=row, column=col, value=value)
                row += 1

        # Process Sales
        elif status == "sales":
            for item in queryset:
                total_amount = (getattr(item, 'sale_price', 0) or 0) * getattr(item, 'quantity', 0)
                if getattr(item, 'discount', None):
                    total_amount *= (1 - item.discount / 100)
                data = [
                    getattr(item, 'product_name', ''),
                    getattr(item, 'customer', ''),
                    getattr(item, 'quantity', ''),
                    getattr(item, 'sale_price', ''),
                    getattr(item, 'discount', ''),
                    str(getattr(item, 'sale_date', '')),
                    round(total_amount, 2)
                ]
                for col, value in enumerate(data, 1):
                    ws.cell(row=row, column=col, value=value)
                row += 1

        # Process Purchases
        elif status == "purchases":
            for item in queryset:
                data = [
                    getattr(item, "item_name", ""),
                    getattr(item, "supplier", ""),
                    getattr(item, "quantity", ""),
                    getattr(item, "price", ""),
                    str(getattr(item, "purchase_date", ""))
                ]
                for col, value in enumerate(data, 1):
                    ws.cell(row=row, column=col, value=value)
                row += 1

        # Process Expenses
        elif status == "expenses":
            for item in queryset:
                data = [
                    getattr(item, "expense_name", ""),
                    getattr(item, "price", ""),
                    getattr(item, "quantity", ""),
                    str(getattr(item, "date_spent", ""))
                ]
                for col, value in enumerate(data, 1):
                    ws.cell(row=row, column=col, value=value)
                row += 1

        # Create response
        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = f'attachment; filename={status}_report_{datetime.now().strftime("%Y%m%d")}.xlsx'
        wb.save(response)
        return response

    except Exception as e:
        return HttpResponse(f"Error generating report: {str(e)}", status=500)

import os
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import red, black
from .models import AddMember

def generate_invoice(request, member_id):
    """Generate a professional PDF invoice with gym details, logo, and payment info."""
    member = get_object_or_404(AddMember, id=member_id)

    # Ensure pending amount is correct
    pending_amount = max(member.total_amount - member.current_installment_amount, 0)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="invoice_{member.name}.pdf"'

    pdf = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    # **Gym Name - TEFFEY FITNESS**
    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawCentredString(width / 2, height - 50, "TEFFEY FITNESS")

    # **Gym Logo - Dynamic Path Handling**
    gym_logo_path = 'static/image/Mask group (2).png'  # Update this with your actual logo path
    if gym_logo_path:
        pdf.drawImage(gym_logo_path, 30, height - 110, width=100, height=100)

    # **Invoice Title**
    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawCentredString(width / 2, height - 120, "INVOICE")

    # **Member Details**
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, height - 160, "Member Information")
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, height - 180, f"Name: {member.name}")
    pdf.drawString(50, height - 200, f"Email: {member.email or 'N/A'}")
    pdf.drawString(50, height - 220, f"Phone: {member.mobile_number or 'N/A'}")
    pdf.drawString(50, height - 240, f"Gender: {member.gender or 'N/A'}")
    pdf.drawString(50, height - 260, f"Location: {member.location or 'N/A'}")

    # **Service & Membership**
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, height - 290, "Service & Membership Details")
    pdf.setFont("Helvetica", 12)
    service_name = member.service.name if member.service else "N/A"
    membership_name = member.select_membership_plan.plan_name if member.select_membership_plan else "N/A"
    pdf.drawString(50, height - 310, f"Service Taken: {service_name}")
    pdf.drawString(50, height - 330, f"Membership Plan: {membership_name}")
    pdf.drawString(50, height - 350, f"Enrollment Date: {member.enrollment_date}")
    pdf.drawString(50, height - 370, f"Expiry Date: {member.expiry_date}")

    # **Payment Details**
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, height - 400, "Payment Details")
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, height - 420, f"Total Amount: RS.{member.total_amount:.2f}")
    pdf.drawString(50, height - 440, f"Amount Paid: RS.{member.current_installment_amount:.2f}")
    pdf.drawString(50, height - 460, f"Pending Amount: RS.{pending_amount:.2f}")

    # **Highlight Pending Amount if Any**
    if pending_amount > 0:
        pdf.setFont("Helvetica-Bold", 14)
        pdf.setFillColor(red)
        pdf.drawString(50, height - 490, f" PENDING DUE: RS.{pending_amount:.2f}")
        pdf.setFillColor(black)

    # **Footer - Contact Info**
    pdf.setFont("Helvetica", 10)
    pdf.drawString(50, 30, "TEFFEY FITNESS | www.teffeyfitness.com | CONTACT US : 9865638121")

    # **Finalize and Save the PDF**
    pdf.showPage()
    pdf.save()

    return response




def update_member_payment(request, member_id):
    """Handles updating member payments and prevents overpayment."""
    member = get_object_or_404(AddMember, id=member_id)

    if request.method == 'POST':
        amount_paid = float(request.POST.get('amount_paid', 0))
        pending_amount = max(member.total_amount - member.current_installment_amount, 0)

        if amount_paid > pending_amount:
            messages.error(request, f"Payment failed! You cannot pay more than ₹{pending_amount}.")
        elif amount_paid > 0:
            member.current_installment_amount += amount_paid
            member.payment_date = now()

            # Ensure the total paid does not exceed the total amount
            if member.current_installment_amount >= member.total_amount:
                member.current_installment_amount = member.total_amount  # Set it to total amount if overpaid

            member.save()
            pending_amount = max(member.total_amount - member.current_installment_amount, 0)

            messages.success(request, f"Payment of ₹{amount_paid} updated! Pending: ₹{pending_amount}")

    return redirect('view_each_member', member_id=member.id)




def view_each_member(request, member_id):
    """Retrieve a specific member and ensure pending amount is included"""
    member = get_object_or_404(AddMember, id=member_id)
    
    # Fetch the pending amount (same logic as in add-members.html)
    pending_amount = max(member.total_amount - member.current_installment_amount, 0)

    return render(request, 'view-each-add-members.html', {
        'member': member,
        'pending_amount': pending_amount,  # Pass this to the template
    })