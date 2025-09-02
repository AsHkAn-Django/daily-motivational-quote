from django.urls import path
from .views import IndexView, QuoteListView, QuoteDetailView, QuoteUpdateView, QuoteDeleteView, QuoteCreateView, SignUpView

urlpatterns = [
    path('quote/quote_delete/<int:pk>/', QuoteDeleteView.as_view(), name='quote_delete'),
    path('quote/quote_edit/<int:pk>/', QuoteUpdateView.as_view(), name='quote_edit'),
    path('quote/quote_detail/<int:pk>/', QuoteDetailView.as_view(), name='quote_detail'),
    path('quote/quote_new/', QuoteCreateView.as_view(), name='quote_new'),
    path('quote/quote_list/', QuoteListView.as_view(), name='quote_list'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', IndexView.as_view(), name='home'),
]

