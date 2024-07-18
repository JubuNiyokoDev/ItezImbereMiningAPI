from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UsersListCreate.as_view(), name='users-list-create'),
    path('users/<int:pk>/', views.UsersDetail.as_view(), name='users-detail'),
    path('register/', views.RegisterAPIView.as_view(), name='register'),
    path('login/', views.CustomAuthToken.as_view(), name='login'),
    path('api-token-auth/', views.CustomAuthToken.as_view(), name='api_token_auth'),
    path('profile/<int:pk>/', views.UserProfileDetail.as_view(), name='user-profile-detail'),
]
