from django.urls import  path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('calculator/', calculator, name='calculator'),
    path('form/',form,name="form"),
    path('',login_page,name='login'),
    path('register/',register_page,name='register'),
    path('homepage/',homepage,name= 'homepage'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)