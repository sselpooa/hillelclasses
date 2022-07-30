from django.urls import path
from product import views


urlpatterns = [
    path('', views.index, name='index'),
    path('all', views.get_all_products),
    path('all/<str:status>',views.get_by_status),
    path('product/<int:prd_id>', views.get_detail),
    path('product/<str:genre>', views.get_by_genre),
    path('product/<str:performer>', views.get_by_performer)
]