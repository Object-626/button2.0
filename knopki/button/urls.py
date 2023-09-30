from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('destroy', views.destroy, name='destroy'),
    path('crush', views.crush, name='crush'),
    path('exterminate', views.exterminate, name='exterminate'),
    path('overthrow', views.overthrow, name='overthrow'),
    path('enslave', views.enslave, name='enslave'),
    path('incinerate', views.incinerate, name='incinerate'),
    path('erase', views.erase, name='erase'),
    path('ruin', views.ruin, name='ruin'),
    path('broak', views.broak, name='broak'),
    path('suppress', views.suppress, name='suppress')
    ]
