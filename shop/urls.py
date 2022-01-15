from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include
from .views import by_category, delivery, index, order, support

urlpatterns = [
    path('', index, name='index'),
    path('<int:category_id>/', by_category),
    path('delivery/', delivery, name='delivery'),
    path('order/', order, name='order'),
    path('support/', support, name='support'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
