from django.conf.urls import url

from . import views

app_name = 'lab'
urlpatterns = [
    # url(r'^$', views.item000, name='index'),
    url(r'^power/', views.power, name='power'),
]