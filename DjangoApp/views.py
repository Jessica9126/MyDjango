# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# # from .forms import InputForm
# from .forms import GeeksForm
# # importing formset_factory
# from django.forms import formset_factory

# # Create your views here.
# def index(request):
#   return HttpResponse("Hello Geeks!")

# Create your views here.
# def home_view(request):
#     context ={}
#     # context['form']= InputForm()
#     context['form']= GeeksForm()
#     print(request.POST)
#     return render(request, "home.html", context)

# def formset_view(request):
#     context ={}
  
#     # creating a formset
#     GeeksFormSet = formset_factory(GeeksForm, extra = 5)
#     formset = GeeksFormSet()
      
#     # Add the formset to context dictionary
#     context['formset']= formset
#     return render(request, "home.html", context)

# def formset_view(request):
#     context ={}
  
#     # creating a formset and 5 instances of GeeksForm
#     GeeksFormSet = formset_factory(GeeksForm, extra = 3)
#     formset = GeeksFormSet(request.POST or None)
      
#     # print formset data if it is valid
#     if formset.is_valid():
#         for form in formset:
#             print(form.cleaned_data)
              
#     # Add the formset to context dictionary
#     context['formset']= formset
#     return render(request, "home.html", context)

# def home_view(request):
#     context ={}
 
#     # create object of form
#     form = GeeksForm(request.POST or None, request.FILES or None)
#     # check if form data is valid
#     if form.is_valid():
#         # save the form data to model
#         form.save()
 
#     context['form']= form
#     return render(request, "home.html", context)

from django.shortcuts import get_object_or_404, render

# relative import of forms
from .models import GeeksModel
from .forms import GeeksForm


def create_view(request):
	# dictionary for initial data with
	# field names as keys
	context ={}

	# add the dictionary during initialization
	form = GeeksForm(request.POST or None)
    
	if form.is_valid():
		form.save()
	
	context['form']= form
	return render(request, "create_view.html", context)

def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = GeeksModel.objects.all()
         
    return render(request, "list_view.html", context)

# pass id attribute from urls
# def detail_view(request, id):
#     # dictionary for initial data with
#     # field names as keys
#     context ={}
 
#     # add the dictionary during initialization
#     context["data"] = GeeksModel.objects.get(id = id)
         
#     return render(request, "detail_view.html", context)

# after updating it will redirect to detail_View
def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
  
    # add the dictionary during initialization
    context["data"] = GeeksModel.objects.get(id = id)
          
    return render(request, "detail_view.html", context)
 
# update view for details
def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(GeeksModel, id = id)
 
    # pass the object as instance in form
    form = GeeksForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update_view.html", context)

# delete view for details
def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(GeeksModel, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")
 
    return render(request, "delete_view.html", context)
