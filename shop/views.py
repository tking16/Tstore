from django.views import generic
from .models import Shirt

class IndexView(generic.ListView):
	template_name = 'shop/index.html'
	context_object_name = 'all_shirts' # so we don't have to use 'object_list' when calling the variable
	
	def get_queryset(self):
		return Shirt.objects.all()	
	
class DetailView(generic.DetailView):
	model = Shirt
	template_name = 'shop/detail.html'
	