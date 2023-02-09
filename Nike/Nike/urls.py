from django.contrib import admin
from django.urls import path, include
from Nike.settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static
from Nike.views import index
from Shop.views import create_clothes

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('Shop/', include('Shop.urls'))
]+ static(MEDIA_URL, document_root = MEDIA_ROOT)
