from django.shortcuts import render,redirect
from django.views import View
from shop.models import Product_model
from django.db.models import Q



class Search(View):
    def get(self, request):
        query = request.GET.get('p', '')
        result = Product_model.objects.filter(Q(name__icontains=query) |
                                              Q(descriptions__icontains=query) |
                                              Q(category__name__icontains=query))
        return render(request, 'search.html', {'result': result, 'query': query})

