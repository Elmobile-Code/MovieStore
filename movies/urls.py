from django.urls import path
from . import views
from .views import add_to_cart, remove_from_cart, cart_detail

urlpatterns = [
    path('', views.index, name='movies.index'),
    path('<int:id>/', views.show, name='movies.show'),
    path('<int:id>/review/create/', views.create_review, name='movies.create_review'),
    path('<int:id>/review/<int:review_id>/edit/', views.edit_review, name='movies.edit_review'),
    path('<int:id>/review/<int:review_id>/delete/', views.delete_review, name='movies.delete_review'),
    path('add-to-cart/<int:movie_id>/', views.add_to_cart, name='movies.add_to_cart'),
    path('remove-from-cart/<int:cart_item_id>/', views.remove_from_cart, name='movies.remove-from-cart'),
    path('cart/', views.cart_detail, name='movies.cart-detail'),
]