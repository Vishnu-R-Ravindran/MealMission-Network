from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('service/',views.service,name='service'),
    path('contact/',views.contact,name='contact'),
    path('profile_1/',views.hotel_profile,name='profile_1'), 
    path('home/',views.home,name='home'),
    path('coordinatoreg/',views.coordinatorreg,name='coordinatoreg'),
    path('coordinatorlogin/',views.coordinatorlogin,name='coordinatorlogin'),
    path('hotel/',views.hotelreg,name='hotel'),
    path('hotellogin/',views.hotellogin,name='hotellogin'),
    path('hotelhome/',views.hotelhome,name='hotelhome'),
    path('coordinatorhome/',views.coordinatorhome,name='coordinatorhome'),
    path('coordinatorprofile/',views.coordinatorprofile,name='coordinatorprofile'),
    path('coupdate/',views.coupdate,name='coupdate'),
    path('houpdate/',views.houpdate,name='houpdate'),
    path('logout/',views.logout,name='logout'),
    path('or/',views.orphanage_register,name='or'),
    path('ol/',views.orphanage_login,name='ol'),
    path('or_pro/',views.or_pro,name='or_pro'),
    path('o_h/',views.orp,name='o_h'), 
    path('adlogin/', views.adlogin, name='adlogin'),
    path('adhome/', views.view_donations, name='adhome'),
    path('adm/', views.adm, name='adm'),

    path('donate/', views.log_donation, name='donate'),



    path('available_donations/', views.view_available_donations, name='available_donations'),
    path('request_donation/<int:donation_id>/', views.request_donation, name='request_donation'),
   

    path('approve_and_assign/<int:donation_id>/', views.approve_and_assign_coordinator, name='approve_and_assign'),
    path('reject_donation/<int:donation_id>/', views.reject_donation, name='reject_donation'),

    path('coordinator_dashboard/', views.view_assigned_donations, name='view_assigned_donations'),
    path('mark_as_collected/<int:donation_id>/', views.mark_as_collected, name='mark_as_collected'),
    path('reject/<int:donation_id>/', views.reject, name='reject'),


    path('orphanage_dashboard/', views.view_collected_donations, name='view_collected_donations'),
    path('mark_as_received/<int:donation_id>/', views.mark_as_received, name='mark_as_received'),




    path('list/', views.list, name='list'),
    path('list1/<int:id>/', views.delete_orphanage, name='list1'),
    path('list2/', views.list2, name='list2'),
    path('deletehotel/<int:id>/', views.delete_hotel, name='list3'),

    path('list_1/', views.list_1, name='list_1'),
    path('list_2/<int:id>/', views.delete_co, name='list_2'),

    path('listx/', views.listx, name='listx'),
    path('listx1/<int:id>/', views.delete_d, name='listx1'),


    path('listy/', views.view_donationss, name='listy'),
    path('listy1/<int:id>/', views.delete_donation, name='listy1'),


    path('listz/', views.view_coordinator_donations, name='listz'),
    
    path('donation-status-chart/', views.donation_status_chart, name='donation_status_chart'),
    path('edit_or/', views.edit_or_pro, name='edit_or_pro'),


    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
    path('f_list/', views.f_list, name='f_list'),
    path('delete_feedback/<int:id>/', views.delete_feedback, name='delete_feedback'),

    # Coordinator paths
    path('coordinator-forgot-password/', views.coordinator_forgot_password, name='coordinator_forgot_password'),
    path('coordinator-reset-password/<str:token>/', views.coordinator_reset_password, name='coordinator_reset_password'),
    
    # Hotel paths
    path('hotel-forgot-password/', views.hotel_forgot_password, name='hotel_forgot_password'),
    path('hotel-reset-password/<str:token>/', views.hotel_reset_password, name='hotel_reset_password'),
    
    # Orphanage paths
    path('orphanage-forgot-password/', views.orphanage_forgot_password, name='orphanage_forgot_password'),
    path('orphanage-reset-password/<str:token>/', views.orphanage_reset_password, name='orphanage_reset_password'),

]

