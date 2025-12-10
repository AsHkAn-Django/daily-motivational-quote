from . import views
from django.urls import path


urlpatterns = [
    path('quotes/', views.QuoteList.as_view(), name='quote-list'),
    path('quote-detail/<int:pk>/', views.QuoteDetail.as_view(), name='quote-detail'),
]