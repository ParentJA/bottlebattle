__author__ = 'parentj@eab.com (Jason Parent)'

# Django imports...
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Local imports...
from .forms import EventForm
from .models import Event


@login_required
def home_view(request):
    return render(request, 'app/home.html')


@login_required
def event_view(request):
    return render(request, 'app/event.html')


@login_required
def new_event_view(request):
    form = EventForm(request)

    if request.method == 'POST':
        form = EventForm(data=request.POST)

        if form.is_valid():
            form.save()

    return render(request, 'app/new_event.html', {
        'form': form
    })


@login_required
def event_detail_view(request, event_id):
    return render(request, 'app/event_detail.html', {
        'event': Event.objects.get(pk=event_id)
    })


@login_required
def event_list_view(request):
    return render(request, 'app/event_list.html')