
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from . import views







urlpatterns = [
    url(r'^$',views.index, name="homePage"),
    url(r'^payment', views.payment, name='payment'),
    url(r'^toilet', views.toilet, name='toilet'),
    url('access/token', views.getAccessToken, name='get_mpesa_access_token'),
    url('online/lipa', views.lipa_na_mpesa_online, name='lipa_na_mpesa'),
    url(r'^api/payment/$', views.PaymentList.as_view()),
    url(r'^confirmation/$', views.confirmation, name='confrimation'),
    url(r'^bills',views.bills,name='bills'),
    url(r'^search/', views.search_results, name='search_results'),

    #API'S
    url(r'^api/bills/', views.BillsList.as_view()),
    url(r'^all_customer_bills/', views.all_customer_bills, name='all_customer_bills'),



 #profile
    # url(r'^my-profile/',views.my_profile, name='my-profile'),
    # url(r'^user/(?P<username>\w{0,50})',views.user_profile,name='user-profile'),
    # url(r'^create/profile$',views.create_profile, name='create-profile'),
    # url(r'^update/profile$',views.update_profile, name='update-profile'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 