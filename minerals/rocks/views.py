from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import Mineral


def mineral_list(request):
    """View to show the mineral list using Paginator to limit 45 per page"""
    mineral_list = Mineral.objects.all()
    paginator = Paginator(mineral_list, 45)
    page = request.GET.get('page')
    minerals = paginator.get_page(page)
    return render(request, 'rocks/mineral_list.html', {'minerals': minerals})


def mineral_detail(request, pk):
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, 'rocks/mineral_detail.html', {'mineral': mineral})
