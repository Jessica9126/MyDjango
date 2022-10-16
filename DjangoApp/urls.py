import imp
import py_compile
from django.contrib import admin
# from Scripts.MyDjango.MyDjango.views import index
from django.urls import path
#now import the views.py file into this code
from . import views
# from .views import home_view
#from .views import formset_view

urlpatterns=[
  path('', views.list_view, name= "view"),
  path('create/', views.create_view, name="create"),
  # path('home/', home_view),
  path('admin/', admin.site.urls),
  path('<id>', views.detail_view ),
  path('<id>/delete', views.delete_view, name="delete"),
  path('<id>/update', views.update_view, name="update"),
  #path('formset/', formset_view),
]

