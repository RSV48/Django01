from django.urls import path, re_path
import ordersapp.views as ordersapp

app_name = 'ordersapp'

urlpatterns = [
    path('', ordersapp.OrderList.as_view(), name='orders_list'),
    path('create/', ordersapp.OrderCreateView.as_view(), name='order_create'),
    path('read/<int:pk>/', ordersapp.OrderReadView.as_view(), name='order_read'),
    path('update/<int:pk>/', ordersapp.OrderUpdateView.as_view(), name='order_update'),
    path('delete/<int:pk>/', ordersapp.OrderDeleteView.as_view(), name='order_delete'),
    path('forming/complete/<int:pk>/', ordersapp.order_forming_complete, name='order_forming_complete'),
    path('product/<pk>/price/', ordersapp.get_product_price),
]