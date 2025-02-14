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
from django.db.models import Sum
from django.utils.timezone import now  
from django.utils.timezone import localtime
from datetime import datetime , timedelta
from django.http import HttpResponseRedirect, HttpResponse
from decimal import Decimal
import calendar
from openpyxl import Workbook
from openpyxl.styles import Alignment


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

    # Count of today's enrollments (filter by today's exact date)
   
    today_enrollments = PersonalInformation.objects.filter(
        status='converted',
        assigned_date__year=today.year,
        assigned_date__month=today.month,
        assigned_date__day=today.day
    ).count()

    today_add_members_count = AddMember.objects.filter(
        enrollment_date__year = today.year,
        enrollment_date__month = today.month,
        enrollment_date__day = today.day,
    ).count()

    daily_enrollments = today_enrollments + today_add_members_count

    # Count of all converted leads
    member_count = PersonalInformation.objects.filter(status='converted').count()

    # Count of all members (all leads)
    all_member_count = PersonalInformation.objects.count() + AddMember.objects.count()


    # Count of sales records
    sales = Sales.objects.filter(
        sale_date__year = today.year,
        sale_date__month = today.month,
    ).count()


    today_sales = Sales.objects.filter(
        sale_date__year = today.year,
        sale_date__month = today.month,
        sale_date__day = today.day,

    ).count()

    # Count of purchase records
    purchase = Purchase.objects.filter(
        purchase_date__year = today.year,
        purchase_date__month = today.month,
    ).count()

    today_purchase = Purchase.objects.filter(
        purchase_date__year = today.year,
        purchase_date__month = today.month,
        purchase_date__day  = today.day

    ).count()

    # Count of follow-up leads
    follow_up = PersonalInformation.objects.filter(status='follow_up').count()

    today_follow_up = PersonalInformation.objects.filter(status="follow_up", assigned_date__year = today.year,
                                                         assigned_date__month = today.month,
                                                          assigned_date__day = today.day ).count()

    # Count of enrollments for the current month
    converted_count = PersonalInformation.objects.filter(
        status='converted',
        assigned_date__year=today.year,
        assigned_date__month=today.month
    ).count()

    enrolled_count = AddMember.objects.filter(
        # status='converted',
        enrollment_date__year=today.year,
        enrollment_date__month=today.month
    ).count()

    total_enrollments = converted_count + enrolled_count



    # Count of today's renewals (filter by exact date)
    today_renewals = Renew.objects.filter(
        renew_date__year=today.year,
        renew_date__month=today.month,
        renew_date__day=today.day
    ).count()

    # Count of renewals for the current month (filter by year and month)
    renewals = Renew.objects.filter(
        renew_date__year=today.year,
        renew_date__month=today.month
    ).count()

    expiry_date = Renew.objects.filter(
        expiry_date__year = today.year,
        expiry_date__month=today.month
    ).count()

    today_expiry_date = Renew.objects.filter(
        expiry_date__year=today.year,
        expiry_date__month=today.month,
        expiry_date__day=today.day
    ).count()

    # Display success message
    messages.success(request, "WELCOME TO TEFFY FITNESS ")

    # Render the response with the necessary context
    return render(request, 'main-page.html', {
        'member_count': member_count,
        'sales': sales,
        'purchase': purchase,
        'follow_up': follow_up,
        'all_member_count': all_member_count,
        'total_enrollments':total_enrollments,
        'renewals': renewals,
        'daily_enrollments':daily_enrollments,
        'today_renewals': today_renewals,  # Add the today_renewals in the context
        'today_sales' : today_sales,
        'today_purchase':today_purchase,
        'today_follow_up':today_follow_up,
        'expiry_date':expiry_date,
        'today_expiry_date':today_expiry_date,
    })



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

        # Assigning service and plan to the client
        lead.services = selected_service
        lead.plan_leads = selected_plan

        lead.save()  # This will automatically call save and calculate the expiry_date

        return redirect('converted_leads')

    all_data = PersonalInformation.objects.filter(status='converted')
    available_services = Service.objects.all()
    plans = Plan.objects.all()

    return render(request, 'converted_leads.html', {
        'all_data': all_data,
        'status_title': 'Converted',
        'available_services': available_services,
        'plans':plans,
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

    # Optionally calculate any other values you want to display
    for client in all_data:
        client.expiry_date_display = client.expiry_date  # Get expiry date dynamically

        # If renewal date exists, you can pass it to the template
        client.renewal_date_display = client.renewal_date if client.renewal_date else 'Not Renewed Yet'

    return render(request, "renew_member_list.html", {"all_data": all_data})



# def renew_member_page(request, member_id):
#     # Fetch the member's details using their ID
#     member = get_object_or_404(PersonalInformation, id=member_id)

#     # Check if the member has a service assigned
#     if not member.services:
#         messages.error(request, "This member does not have a service assigned.")
#         return redirect("renew_member_list")

#     service = member.services

#     # Extract the duration of the service in months (e.g., "5 months")
#     try:
#         duration_months = int(service.duration.split()[0])
#     except ValueError:
#         messages.error(request, "Invalid service duration format.")
#         return redirect("renew_member_list")

#     # Get the renewal date (either from the last renewal or assigned date)
#     renew_date = member.renew_set.last().renew_date if member.renew_set.exists() else member.assigned_date

#     # Calculate the new expiry date
#     new_month = renew_date.month + duration_months
#     new_year = renew_date.year + (new_month - 1) // 12  # Adjust year if month exceeds 12
#     new_month = (new_month - 1) % 12 + 1  # Keep month between 1-12

#     # Get the last valid day of the new month
#     last_day_of_month = calendar.monthrange(new_year, new_month)[1]
#     new_day = min(renew_date.day, last_day_of_month)  # Adjust if the day is out of range

#     # Create the new expiry date
#     expiry_date = date(new_year, new_month, new_day)

#     # If the form is submitted, save the renewal details
#     if request.method == "POST":
#         payment_method = request.POST.get("payment_method")
        
#         # Save the renewal record
#         Renew.objects.create(
#             name=member,
#             service=service,
#             renew_date=renew_date,
#             expiry_date=expiry_date,
#             payment_method=payment_method,
#         )

#         # Show a success message and redirect
#         messages.success(request, "Membership renewed successfully!")
#         return redirect("renew_member_list")

#     # If not a POST request, show the renewal page
#     return render(request, "renew_member_page.html", {"member": member, "renew_date": renew_date})

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

# def add_members(request):
#     available_services = Service.objects.all()
#     group = Service.objects.all()
#     return render(request,"add-members.html", {"available_services": available_services,"group":group})
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .models import Service, AddMember


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
    return render(request,"display-all-add-members.html", {"add_members":add_members})


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



# from django.http import HttpResponse
# from openpyxl import Workbook
# from datetime import datetime


# # from django.http import HttpResponse
# # from openpyxl import Workbook
# # from datetime import datetime
# # from your_app.models import Payments, PersonalInformation  # Replace 'your_app' with your actual app name

# def download_report(request):
#     # Get query parameters
#     from_date = request.GET.get('from_date', None)
#     to_date = request.GET.get('to_date', None)
#     status = request.GET.get('status', None)

#     # Convert date strings to datetime objects
#     if from_date and to_date:
#         from_date = datetime.strptime(from_date, "%Y-%m-%d")
#         to_date = datetime.strptime(to_date, "%Y-%m-%d")

#     # Filter Payments data based on the date range
#     payment_data = Payments.objects.filter(date_paid__range=[from_date, to_date]) if from_date and to_date else Payments.objects.all()

#     # Filter Leads data based on the date range and status
#     leads_data = PersonalInformation.objects.filter(created_date__range=[from_date, to_date]) if from_date and to_date else PersonalInformation.objects.all()
    
#     if status:  # Apply status filter if provided
#         leads_data = leads_data.filter(status=status)

#     # Create a workbook and worksheet
#     wb = Workbook()
#     ws = wb.active
#     ws.title = "Payments & Leads Report"

#     # Define column headers
#     columns = [
#         "Name", "Amount Paid", "Pending Amount", "Payment Mode", "Payment Date",  # Payments
#         "Lead Name", "Phone Number", "Email", "Created Date", "Status"  # Leads
#     ]
#     ws.append(columns)

#     # Append Payments data to the worksheet
#     for payment in payment_data:
#         date_paid = payment.date_paid.replace(tzinfo=None) if payment.date_paid and payment.date_paid.tzinfo else payment.date_paid
#         row = [
#             payment.name,  
#             payment.amount_paid,
#             payment.pending_amount,
#             payment.payment_mode,
#             date_paid,
#             "", "", "", "", ""  # Empty placeholders for Leads
#         ]
#         ws.append(row)

#     # Append Leads data to the worksheet
#     for lead in leads_data:
#         created_date = lead.created_date.replace(tzinfo=None) if lead.created_date and lead.created_date.tzinfo else lead.created_date
#         row = [
#             "", "", "", "", "",  # Empty placeholders for Payments
#             str(lead.name),  
#             str(lead.phone_number),
#             str(lead.email),
#             created_date,
#             str(lead.status)  # Ensure status is a string
#         ]
#         ws.append(row)

#     # Adjust column widths for better readability
#     for col in ws.columns:
#         max_length = 0
#         column = col[0].column_letter
#         for cell in col:
#             try:
#                 if cell.value:
#                     max_length = max(max_length, len(str(cell.value)))
#             except:
#                 pass
#         ws.column_dimensions[column].width = max_length + 2

#     # Return the Excel file as a response
#     response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
#     response['Content-Disposition'] = 'attachment; filename="gym_report.xlsx"'
#     wb.save(response)
#     return response

from django.http import HttpResponse
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill
from datetime import datetime
from django.shortcuts import render
from django.core.exceptions import BadRequest
from django.db.models import Q

def download_report(request):
    # Get filter parameters
    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')
    status = request.GET.get('status')

    if not all([from_date, to_date, status]):
        raise BadRequest("Please provide all required parameters")

    # Create workbook
    wb = Workbook()
    ws = wb.active

    # Define styles
    header_font = Font(bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="366092", end_color="366092", fill_type="solid")

    # Configure report based on category
    if status == 'PersonalInformation':
        ws.title = "Personal Information Report"
        headers = [
            "Name", "Address", "Occupation", "Gender", "Mobile", "Email",
            "Perfect Body", "Body Type", "Goal", "Body You Want",
            "Level of Body Fat", "Problem Areas", "Diets",
            "Water Intake", "Food Division", "Event Coming Up",
            "Height", "Current Weight", "Target Weight", "Level of Fitness"
        ]
        queryset = PersonalInformation.objects.filter(
            created_date__range=[from_date, to_date]
        )
        
    elif status in ['new', 'converted', 'not-converted', 'follow-up', 'pending']:
        ws.title = f"{status.title()} Leads Report"
        headers = [
            "Name", "Mobile", "Email", "Status", "Follow Up Date",
            "Created Date", "Service", "Plan", "Height", "Current Weight",
            "Target Weight", "Goal"
        ]
        queryset = PersonalInformation.objects.filter(
            Q(created_date__range=[from_date, to_date]) &
            Q(status=status)
        )

    elif status == 'sales':
        ws.title = "Sales Report"
        headers = [
            "Product Name", "Customer", "Quantity", "Sale Price",
            "Discount", "Sale Date", "Total Amount"
        ]
        queryset = Sales.objects.filter(sale_date__range=[from_date, to_date])

    elif status == 'purchase':
        ws.title = "Purchase Report"
        headers = [
            "Product Name", "Brand", "Quantity", "Amount",
            "Purchase Date"
        ]
        queryset = Purchase.objects.filter(purchase_date__range=[from_date, to_date])

    elif status == 'returns':
        ws.title = "Returns Report"
        headers = [
            "Product Name", "Customer", "Quantity", "Reason",
            "Return Date"
        ]
        queryset = Returns.objects.filter(return_date__range=[from_date, to_date])

    elif status == 'stocks':
        ws.title = "Stock Report"
        headers = [
            "Product Name", "Quantity", "Purchase Details"
        ]
        queryset = Stock.objects.all()  # Usually stocks don't need date filtering

    elif status == 'payments':
        ws.title = "Payments Report"
        headers = [
            "Member Name", "Amount Paid", "Pending Amount",
            "Payment Mode", "Date Paid", "Created Date"
        ]
        queryset = Payments.objects.filter(date_paid__range=[from_date, to_date])

    else:
        raise BadRequest("Invalid report type")

    # Apply headers
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal="center")
        ws.column_dimensions[chr(64 + col)].width = 15

    # Add data based on report type
    for row, item in enumerate(queryset, 2):
        if status == 'PersonalInformation':
            data = [
                item.name, item.address, item.occupation, item.gender,
                item.mobile_number, item.email, item.perfect_body,
                item.body_type, item.goal, item.body_you_want,
                item.level_of_body_fat, item.problem_areas, item.diets,
                item.water_you_drink_daily, item.eat_or_dividie_foods_or_beverages,
                item.event_coming_up, item.height, item.current_weight,
                item.target_weight, item.level_of_fitness
            ]
        elif status in ['new', 'converted', 'not-converted', 'follow-up', 'pending']:
            data = [
                item.name, item.mobile_number, item.email, item.status,
                str(item.follow_up_date), str(item.created_date),
                item.services.name if item.services else '',
                item.plan_leads.plan_name if item.plan_leads else '',
                item.height, item.current_weight, item.target_weight, item.goal
            ]
        elif status == 'sales':
            total_amount = (item.sale_price or 0) * item.quantity
            if item.discount:
                total_amount = total_amount * (1 - item.discount/100)
            data = [
                item.product_name, item.customer, item.quantity,
                item.sale_price, item.discount, str(item.sale_date),
                total_amount
            ]
        elif status == 'purchase':
            data = [
                item.product_name, item.brand, item.quantity,
                item.amount, str(item.purchase_date)
            ]
        elif status == 'returns':
            data = [
                item.product_name, item.customer, item.quantity,
                item.reason, str(item.return_date)
            ]
        elif status == 'stocks':
            data = [
                item.product_name, item.quantity,
                f"Purchase ID: {item.purchase.id}" if item.purchase else 'N/A'
            ]
        elif status == 'payments':
            data = [
                item.name.name if item.name else '', item.amount_paid,
                item.pending_amount, item.payment_mode,
                str(item.date_paid), str(item.created_date)
            ]

        for col, value in enumerate(data, 1):
            ws.cell(row=row, column=col, value=value)

    # Add summary section
    summary_row = len(queryset) + 3
    ws.cell(row=summary_row, column=1, value="Report Summary").font = Font(bold=True)
    ws.cell(row=summary_row + 1, column=1, value="Total Records:")
    ws.cell(row=summary_row + 1, column=2, value=len(queryset))
    ws.cell(row=summary_row + 2, column=1, value="Date Range:")
    ws.cell(row=summary_row + 2, column=2, value=f"{from_date} to {to_date}")

    # Add totals for relevant reports
    if status in ['sales', 'payments', 'purchase']:
        total_amount = sum(item.amount_paid if status == 'payments' 
                         else item.amount if status == 'purchase'
                         else (item.sale_price * item.quantity * (1 - (item.discount or 0)/100))
                         for item in queryset)
        ws.cell(row=summary_row + 3, column=1, value="Total Amount:")
        ws.cell(row=summary_row + 3, column=2, value=total_amount)

    # Create response
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = (
        f'attachment; filename={status}_report_{datetime.now().strftime("%Y%m%d")}.xlsx'
    )

    wb.save(response)
    return response