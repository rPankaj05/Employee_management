from django.contrib import admin

# Register your models here.
from empApp.models import Emp,Feedback

class EmpAdmin(admin.ModelAdmin):
    list_display=('name','working','emp_id','phone','department')
    list_editable=('working','emp_id')
    search_fields=('emp_id','name','phone' )
    list_filter=('working',)
admin.site.register(Emp,EmpAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','desc','date')
admin.site.register(Feedback,FeedbackAdmin)

