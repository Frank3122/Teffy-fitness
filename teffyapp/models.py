from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    duration = models.CharField(max_length=50, null=True, blank=True)  # Optional field for service details
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

    created_date = models.DateTimeField(default=timezone.now)

    #services

    services = models.ForeignKey(Service,on_delete=models.SET_NULL, null=True, related_name="users")   # for services

    

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
class UserProfile(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    profile_user_id = models.CharField(max_length=100, unique=True)
    group = models.CharField(max_length=50, null=True, blank=True)
    


    def __str__(self):
        return str(self.id)

class Sales(models.Model):
    sales = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sales
    
class Purchase(models.Model):
    purchase = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.purchase



class Plan(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    batch = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
