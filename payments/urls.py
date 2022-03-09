from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('success/', views.payment_success),
    path('cancelled/', views.payment_cancel),
    path('webhook/', views.stripe_webhook), # new
]