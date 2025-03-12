from django.urls import path
from .import views 
from .views import home_view, signup_view, login_view, cafe_setup_view

app_name = 'cafeCritics'

urlpatterns = [
    path('', home_view, name='home_page'),
    path('cafes/', views.cafes_view, name='cafes'),
    path('about/', views.about_view, name='about'),
    path('accountsettings/', views.account_settings_view, name='account_settings'),
    path('cafes/<slug:cafe_name_slug>/', views.show_cafe, name='show_cafe'),
    path('cafes/<slug:cafe_name_slug>/review', views.review_view, name='review'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('cafe_setup/', cafe_setup_view, name='cafe_setup'),
]
