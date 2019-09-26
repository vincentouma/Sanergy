from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    url(r'^payment', views.payment, name='payment'),
    url('access/token', views.getAccessToken, name='get_mpesa_access_token'),

]