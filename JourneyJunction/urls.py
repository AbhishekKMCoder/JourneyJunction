from django.urls import path
from TravelApp import urls
from JourneyJunction import views
# from django.urls import path
# from . import views
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    # Core pages
    path('index/', views.html_pag, name="index"),
    path('about/', views.about_pag, name="about"),
    path('contact/', views.contact_pag, name="contact"),

    # Tour and hotel pages
    path('tour/', views.tour_pag, name="tour"),
    path('tour/<int:tour_id>/', views.Single_tour_detail, name='single_tour_detail'),  # Single tour detail
    path('tour_single/', views.tour_single_pag, name="tour_single"),
    path('hotel/', views.hotel_pag, name="hotel"),
    path('hotel_single/', views.hotel_single_pag, name="hotel_single"),

    # Blog
    path('blog/', views.blog_pag, name="blog"),

    # Authentication pages
    path('', views.Loginpage, name="login"),
    path('sign/', views.Sign_page, name="sign"),
    path('signup/', views.signup_view, name="signup"),
    path('user_login/', views.User_login, name="user_login"),
    path('logout/', views.User_logout, name='logout'),

    # New view example
    path("new/", views.new_fun, name="new"),

    # razorpay
    path('book-tour/', views.booking_form, name='booking_form'),

    path('payment_page/',views.payment_page,name='payment_page'),

    path('save_user_profile/',views.save_user_profile,name='save_user_profile'),

    path('contact_save/',views.contact_save,name='contact_save')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
