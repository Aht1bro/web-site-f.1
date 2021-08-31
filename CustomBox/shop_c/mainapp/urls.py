from django.urls import path

from .views import (
    BaseView, 
    katalog, 
    ProductDetailView, 
    CategoryDetailView, 
    CartView, 
    AddToCartView, 
    DeleteFromCartView,
    ChangeQTYView,
    CheckoutView,
    MakeOrderView,
    # loginView

)
urlpatterns = [
    path('', BaseView.as_view(), name='header2'),
    path('katalog/', katalog, name='katalog'),
    path('products/<str:ct_model>/<str:slug>/', ProductDetailView.as_view(), name='tovar'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/<str:ct_model>/<str:slug>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove-from-cart/<str:ct_model>/<str:slug>/', DeleteFromCartView.as_view(), name='delete_from_cart'),
    path('change-qty/<str:ct_model>/<str:slug>/', ChangeQTYView.as_view(), name='change_qty'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('make-order/', MakeOrderView.as_view(), name='make_order'),
    # path('login/', loginView.as_view(), name='login')
]

