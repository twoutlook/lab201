from django.conf.urls import url

from . import views

app_name = 'lab'
urlpatterns = [
    # url(r'^$', views.item000, name='index'),
    url(r'^labpower/', views.labpower, name='labpower'),
    url(r'^info/', views.info, name='info'),
    url(r'^teacher/', views.teacher, name='teacher'),
    url(r'^student/', views.student, name='student'),
    url(r'^labtest/', views.labtest, name='labtest'),
    url(r'^prj_spec/', views.prj_spec, name='prj_spec'),
]