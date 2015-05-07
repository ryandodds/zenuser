from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from collection.models import Interview
from collection.forms import InterviewForm

# the rewritten view!
def index(request):
    interviews = Interview.objects.all()
    return render_to_response('index.html', {
        'interviews': interviews,
    }, context_instance=RequestContext(request))

def interview_detail(request, slug):
    # grab the object...
    interview = Interview.objects.get(slug=slug)
    # and pass to the template
    return render_to_response('interviews/interview_detail.html', {
        'interview': interview,
    }, context_instance=RequestContext(request))

def edit_interview(request, slug):
    # grab the object...
    interview = Interview.objects.get(slug=slug)
    # set the form we're using...
    form_class = InterviewForm

    # if we're coming to this view from a submitted form,  
    if request.method == 'POST':
        # grab the data from the submitted form
        form = form_class(data=request.POST, instance=interview)
        if form.is_valid():
            # save the new data
            form.save()
            return redirect('interview_detail', slug=interview.slug)
    # otherwise just create the form
    else:
        form = form_class(instance=interview)

    # and render the template
    return render_to_response('interviews/edit_interview.html', {
        'interview': interview,
        'form': form,
    }, context_instance=RequestContext(request))