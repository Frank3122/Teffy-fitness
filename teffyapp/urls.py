from teffyapp.views import *
from django.urls import path,include

urlpatterns = [
    path("", forms, name="forms"),
    path("main/", main, name="main"),
    path("expense/", expense, name="expense"),
    path("follow-up/", follow_up, name="follow_up"),
    path("plan/", plan, name="plan"),
    path('edit_plan/<int:plan_id>/', edit_plan, name='edit_plan'),
    path('assign_plan<int:id>/', assign_plan, name='assign_plan'),
    # path("price/", price, name="price"),
    path("work/", workplan, name="workplan"),
    path("personal/", personal_info_list, name="personal_information"),
    path("login/", user_login, name="login"),
    path("register/", register, name="register"),
    path("user_management/", user_management, name="user_management"),
    path("leads/<int:id>/", getone_lead, name="getone_lead"),
    # path("leads/add/",add_leads, name="add_leads"),
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
    # path('report/',report_view,name="report"),
    # path('edit-plan/<int:plan_id>/',edit_plan, name='edit-plan'),
    path('service/',services,name="services"),
    # path('manage_services/', manage_services, name='manage_services'),
    path('delete_service/<int:service_id>/',delete_service, name='delete_service'),
    path('assign-service/<int:id>/',assign_service, name='assign_service'),
    path('overall-services/',overall_services, name='overall_services'),
    path('payment/<int:client_id>/',payment, name='payment_page'),

    path('expenses/', expenses, name='expenses'),
    path('add-expense/', add_expense, name='add_expense'),
    path('delete_expenses/<int:expense_id>/', delete_expense, name='delete_expense'),
    path('expenses/<int:expense_id>/', view_expense, name='view_expense'),

    # path("datatables/",datatable,name="datatable"),
    path('purchase/', purchase, name="purchase"),
    path('edit-purchase/<int:purchase_id>/', edit_purchase, name="edit-purchase"),
    path('delete-purchase/<int:purchase_id>/', delete_purchase, name="delete-purchase"),

    path('sales/',sales,name="sales"),
    path('edit-sales/<int:sales_id>/', edit_sales, name="edit-sales"),
    path('delete-sales/<int:sales_id>/', delete_sales, name="delete-sales"),


    path('stocks/',stocks,name="stocks"),
    path('returns/',returns,name="returns"),

    path('report/',new_reports, name="new_reports"),

    # path('add_leads/',add_leads,name="add_leads"),

    path("renew-member/", renew_member_list, name="renew_member_list"),
    path("renew-member/<int:member_id>/", renew_member_page, name="renew_member_page"),

    path('add-member/',add_member, name="add_member"),

    path('display-add-members/',display_add_members, name='display_add_members'),
    path('display_add_members/<int:id>/',view_add_members, name="view_add_members"),
    path('delete_added_members/<int:id>/', delete_added_members, name="delete_added_members"),
    path('bill/', bill, name="bill"),

    path('view-all-clients/', view_all_clients, name="view_all_clients"),
    
    path("update-assigned-date/<int:id>/", update_assigned_date, name="update_assigned_date"),

    #  path('download_report/', download_report, name='download_report'),

    path('download-report/', download_report, name='download_report'),

    path('view_all_staffs/', view_all_staffs, name='view_all_staffs'),

    # path('members_list/',members_list, name="members_list"),

    # path('assign_service_plan/', assign_service_plan, name="assign_service_plan"),

    # path("assign_service_plan/<int:member_id>/", assign_service_plan, name="assign_service_plan"),

    # path('financial-summary/', financial_summary, name='financial_summary'),

    path("update_followup_date/<int:id>/", update_followup_date, name="update_followup_date"),

    # path('generate_invoice/<int:client_id>/', generate_invoice, name='generate_invoice'),

    # path('invoice/<int:member_id>/', generate_invoice, name='generate_invoice'),

    # path("invoice/download/<int:member_id>/", generate_invoice_pdf, name="generate_invoice_pdf"),

    path('update-payment/<int:member_id>/', update_member_payment, name='update_member_payment'),

    path('update-payment/<int:member_id>/', update_member_payment, name='update_member_payment'),
    path('view-member/<int:member_id>/', view_each_member, name='view_each_member'),  


    # path('download-invoice/<int:client_id>/', generate_invoice_pdf, name='generate_invoice_pdf'),

    # path("invoice/<int:client_id>/<str:client_type>/", generate_invoice, name="generate_invoice"),

    # Download Invoice as PDF
    # path("invoice/pdf/<int:client_id>/<str:client_type>/", generate_invoice_pdf, name="generate_invoice_pdf"),


     # ✅ View Invoice for Members
    # path("invoice/member/<int:member_id>/", generate_invoice_member, name="generate_invoice_member"),

    # ✅ Download Invoice PDF for Members
    # path("invoice/pdf/member/<int:member_id>/", generate_invoice_pdf_member, name="generate_invoice_pdf_member"),

    # path("invoice/member/<int:member_id>/", generate_invoice_member, name="generate_invoice_member"),
    # path("invoice/lead/<int:lead_id>/", generate_invoice_lead, name="generate_invoice_lead"),
    # path("invoice/pdf/<int:client_id>/<str:client_type>/", generate_invoice_pdf, name="generate_invoice_pdf"),

    path("invoice/pdf/member/<int:member_id>/", generate_invoice_pdf_member, name="generate_invoice_pdf_member"),
    path("invoice/pdf/lead/<int:lead_id>/", generate_invoice_pdf_lead, name="generate_invoice_pdf_lead"),

    path('plan/', plan, name='plan'),
    path('plan/edit/<int:plan_id>/', edit_plan, name='edit_plan'),
    path('plan/delete/<int:plan_id>/', delete_plan, name='delete_plan'),  # Delete URL
    
    path('todays-amount/', todays_amount, name='todays-amount'),
    path('total-amount/', total_amount, name="total-amount"),
]


    # path("invoice/lead/<int:lead_id>/", generate_invoice_lead, name="invoice_lead"),
    # path("invoice/member/<int:member_id>/", generate_invoice_member, name="invoice_member"),

    # path("invoice/lead/<int:lead_id>/", generate_invoice_lead, name="invoice_lead"),
    # path("invoice/member/<int:member_id>/", generate_invoice_member, name="invoice_member"),

    # Download Invoice as PDF
    # path("invoice/pdf/<int:client_id>/<str:client_type>/", generate_invoice_pdf, name="invoice_pdf"),

    # path("invoice/lead/<int:lead_id>/", generate_invoice_lead, name="invoice_lead"),
    # path("invoice/member/<int:member_id>/", generate_invoice_member, name="invoice_member"),
    # path("invoice/pdf/<int:client_id>/<str:client_type>/", generate_invoice_pdf, name="invoice_pdf"),

    # path("invoice/<int:client_id>/<str:client_type>/", generate_invoice, name="generate_invoice"),
    
    # # Download Invoice as PDF
    # path("invoice/pdf/<int:client_id>/<str:client_type>/", generate_invoice_pdf, name="generate_invoice_pdf"),

    # path("invoice/<int:client_id>/<str:client_type>/", generate_invoice, name="generate_invoice"),
    # path("invoice/pdf/<int:client_id>/<str:client_type>/", generate_invoice_pdf, name="generate_invoice_pdf"),


    # path("invoice/<int:client_id>/<str:client_type>/", generate_invoice, name="generate_invoice"),
    
    # # Download Invoice as PDF
    # path("invoice/pdf/<int:client_id>/<str:client_type>/", generate_invoice_pdf, name="generate_invoice_pdf"),

    # path("invoice/<int:client_id>/<str:client_type>/", generate_invoice, name="generate_invoice"),

    # # Download Invoice as PDF
    # path("invoice/pdf/<int:client_id>/<str:client_type>/", generate_invoice_pdf, name="generate_invoice_pdf"),

    # path("invoice/<int:client_id>/<str:client_type>/", generate_invoice, name="generate_invoice"),

    # # Download Invoice as PDF
    # path("invoice/pdf/<int:client_id>/<str:client_type>/", generate_invoice_pdf, name="generate_invoice_pdf"),




 



    # path('invoice/<int:client_id>/', generate_invoice_pdf, name='generate_invoice'),


    # path('pending-members/', pending_members_list, name='pending_members_list'),

    # path('pending-members/', pending_members_list, name='pending_members_list'),
    # path('add-payment/<int:member_id>/', add_payment, name='add_payment'),


#     path('pending-members/', pending_members_list, name='pending_members_list'),
#     # path('member-payment/<int:member_id>/', update_member_payment, name='member_payment_page'),

#     path('member-payment/<int:member_id>/', update_member_payment, name='member_payment_page'),





