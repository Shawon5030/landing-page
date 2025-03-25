from django.urls import path
from .views import home_page, update_cart
from django.conf import settings
from django.conf.urls.static import static
from .views import home_page, update_cart, submit_order

urlpatterns = [
    path('', home_page, name='home'),
    path('update-cart/', update_cart, name='update_cart'),
    path('submit-order/', submit_order, name='submit_order'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)