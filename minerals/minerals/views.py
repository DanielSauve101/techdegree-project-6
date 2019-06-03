from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from rocks.models import Minerals

# Create your views here.


def mineral_list(request):
    """View to show the mineral list using Paginator to limit 45 per page"""
    mineral_list = Minerals.objects.all()
    paginator = Paginator(mineral_list, 45)
    page = request.GET.get('page')
    minerals = paginator.get_page(page)
    return render(request, 'mineral_list.html', {'minerals': minerals})
