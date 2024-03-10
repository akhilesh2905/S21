from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(Department)
admin.site.register(Doctor)

class BookingAdmin(admin.ModelAdmin):
    list_display=('p_name','p_phone','p_email','booking_date','booked_on')


admin.site.register(Booking,BookingAdmin)