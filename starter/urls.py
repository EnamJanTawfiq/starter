from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    path('',views.home,name='home'),
    path('create_product/',views.create_product),
    path('update_product/<int:pk>/edit',views.update_product,name='update_product'),
    path('delete_product/<int:pk>/delete',views.delete_product,name='delete_product')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

