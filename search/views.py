from django.shortcuts import render
from products.models import Product
from django.views.generic import ListView

class SearchProductView(ListView):
    template_name = "search/templates/view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        if query is not None:
            return Product.objects.filter(title__icontains=query)
        return Product.objects.none()
        '''
        __icontains = field contains this
        --iexact = field is exact
        '''