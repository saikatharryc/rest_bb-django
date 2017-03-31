from django.http import Http404
from django.shortcuts import render
from .models import Organizations
# Create your views here.


def index(request):
    all_org = Organizations.objects.all()
    return render(request, 'organizations/index.html', {'all_org': all_org})


def detail(request, org_id):
    try:
        org = Organizations.objects.get(pk=org_id)
    except Organizations.DoesNotExist:
        raise Http404("Organization Does Not exist")

    return render(request, 'organizations/details.html', {'org': org})
