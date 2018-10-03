from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.slpu, name='slpu'),
    re_path(r'^(?P<glpuid>[\w]{6})/$', views.glpu_data, name='glpu_data'),
    re_path(r'^(?P<glpuid>[\w]{6})/(?P<mcodid>[\w]{6})/$', views.infomcod, name='infomcod'),
    re_path(r'^(?P<glpuid>[\w]{6})/period/(?P<period>[\d]{6})/$', views.eksp, name='eksp'),
]
