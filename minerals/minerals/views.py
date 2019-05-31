from django.shortcuts import get_object_or_404, render

from rocks.models import Minerals

# Create your views here.


def mineral_list(request):
    minerals = Minerals.objects.all()
    return render(request, 'mineral_list.html', {'minerals': minerals})
