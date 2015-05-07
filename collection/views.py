from django.shortcuts import render
from collection.models import interview

# Create your views here.
def index(request):
	interviews = interview.objects.all()
	return render(request, 'index.html', {
		'interviews': interviews,
	})