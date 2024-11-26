from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   # path('admin/', admin.site.urls),
    path('', include('products.urls')),  # تضمين مسارات تطبيق products
    path('accounts/', include('django.contrib.auth.urls')),  # إضافة مسارات تسجيل الدخول والخروج
]

# إضافة مسارات ملفات الوسائط أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
