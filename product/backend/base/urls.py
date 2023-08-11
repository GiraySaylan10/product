from django.urls import path
from . import views

urlpatterns = [
    path('home', views.products_home_view, name='productsHome'),
    path('index',views.products_index_view,name = 'productsIndex'),
     path('detail/<int:id>',views.products_detail_view,name = 'productsDetail'),
     path('create',views.products_create_view, name = "productsForm"),
      path('update/<int:id>',views.products_update_view, name = "productsUpdate"),
      path('delete/<int:id>',views.products_delete_view, name = "productsDelete")
]