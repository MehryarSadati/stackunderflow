from django.urls import path

from users.views import user_login_view, user_logout_view, user_profile_view, user_profile_edit_view, \
    user_register_view, user_home_view

app_name = 'users'
urlpatterns = [
    path('home/', user_home_view, name='home'),
    path('register/', user_register_view, name='register'),
    path('login/', user_login_view, name='login'),
    path('logout/', user_logout_view, name='logout'),
    path('profile/<int:uid>', user_profile_view, name='profile'),
    path('profile/edit/', user_profile_edit_view, name='profile_edit'),
]
