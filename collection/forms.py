from django.forms import ModelForm 
from collection.models import Interview


class InterviewForm(ModelForm): 
	class Meta:
		model = Interview
		fields = ('name', 'description', 'due_date')