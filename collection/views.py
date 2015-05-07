from django.shortcuts import render
from collection.models import interview

# Create your views here.
def index(request):
	interviews = interview.objects.all()
	return render(request, 'index.html', {
		'interviews': interviews,
	})	

def interview_detail(request, slug):
	# grab the object...
	interviews = interview.objects.get(slug=slug)
	# and pass to the template
	return render(request, 'interviews/interview_detail.html', { 
		'interview': interview,
	})