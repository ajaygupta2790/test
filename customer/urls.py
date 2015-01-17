from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
	url(r'^invoices/', InvoiceView.as_view(), name='home'),

)
