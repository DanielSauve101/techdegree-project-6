from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render

from .models import Mineral


def mineral_list(request):
    """View to show the mineral list using Paginator to limit 45 per page"""
    mineral_list = Mineral.objects.all()
    paginator = Paginator(mineral_list, 45)
    page = request.GET.get('page')
    minerals = paginator.get_page(page)
    return render(request, 'rocks/mineral_list.html', {'minerals': minerals})


def mineral_detail(request, pk):
    mineral = Mineral.objects.filter(pk=pk).values()
    important_details_dict = {}
    other_details_dict = {}
    for elements in mineral:
        for key, value in elements.items():
            if key != 'id':
                if (key == 'name' or key == 'image_filename' or key == 'image_caption'):
                    important_details_dict.update({key: value})
                else:
                    if value:
                        other_details_dict.update({key: value})
    return render(request, 'rocks/mineral_detail.html',
                  {'important': important_details_dict,
                   'other': other_details_dict})
