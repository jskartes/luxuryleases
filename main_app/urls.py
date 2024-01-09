from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('cars/',views.cars_index, name='cars_index'),
    path('cars/<int:car_id>/', views.cars_detail, name='cars_detail'),
    path('rentals/new', views.rentals_new,name='rentals_new'),
    path('rentals/create', views.rentals_create, name='rentals_create'),
    path('rentals/<int:car_id>/create', views.rentals_car, name='quick_car'),
    path('rentals/<int:rental_id>', views.rentals_detail, name='rentals_detail'),
    path('rentals/<int:rental_id>/edit', views.rentals_edit, name='rentals_edit'),
    path('rentals/<int:rental_id>/update', views.rentals_update, name='rentals_update'),
    path('rentals/<int:pk>/delete', views.RentalDelete.as_view(), name='rentals_delete'),
    path('stores/', views.stores_index, name='stores_index'),
    path('stores/select/<int:store_id>/', views.select_store, name='select_store'),
    path('users/login', views.users_login, name='users_login'),
    path('users/<int:user_id>/', views.users_detail, name='users_detail'),
    path('administrator/', views.admin_page,name='admin'),
    path('administrator/addcar', views.add_car,name='add_car'),
    path('administrator/addstore', views.add_store, name='add_store'),
    # path('cars/editcar', views.edit_car, name='edit_car'),
    # path('cars/updatecar', views.update_car, name='update_car'),
    path('cars/<int:car_id>/editcar', views.edit_car, name='edit_car'),
    path('cars/<int:car_id>/updatecar', views.update_car, name='update_car'),
    # path('cars/deletecar', views.delete_car, name='delete_car'),
    path('cars/<int:pk>/deletecar', views.CarDelete.as_view(), name='delete_car'),
    # path('stores/<int:store_id>/editstore', views.edit_store, name='edit_store'),


    
   
    

]
