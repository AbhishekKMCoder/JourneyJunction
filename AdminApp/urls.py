from django.urls import path
from AdminApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("index1/", views.index1_page, name="index1"),
    path("", views.index_page, name="index2"),
    path("add_package/", views.add_package_pag, name="add_package"),
    path("display/",views.display_package_page, name="display"),
    path("add_tour/",views.add_tour_destination, name= "add_tour"),
    path("display_package/", views.display_package_page, name="display_package"),
    path("edit_package/<int:des_id>", views.edit_package_page, name="edit_package"),
    path("update_package/<int:des_id>", views.update_package_page, name="update_package"),
    path("delete_package/<int:des_id>", views.delete_package_page, name="delete_package"),

    path('add-hotel/', views.add_hotel_packages_page, name='add_hotel_packages_page'),
    path('add-hotels/', views.add_hotels_list, name='add_hotels_list'),
    path('display-hotels/', views.display_hotel_page, name='display_hotel_page'),
    path('update-hotel/<int:hot_id>/', views.update_hotels_list, name='update_hotels_list'),
    path('delete-hotel/<int:hot_id>/', views.delete_hotel_list, name='delete_hotel_list'),
    path('view_contact_messages/', views.view_contact_messages, name='view_contact_messages')

]


