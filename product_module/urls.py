from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product-list'),
    path('cat/<cat>', views.ProductListView.as_view(), name='product-categories-list'),
    path('brand/<brand>', views.ProductListView.as_view(), name='product-list-by-brands'),
    path('<int:product_id>/add_to_favorites/', views.add_to_favorites, name='add_to_favorites'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product-detail'),
    path('compare/', views.compare_products, name='compare_products'),
    path('compare-result/', views.compare_result, name='compare_result'),
    path('search/', views.search, name='search')
]