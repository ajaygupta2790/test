from django.shortcuts import render

# Create your views here.
from .models import *
from restless.views import Endpoint

from restless.auth import BasicHttpAuthMixin, login_required
from restless.models import serialize

class InvoiceView(Endpoint):
	@login_required
	def get(self, request):
		context = {}
		try:
			invoice = Invoice.objects.all()
			if invoice.count():
				context['invoice'] = invoice
				return serialize(context, )
			else:
				context['error'] = 'Insufficient data'
		except:
			pass
		return context