from django.contrib import admin

from collection.models import interview

# set up automated slug creation
class InterviewAdmin(admin.ModelAdmin): 
	model = interview
	list_display = ('name', 'description',) 
	prepopulated_fields = {'slug': ('name',)}

# Register your models here.
admin.site.register(interview, InterviewAdmin)