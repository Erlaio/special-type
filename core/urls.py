from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from api.views import CaptureCheckViewSet

admin.site.site_header = "Администрирование сайта"
admin.site.site_title = "Администрирование сайта"
admin.site.index_title = "Добро пожаловать!"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('yookassa/', include('yookassa_payment.urls')),
    path('captcha/', include('rest_captcha.urls')),
    path('checker/', CaptureCheckViewSet.as_view())
]
