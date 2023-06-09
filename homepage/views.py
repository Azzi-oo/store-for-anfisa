from django.shortcuts import render

from ice_cream.models import IceCream


def index(request):
    template = 'homepage/index.html'
    # Добавьте фильтрацию по полю is_publushed.
    ice_cream_list = IceCream.objects.filter(is_publushed=False).values('id', 'title', 'description')
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template, context)