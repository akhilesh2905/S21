from django.urls import path
from .import views 

urlpatterns = [
    path('',views.index,name='home'),
    path('about/',views.about,name='about'),
    path('booking/',views.booking,name='booking'),
    path('doctors/',views.doctors,name='doctors'),
    path('contact/',views.contact,name='contact'),
    path('login/', views.login, name='login'),
     path("checkadminlogin",views.checkadminlogin,name="checkadminlogin"),
    path('logout/', views.logout, name='logout'),
    path('department/',views.department,name='department'),

]