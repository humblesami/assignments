from django.urls import path
from .views import UserProfileListView, UserProfileDetailView

urlpatterns = [
    path('', UserProfileListView.as_view(), name='user-profiles'),
    path('<int:pk>/', UserProfileDetailView.as_view(), name='user-profiles'),
]
