from teffyapp.views import *
from django.urls import path,include

urlpatterns = [
    path("", forms, name="forms"),
    path("main/", main, name="main"),
    path("expense/", expense, name="expense"),
    path("follow-up/", follow_up, name="follow_up"),
    path("plan/", plan, name="plan"),
    path("price/", price, name="price"),
    path("work/", workplan, name="workplan"),
    path("personal/", personal_info_list, name="personal_information"),
    path("login/", user_login, name="login"),
    path("register/", register, name="register"),
    path("user_management/", user_management, name="user_management"),
    path("leads/<int:id>/", getone_lead, name="getone_lead"),
    path("leads/new/", new_leads, name="new_leads"),
    path("leads/converted/", converted_leads, name="converted_leads"),
    path("leads/not_converted/", not_converted_leads, name="not_converted_leads"),
    path("leads/pending/", pending_leads, name="pending_leads"),
    path("leads/follow_up/", follow_up_leads, name="follow_up_leads"),
    path("leads/update-status/<int:id>/", update_status, name="update_status"),
    path("leads/delete/<int:id>/", delete_lead, name="delete_lead"),
    path("logout/", user_logout, name="logout"),
    path("edit_user/<str:user_id>/", edit_user, name="edit_user"),
    path('delete_user/<str:user_id>/',delete_user, name='delete_user'),
]