from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.info,name='force'),
    path('warmup/',views.pretest),
    path('Energy_1/',views.energy),
    path('Post/',views.posttest),
    path('Complete/',views.complete),
]