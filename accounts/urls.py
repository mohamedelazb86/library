from django.urls import path
from . import views

app_name='accounts'


urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('activate_code',views.actiavte_code,name='activate-code'),

    
]
