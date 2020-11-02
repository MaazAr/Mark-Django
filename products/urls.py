
from django.urls import path

from django.conf.urls.static import static
from products.views import (
    ProductListView,
    ProductDetailView,
   # ProductFeaturedDetailView,
   # ProductFeaturedListView,
    )

app_name = "products"
urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='detail'),
#    path('featured/<slug:slug>/', ProductFeaturedDetailView.as_view()),

]
