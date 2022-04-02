from django.urls import path
from .views import UserProfileListView

urlpatterns = [
    path('', UserProfileListView.as_view(), name='user-profiles'),
]
