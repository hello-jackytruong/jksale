from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jksale.product.urls')),
    path('', include('jksale.blog.urls')),
    path('', include('jksale.account.urls', namespace='account')),
    path('', include('jksale.checkout.urls')),
    path('', include('jksale.order.urls', namespace='order')),
    path('', include('jksale.page.urls')),
    path('', include('jksale.media.urls')),
    # path('basket/', include('jksale.basket.urls', namespace='basket')),
    
    
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)