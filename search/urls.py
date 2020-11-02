
from django.urls import path

from django.conf.urls.static import static
from .views import (
        SearchProductView
        )

app_name = "search"
urlpatterns = [
    path('', SearchProductView.as_view(), name='query'),
#    path('featured/<slug:slug>/', ProductFeaturedDetailView.as_view()),

]
