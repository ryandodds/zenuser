from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.template.defaultfilters import slugify
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

@login_required
def edit_interview(request, slug):
    # grab the object...
    interview = Interview.objects.get(slug=slug)
    if interview.user != request.user: 
        raise Http404
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

def create_interview(request):
    # request.user is the logged in user, we're going to assign it to "user" to make it easy
    user = request.user

    form_class = InterviewForm

    # if we're coming from a submitted form, do this
    if request.method == 'POST':
        # grab the data from the submitted form and apply to the form
        form = form_class(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            # create the slug from our name
            slug = slugify(name)

            # create our object
            interview = Interview.objects.create(
                name=name,
                description=description,
                slug=slug,
                user=user,
            )

        # redirect to our newly created thing
        return redirect('interview_detail', slug=interview.slug)

    # otherwise just create the form
    else:
        form = form_class()

    return render_to_response('interviews/create_interview.html', {
        'form': form,
    }, context_instance=RequestContext(request))