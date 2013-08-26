from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from models import Product, ShoppingList, Dashboard, Category
from django import forms
from django.views.decorators.csrf import csrf_exempt
from datetime import date
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse


@csrf_exempt
@login_required
def index(request):
    a = ""
    list1=Product.objects.all()
    user=request.user # define who is logged in
    curr_dashboard = request.user.get_dashboard()
    curr_buylist = ShoppingList.objects.filter(dashboard = curr_dashboard)
    print unicode(curr_dashboard)
    if request.is_ajax():
        a = request.POST['to_delete']
        #Product.objects.all(name = a).delete()
    print Product.name
#    if request.POST:
#        name = request.POST['name']
#        age = request.POST['age']
#        print name
#        print age
# Validation for adding product form
    if request.method == 'POST': # If the form has been submitted...
        form = AddForm(request.POST) # A form bound to the POST datas
        if form.is_valid(): # All validation rules pass
            obj = form.save(commit=False)
            obj.dashboard = curr_dashboard
            obj.save()
            curr_buylist[0].add_product(obj.id)
            return HttpResponseRedirect(request.get_full_path()) # Redirect after POST
    else:
        form = AddForm() # An unbound form

    context = {'listproduct': list1 ,
               'currUserDashboard': curr_dashboard,
               'currBuyList': curr_buylist,
               'user': user,
               'form': form}
    return TemplateResponse(request, 'main/index.html', context)


class AddForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'price', 'category',)

