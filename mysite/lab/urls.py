from django.conf.urls import url

from . import views

app_name = 'lab'
urlpatterns = [
    # url(r'^$', views.item000, name='index'),
    url(r'^labpower/', views.labpower, name='labpower'),
    url(r'^labinfo/', views.labinfo, name='labinfo'),
    url(r'^labteacher/', views.labteacher, name='labteacher'),
    url(r'^labstudent/', views.labstudent, name='labstudent'),
    url(r'^labtest/', views.labtest, name='labtest'),
    url(r'^prj_spec/', views.prj_spec, name='prj_spec'),
]