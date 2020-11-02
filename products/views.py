from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView
from .models import Product
from carts.models import Cart


# Create your views here.
class ProductFeaturedListView(ListView):
    template_name = "products/templates/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.featured()


class ProductFeaturedDetailView(DetailView):
    # queryset = Product.objects.all()
    template_name = "products/templates/featured-detail.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.featured()


class ProductListView(ListView):
    template_name = "products/templates/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/templates/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context
    #   def get_context_data(self, *args, **kwargs):
    #     context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # instance = Product.objects.get_by_id(pk)
        try:
            instance = Product.objects.get(slug=slug)
        except Product.DoesNotExist:
            raise Http404("Not Found..")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug)
            instance = qs.first()
        except:
            raise Http404("Uhmmm")
        return instance
