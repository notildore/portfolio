from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about', views.about, name = 'about'),
    path('projects', views.projects, name = 'projects'),
    # path('certificates', views.certificates, name = 'certificates'),
    path('resume', views.resume, name='resume'),
    path('contact', views.contact, name = 'contact'),
]
