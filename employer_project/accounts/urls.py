from django.urls import path
from .views import SignUpView, LoginView, ProfileView,LogoutView

urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('logout/', LogoutView.as_view(), name='logout'),
]
