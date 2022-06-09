from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('category/<int:pk>', views.CategoryDetailView.as_view(), name='category-detail'),
]
urlpatterns += [
    path('product/create/', views.ProductCreate.as_view(), name='product-create'),
    path('product/<int:pk>/update/', views.ProductUpdate.as_view(), name='product-update'),
    path('product/<int:pk>/delete/', views.ProductDelete.as_view(), name='product-delete'),
]
urlpatterns += [
    path('category/create/', views.CategoryCreate.as_view(), name='category-create'),
    path('category/<int:pk>/update/', views.CategoryUpdate.as_view(), name='category-update'),
    path('category/<int:pk>/delete/', views.CategoryDelete.as_view(), name='category-delete'),
]
