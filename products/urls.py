from django.urls import path
from .views import (
    SingleProductPageDetailView,
    CategoryDetailView,
    products_bulk_edit,
    ProductImageBulkEditListView
)
app_name = 'products'

urlpatterns = [
    path('single_product/<int:pk>', SingleProductPageDetailView.as_view(), name='show_single_product_page'),
    path('products_bulk_edit/', products_bulk_edit, name='products_bulk_edit'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='category_view'),
    path('product_images_bulk_edit/', ProductImageBulkEditListView.as_view(), 
                                    name = 'product_image_bulk_edit')
    
]