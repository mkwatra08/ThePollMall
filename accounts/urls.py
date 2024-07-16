from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView  # Ensure this import is present

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
]
