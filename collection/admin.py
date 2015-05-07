from django.contrib import admin

from collection.models import Interview

# set up automated slug creation
class InterviewAdmin(admin.ModelAdmin): 
	model = Interview
	list_display = ('name', 'description',) 
	prepopulated_fields = {'slug': ('name',)}

# Register your models here.
admin.site.register(Interview, InterviewAdmin)