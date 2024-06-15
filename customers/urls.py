from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from . import views
urlpatterns = [

    path('Account/',views.account_view,name='view_account'),
    
]
urlpatterns += static(settings.MEDIA_URL,documment_root=settings.MEDIA_ROOT)