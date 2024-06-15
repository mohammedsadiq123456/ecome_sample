from . import views
from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from . import views
urlpatterns = [
    path('',views.index,name='indexpage'),
    path('product_list/',views.list_products,name='list_product'),
    path('detail_product/<pk>',views.detail_products,name='detailed_product')
]
urlpatterns += static(settings.MEDIA_URL,documment_root=settings.MEDIA_ROOT)