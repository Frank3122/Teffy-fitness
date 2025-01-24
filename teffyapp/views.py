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
from django.http import HttpResponseRedirect
from django.urls import reverse
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
    member_count =  PersonalInformation.objects.filter(status='converted').count()
    sales = Sales.objects.count()
    purchase = Purchase.objects.count()
    follow_up = PersonalInformation.objects.filter(status='follow_up').count()
    messages.success(request,"WELCOME")
    return render(request, 'main-page.html', {'member_count': member_count, "sales":sales, "purchase":purchase, "follow_up":follow_up})

def expense(request):
    return render(request,"expense-page.html")

def follow_up(request):
    return render(request,"follow-up page.html")

def plan(request):
    if request.method == "POST":
        plan_name = request.POST.get('plan_name')
        price = request.POST.get('price')
        duration = request.POST.get('duration')
        batch = request.POST.get('batch')

        if plan_name and price and duration and batch:
            Plan.objects.create(plan_name=plan_name, price=price, duration=duration, batch=batch)
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

# def add_leads(request):
#     return render(request,"add-leads.html")

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


def payment(request, client_id):
    client = PersonalInformation.objects.get(id=client_id)
    if client.services:
        service_price = client.services.prices 
    else:
        service_price = 0  
    total_amount_paid = Payments.objects.filter(payments=client).aggregate(Sum('amount_paid'))['amount_paid__sum'] or 0
    pending_amount = service_price - total_amount_paid

    if request.method == 'POST':
        amount_paid = float(request.POST.get('amount_paid', 0))
        payment_mode = request.POST.get('payment_mode')

        if amount_paid > 0 and payment_mode:
            new_pending_amount = pending_amount - amount_paid 
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
        
    payment_history = Payments.objects.filter(payments=client)
    return render(request,'payment.html',
        {
            'client': client,
            'service_price': service_price,
            'total_amount_paid': total_amount_paid,
            'pending_amount': pending_amount,
            'payment_history': payment_history,
        }
    )

def expenses(request):
    if request.method == "POST":
        expense_name = request.POST.get('expense_name')
        price = request.POST.get('price')
        date_spent = request.POST.get('date_spent')

        if expense_name and price and date_spent:  
            Expense.objects.create(expense_name=expense_name, price=price, date_spent=date_spent)
            return redirect('expenses')  

    now = datetime.now()
    current_month = now.month
    current_year = now.year
    monthly_expenses = Expense.objects.filter(date_spent__month=current_month,date_spent__year=current_year)
    total_monthly_expenses = monthly_expenses.aggregate(Sum('price'))['price__sum'] or 0
    return render(request, 'new-expense.html', {'expenses': monthly_expenses,'total_monthly_expenses': total_monthly_expenses,})


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
        

# def datatable(request):
#     return render(request,"datatable.html")

def purchase(request):
    if request.method == "POST":
        product_name = request.POST.get("product_name")
        brand = request.POST.get("brand")
        quantity = request.POST.get("quantity")
        amount = request.POST.get("amount")
        if product_name and brand and quantity and amount:
            Purchase.objects.create(product_name=product_name, brand=brand, quantity=quantity, amount=amount)
            return redirect('purchase') 
    purchase = Purchase.objects.all()
    return render(request, "purchase.html", {"purchase": purchase})

def edit_purchase(request, purchase_id):
    obj = Purchase.objects.get(id = purchase_id)
    if request.method == "POST":
        product_name = request.POST.get("product_name")
        brand = request.POST.get("brand")
        quantity = request.POST.get("quantity")
        amount = request.POST.get("amount")

        if product_name:
            obj.product_name = product_name
        if brand:
            obj.brand = brand
        if quantity:
            obj.quantity = quantity
        if amount:
            obj.amount = amount

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

        if product_name and customer and quantity and sale_price:
            try:
                product = Purchase.objects.get(product_name=product_name)
                
                Sales.objects.create(
                    product=product,  
                    customer=customer,  
                    quantity=quantity,
                    sale_price=sale_price
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
        if product_name:
            purchase_obj = Purchase.objects.get(product_name=product_name)
            obj.product = purchase_obj 
        if customer:
            obj.customer = customer

        if quantity:
            obj.quantity = quantity

        if sale_price:
            obj.sale_price = sale_price

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
    print(all_data)
    return render(request, "renew_member_list.html", {"all_data": all_data})



def renew_member_list(request):
    all_data = PersonalInformation.objects.filter(status='converted')  
    print(all_data)
    return render(request, "renew_member_list.html", {"all_data": all_data})


def renew_member_page(request, member_id):
    member = PersonalInformation.objects.get(id=member_id)

    if not member.services:
        messages.error(request, "This member does not have a service assigned.")
        return redirect("renew_member_list")

    if request.method == "POST":
        renew_date = request.POST.get("renew_date")
        payment_method = request.POST.get("payment_method")
        if renew_date:
            
            Renew.objects.create(
                name=member,
                service=member.services,  
                renew_date=renew_date,
                payment_method = payment_method,
            )
            messages.success(request, "Membership renewed successfully!")
            return redirect("renew_member_list")
        else:
            messages.error(request, "Please provide a valid renewal date.")

    return render(request, "renew_member_page.html", {"member": member})


def save_renewal_date(request, client_id):
    client = get_object_or_404(PersonalInformation, id=client_id)
    if request.method == 'POST':
        renewal_date = request.POST.get('renewal_date')
        client.renewal_date = renewal_date
        client.save()
        return redirect('some_success_page')  

    return render(request, 'renew_member_page.html', {'client': client})