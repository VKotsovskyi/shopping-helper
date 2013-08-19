from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from models import Product, ShoppingList
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from django.views.generic import ListView

@login_required
def index(request):
    list1=Product.objects.all()
    list2 = ShoppingList.objects.all()
    context = {'listproduct':list1 , 'shoppinglist':list2}
    return TemplateResponse(request, 'main/index.html', context)


#def current_list(request):
#    list2 = ShoppingList.objects.all()
#    context = {'shoppinglist': list2}
#    return TemplateResponse(request, 'main/index.html', context)


