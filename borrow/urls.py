from django.urls import path
from .views import CheckoutBookView, ReturnBookView

urlpatterns = [
    path('checkout/', CheckoutBookView.as_view()),
    path('return/', ReturnBookView.as_view()),
]