from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from ffp.settings import MEDIA_ROOT, MEDIA_URL, STATIC_URL, STATICFILES_DIRS

urlpatterns = [
    path('', views.home, name='home'),
    path('just-admin-page', views.admin_i, name='admin_i'),
    path('item-list', views.item_list, name='item_list'),
    path('add-item', views.add_item, name='add_item'),
    path('delete-item/<int:id>', views.delete_item, name='delete_item'),
    path('payment-page', views.payment_p, name='payment'),
    path('img-list', views.img_list, name='img_list'),
    path('add-image', views.add_img, name="add_img"),
    path('delete-img/<int:id>', views.delete_img, name='delete_img'),
    path('login', views.login_page, name='login')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
