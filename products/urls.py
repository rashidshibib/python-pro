from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from .views import login_view, logout_view, buy_product
from .views import buy_product
from oscar.app import get_application

urlpatterns = [
    path('', views.index, name='index'),  # الصفحة الرئيسية
    path('about/', views.about, name='about'),  # صفحة "من نحن"
    path('contact/', views.contact, name='contact'),  # صفحة التواصل
    path('products/', views.product_list, name='product_list'),  # قائمة المنتجات
    path('admin-page/', views.admin_page, name='admin_page'),  # صفحة الإدارة
    path('admin/products/', views.products_view, name='admin_products'),  # صفحة منتجات الإدارة
    path('books/<int:book_id>/', views.book_lessons_view, name='book_lessons'),  # عرض دروس الكتاب
    path('buy-lesson/<int:lesson_id>/', views.buy_lesson, name='buy_lesson'),  # صفحة شراء الدرس
    path('book_detail/<int:book_id>/', views.book_detail, name='book_detail'),  # صفحة تفاصيل الكتاب
    path('purchase/<int:book_id>/', views.purchase_book, name='purchase_book'),  # صفحة شراء الكتاب
    path('success/', views.success, name='success'),  # صفحة نجاح الشراء
    path('cancel/', views.cancel, name='cancel'),  # صفحة إلغاء الشراء
    path('login/', login_view, name='login'),  # صفحة تسجيل الدخول
    path('logout/', logout_view, name='logout'),  # صفحة تسجيل الخروج
    path('auth/', include('social_django.urls', namespace='social')),  # مسار المصادقة الاجتماعية
    path('buy_product/<int:product_id>/', buy_product, name='buy_product'),  # صفحة شراء المنتج
    path('download/<int:book_id>/', views.download_file, name='download_file'),  # صفحة تحميل الملف
    path('payment/execute/', views.payment_execute, name='payment_execute'),  # تنفيذ الدفع
    path('payment/success/', views.success, name='payment_success'),  # صفحة نجاح الدفع (تغيير الاسم لتفادي التكرار)
    path('payment/cancel/', views.cancel, name='payment_cancel'),  # صفحة إلغاء الدفع (تغيير الاسم لتفادي التكرار)
    path('admin/', admin.site.urls),  # استخدام admin بدون مساحة اسم
    path('buy/<int:product_id>/', views.buy_product,name='buy_product'),
    path('admin/', admin.site.urls),
    path('dashboard/', include('oscar.apps.dashboard.urls')),  # إضافة لوحة التحكم
    path('shop/', include('oscar.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
