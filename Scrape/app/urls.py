from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('scripe/', views.scrape_and_capture_images, name='scrape'),
    path('',views.index)
    

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
