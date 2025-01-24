from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import datetime

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    duration = models.CharField(max_length=50, null=True, blank=True)  
    prices = models.PositiveIntegerField(null=True, blank=True)

    

    def __str__(self):
        return self.name
    

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
    
    #status
    status = models.CharField(max_length=20, default='new')  # Track the status of the lead
    follow_up_date = models.DateTimeField(default=timezone.now)

    created_date = models.DateTimeField(default=timezone.now)

    #services

    services = models.ForeignKey(Service,on_delete=models.SET_NULL, null=True, related_name="users")   # for services
    assigned_date = models.DateField(default=timezone.now)
    renewal_date = models.DateField(null=True, blank=True)


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
    
class Expense(models.Model):
    expense_name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(null=True, blank=True)
    date_spent = models.DateTimeField(default = now  )  
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

    def __str__(self):
        return self.product_name
    
    def purchase(self):
        return{ "product_name":self.product_name,
               "brand" : self.brand,
               "quantity" : self.quantity,
               "amount" : self.amount

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
    sale_date = models.DateTimeField(auto_now_add=True)

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
    payment_method = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.renew_date


