from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.utils import timezone
import calendar
from django.db.models import Sum
from datetime import timedelta
# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=100)
    duration = models.CharField(max_length=50, null=True, blank=True)  
    prices = models.PositiveIntegerField(null=True, blank=True)
    group = models.CharField(max_length=100, null=True, blank=True)
    sessions = models.CharField(max_length=100,null=True, blank=True)

    def __str__(self):
        return self.name
    
class Plan(models.Model):
    plan_name = models.CharField(max_length=100,null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    batch = models.CharField(max_length=50,null=True, blank=True )
    duration = models.CharField(max_length=50, null=True, blank=True) 

    def __str__(self):
        return self.plan_name
    
    def plan(self):
        return {"plan_name":self.plan_name,
                "price" : self.price,
                "batch" : self.batch,
                "duration":self.duration,
                "id": self.id,  # Include the id
        }
    
    #1st page
class PersonalInformation(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    occupation = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    mobile_number = models.CharField(max_length=12)
    email = models.EmailField()

    #2nd page
    perfect_body = models.CharField(max_length=20,null=True,blank=True)
    body_type=models.CharField(max_length=20,null=True,blank=True)
    goal=models.CharField(max_length=30,null=True,blank=True)

    #3rd page
    body_you_want = models.CharField(max_length=50, null=True,blank=True)
    level_of_body_fat = models.CharField(max_length=50,null=True,blank=True)
    problem_areas = models.CharField(max_length=50,null=True,blank=True)

    #4th page
    diets = models.CharField(max_length=70,null=True,blank=True)
    water_you_drink_daily = models.CharField(max_length=50,null=True,blank=True)
    eat_or_dividie_foods_or_beverages = models.CharField(max_length=70,blank=True,null=True)

    #5th page
    # programe = models.CharField(max_length=50,null=True,blank=True)
    event_coming_up = models.CharField(max_length=50,null=True,blank=True)
    height = models.CharField(max_length=50)
    current_weight = models.CharField(max_length=50)
    target_weight = models.CharField(max_length=50)
    level_of_fitness = models.CharField(max_length=50,null=True,blank=True)

    reason = models.TextField(blank=True, null=True)  # New field for pending reason
    
    #status
    status = models.CharField(max_length=20, default='new')  # Track the status of the lead
    follow_up_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(default=timezone.now)


    services = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, related_name="users")
    assigned_date = models.DateField(default=timezone.now)
    renewal_date = models.DateField(null=True, blank=True)
    

    # plans assigned
    plan_leads = models.ForeignKey(to=Plan, on_delete=models.SET_NULL, null=True, related_name="plan_leads")

    # converted_member = models.OneToOneField('AddMember', null=True, blank=True, on_delete=models.SET_NULL, related_name='converted_from_lead')
    # conversion_date = models.DateTimeField(null=True, blank=True)


    
    # reports

    # report = models.ForeignKey(Report, on_delete=models.SET_NULL, null=True, blank=True, related_name='leads')

    

    def __str__(self):
        return self.name
    
    def gym(self):
        return {"name":self.name,
                "address":self.address,
                "occupation":self.occupation,
                "gender":self.gender,
                "mobile_number":self.mobile_number,
                "email":self.email,
                "perfect_body":self.perfect_body,
                "body_type":self.body_type,
                "goal":self.goal,
                "body_you_want":self.body_you_want,
                "level_of_body_fat":self.level_of_body_fat,
                "problem_areas":self.problem_areas,
                "diets":self.diets,
                "water_you_drink_daily":self.water_you_drink_daily,
                "eat_or_dividie_foods_or_beverages":self.eat_or_dividie_foods_or_beverages,
                "event_coming_up":self.event_coming_up,
                "height":self.height,
                "current_weight":self.current_weight,
                "target_weight":self.target_weight,
                "level_of_fitness":self.level_of_fitness,
                "status":self.status,  
        }
    


class Report(models.Model):
    from_date = models.DateField()
    to_date = models.DateField()
    status = models.ForeignKey(to=PersonalInformation,on_delete=models.SET_NULL, null=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.from_date




class UserProfile(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    profile_user_id = models.CharField(max_length=100, unique=True)
    group = models.CharField(max_length=50, null=True, blank=True)
    


    def __str__(self):
        return str(self.id)


    
class Expense(models.Model):
    expense_name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(null=True, blank=True)
    date_spent = models.DateField(default = now  )  
    quantity = models.PositiveIntegerField(null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.expense_name
    
    def expense(self):
        return {"expense_name":self.expense_name,
                "price" : self.price,
                "date_spent" : self.date_spent,
                
        }

class Payments(models.Model):
    payments = models.ForeignKey(to=PersonalInformation, on_delete=models.SET_NULL, null=True, related_name="payment_records" )
    name = models.ForeignKey(to=PersonalInformation, on_delete=models.SET_NULL, null=True, related_name='name_records')
    amount_paid = models.PositiveIntegerField(null=True, blank=True)
    pending_amount = models.PositiveIntegerField(null=True, blank=True)
    payment_mode = models.CharField(max_length=50, null=True, blank=True)
    date_paid = models.DateTimeField(default = now ) 
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name.name if self.name else 'No Name'} - Amount Paid: {self.amount_paid}"
    

class Purchase(models.Model):
    product_name = models.CharField(max_length=100, null=True, blank=True)
    brand = models.CharField(max_length=50, null=True, blank=True)
    quantity = models.IntegerField()
    amount = models.FloatField(null=True, blank=True)
    purchase_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.product_name
    
    def purchase(self):
        return{ "product_name":self.product_name,
               "brand" : self.brand,
               "quantity" : self.quantity,
               "amount" : self.amount,
               "purchase_date": self.purchase_date,
             


        }
    
class Stock(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name='stocks',default=1)
    product_name = models.CharField(max_length=100, null=True, blank=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.purchase.product_name
    
class Sales(models.Model):
    product = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name='sales', default=1)
    product_name = models.CharField(max_length=100, null=True, blank=True)
    customer = models.CharField(max_length=50,null=True, blank=True)
    quantity = models.IntegerField()
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    sale_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product.product_name  


class Returns(models.Model):
    product = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name='returns')
    product_name = models.CharField(max_length=100, null=True, blank=True)
    customer = models.CharField(max_length=50,null=True, blank=True)
    quantity = models.IntegerField()
    reason = models.TextField(null=True, blank=True)
    return_date = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return self.product.product_name  

class Renew(models.Model):
    name = models.ForeignKey(to=PersonalInformation, on_delete=models.SET_NULL,null=True)
    service = models.ForeignKey(to=Service, on_delete=models.SET_NULL, null=True)
    renew_date = models.DateField()
    expiry_date = models.DateField(null=True, blank=True)
    payment_method = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.renew_date

class AddMember(models.Model):
    name = models.CharField(max_length=45, null=True, blank=True)
    gender = models.CharField(max_length=10)
    mobile_number = models.CharField(max_length=12, null=True, blank=True)
    aadhar_number  = models.CharField(max_length=16, unique=True ,null=True)
    uploaded_file = models.FileField(upload_to='member_files/', blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=30, null=True, blank=True)
    source = models.CharField(max_length=50, null=True, blank=True)
    occupation = models.CharField(max_length=50, null=True, blank=True)
    emergency_number = models.CharField(max_length=12, null=True, blank=True)
    registration_amount = models.FloatField(null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, related_name='members_by_service')
    batch = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, related_name='batch_members')
    cost_of_plan = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, related_name='cost_of_plan_members')
    total_session = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, related_name='total_session_members')
    conveniance_fees = models.FloatField(null=True, blank=True)
    total_amount = models.FloatField(null=True, blank=True)
    enrollment_date = models.DateField(null=True, blank=True)
    activation_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    current_installment_amount = models.FloatField(null=True, blank=True)
    payment_mode = models.CharField(max_length=50, null=True, blank=True)
    payment_date = models.DateField(null=True, blank=True)
    sold_by = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    discount = models.FloatField(null=True, blank=True)  
    discount_type = models.CharField(max_length=50, null=True, blank=True)  
    select_membership_plan = models.ForeignKey(to=Plan, on_delete=models.CASCADE, null=True, blank=True)
    
    def pending_amount(self):
        """Calculate pending amount dynamically"""
        return max(self.total_amount - self.current_installment_amount, 0)

    def payment_status(self):
        """Check if fully paid"""
        return "Paid" if self.pending_amount() == 0 else "Pending"

    def __str__(self):
        return self.name
    
    def member(self):
        return{"uploaded_file":self.uploaded_file,
               "discount":self.discount,
               "discount_type": self.discount_type,
               "sold_by" : self.sold_by,
               "payment_date" : self.payment_date,
               " current_installment_amount" : self.current_installment_amount,
               "expiry_date":self.expiry_date,
               "activation_date":self.activation_date,
               "enrollment_date":self.enrollment_date,
               "total_amount":self.total_amount,
               "conveniance_fees": self.conveniance_fees,
            #    "discount_on_plan":self.discount_on_plan,
               "total_session":self.total_session,
               "batch":self.batch,
               "service":self.service,
               "registration_amount":self.registration_amount,
               "emergency_number":self.emergency_number,
               "occupation":self.occupation,
               "source":self.source,
               "location":self.location,
               "date_of_birth":self.date_of_birth,
               "email":self.email,
               "aadhar_number":self.aadhar_number,
                "mobile_number":self.mobile_number,
                "gender":self.gender,
                "name":self.name,
                "cost_of_plan":self.cost_of_plan,
                "select_membership_plan":self.select_membership_plan,

 

        }


class MemberPayment(models.Model):
    member = models.ForeignKey("AddMember", on_delete=models.CASCADE, related_name="payments")
    amount_paid = models.FloatField(default=0)
    pending_amount = models.FloatField(default=0)
    payment_mode = models.CharField(max_length=50, choices=[
        ("Cash", "Cash"),
        ("Card", "Card"),
        ("Online Transfer", "Online Transfer"),
    ])
    payment_date = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.member.name} - ₹{self.amount_paid} (Pending: ₹{self.pending_amount})"

    def save(self, *args, **kwargs):
        """Auto-update pending amount when saving."""
        total_paid = sum(payment.amount_paid for payment in MemberPayment.objects.filter(member=self.member))
        self.pending_amount = self.member.total_amount - total_paid
        super().save(*args, **kwargs)