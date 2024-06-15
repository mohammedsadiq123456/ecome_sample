
from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from . import views
urlpatterns = [
   
    path('cart/',views.view_cart,name='cart_view'),
    path('add_to_cart',views.add_to_cart,name='add_to_cart')
    
    
]
urlpatterns += static(settings.MEDIA_URL,documment_root=settings.MEDIA_ROOT)