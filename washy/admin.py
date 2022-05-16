from django.contrib import admin
from washy.models import washingmachine

class WashyAdmin(admin.ModelAdmin):
    list_display=('name','room_no','start_time','end_time')

admin.site.register(washingmachine,WashyAdmin)


# Register your models here.



