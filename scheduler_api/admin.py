from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Timeslot)
admin.site.register(Class)
admin.site.register(Section)
admin.site.register(Room)
admin.site.register(Timetable)