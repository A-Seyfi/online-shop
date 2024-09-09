from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserPanelDashboardPage.as_view(), name='profile_page'),
    path('change-pass', views.ChangePasswordPage.as_view(), name='change_password_page'),
    path('favorites', views.favorites_list, name='favorites_list'),
    path('user-basket', views.user_basket, name='user_basket_page'),
    path('my-shopping', views.MyShopping.as_view(), name='user_shopping_page'),
    path('my-shopping-detail/<order_id>', views.my_shopping_detail, name='user_shopping_detail_page'),
    path('remove-order-detail', views.remove_order_detail, name='remove_order_detail_ajax'),
    path('change-order-detail', views.change_order_detail_count, name='change_order_detail_count_ajax'),
]