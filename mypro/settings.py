# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myproject',  # اسم قاعدة البيانات التي أنشأتها
        'USER': 'root',       # اسم المستخدم (غالبًا root)
        'PASSWORD': 'new_password',  # كلمة المرور التي وضعتها أثناء التثبيت
        'HOST': 'localhost',  # أو 127.0.0.1 إذا كنت تعمل محليًا
        'PORT': '3306',       # المنفذ الافتراضي لـ MySQL
    }
}


import os
from pathlib import Path
BRAINTREE_MERCHANT_ID = 'bhhn84fv5spqsdjp'
BRAINTREE_PUBLIC_KEY = 'qg6h6rvd9ht4j5fn'
BRAINTREE_PRIVATE_KEY = '60c092a9cff3693a648d798a223bdac0'
# إعدادات PayPal

PAYPAL_CLIENT_SECRET = 'EFjCWlXJ6ywHD-kVroXfJa1nwmKJFCfAvb5wRjnstbhOTR0eQzZznr0HC5oIIW4n-SmHoTwDzLr0I474'
PAYPAL_CLIENT_ID = 'ASdkr_QNcVd52rz0WWMvmdmlNxJgeEbUkfMQnz8CgLdecBIEnAAmZnvyHjI9oBg_UfcwCVJNYTu_Sfle'
# استخدم المفتاح السري الخاص بك هنا


# BASE_DIR definition
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your_secret_key_here'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
  

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'products','carton',# التطبيقات الافتراضية
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # التطبيقات الإضافية لـ Django Oscar
    'django.contrib.sites',  # يحتاجه Django Oscar
    'oscar',  # التطبيق الرئيسي
    'oscar.apps.address',  # إدارة العناوين
    'oscar.apps.basket',  # سلة التسوق
    'oscar.apps.checkout',  # عملية الدفع
    'oscar.apps.catalogue',  # إدارة المنتجات
    'oscar.apps.order',  # إدارة الطلبات
    'oscar.apps.payment',  # إدارة الدفع
    'oscar.apps.promotions',  # العروض الترويجية
    'oscar.apps.shipping',  # الشحن
    'oscar.apps.users',  # إدارة المستخدمين
    'oscar.apps.dashboard',  # لوحة التحكم
    'oscar.apps.dashboard.catalogue',  # لوحة التحكم للمنتجات
    'oscar.apps.dashboard.orders',  # لوحة التحكم للطلبات
    'oscar.apps.dashboard.basket',  # لوحة التحكم للسلة
    'oscar.apps.dashboard.promotions',  # لوحة التحكم للعروض الترويجية
    'oscar.apps.dashboard.users',  # لوحة التحكم للمستخدمين
    'oscar.apps.dashboard.addresses',  # لوحة التحكم للعناوين
    'oscar.apps.dashboard.reviews',
    'oscar',
    'oscar.apps.catalogue',
    'oscar.apps.basket',
    'oscar.apps.checkout',
    'oscar.apps.order',
    'oscar.apps.payment',
    'oscar.apps.shipping',
    'oscar.apps.promotions',
    'oscar.apps.dashboard',
    'oscar.apps.partner',
    'oscar.apps.dashboard.apps.DashboardConfig',
    'oscar.apps.checkout.apps.CheckoutConfig',  # إضافة قسم checkout لـ Oscar
    'oscar.apps.catalogue.apps.CatalogueConfig',  # إضافة قسم catalogue لـ Oscar
    'oscar.apps.partner.apps.PartnerConfig',  # إضافة قسم partner لـ Oscar
    'oscar.apps.basket.apps.BasketConfig',  # إضافة قسم basket لـ Oscar
    'oscar.apps.order.apps.OrderConfig',  # إضافة قسم order لـ Oscar
    'oscar.apps.payment.apps.PaymentConfig',  # إضافة قسم payment لـ Oscar
    'oscar.apps.offer.apps.OfferConfig',  # إضافة قسم offer لـ Oscar
    'oscar.apps.shipping.apps.ShippingConfig',  # إضافة قسم shipping لـ Oscar
    'oscar.apps.customer.apps.CustomerConfig',  # إضافة قسم customer لـ Oscar
    'oscar.apps.search.apps.SearchConfig',  # إضافة قسم search لـ Oscar
    'oscar.apps.voucher.apps.VoucherConfig',  # إضافة قسم voucher لـ Oscar
    'oscar.apps.wishlists.apps.WishlistsConfig',  # إضافة قسم wishlists لـ Oscar
    'oscar.apps.dashboard.apps.DashboardConfig',  # إضافة لوحة التحكم Dashboard# لوحة التحكم للتقييمات

    # أي تطبيقات أخرى تحتاجها
    'widget_tweaks',  # لتحسين تصميم النماذج  # اسم التطبيق الخاص بك
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# settings.py

SITE_ID = 1
# settings.py

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
ROOT_URLCONF = 'mypro'

ROOT_URLCONF = 'mypro.urls'

# TEMPLATES configuration

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # مجلد القوالب
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'mypro.wsgi.application'

# Database configuratio
'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
'''
# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files settings
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files (uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Authentication redirect settings
LOGIN_REDIRECT_URL = 'index'  # بعد تسجيل الدخول
LOGOUT_REDIRECT_URL = 'login'  # بعد تسجيل الخروج

# Messages settings
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'error',
}

# PayPal settings
   
PAYPAL_MODE = "sandbox"  # يمكن تغييره إلى "live" في بيئة الإنتاج
# mypro/settings.py

import os
from pathlib import Path

# بناء المسار الأساسي
BASE_DIR = Path(__file__).resolve().parent.parent

# إعدادات سرية
SECRET_KEY = 'your-secret-key'
DEBUG = True

ALLOWED_HOSTS = []

# التطبيقات المثبتة
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'products',  # إضافة تطبيق المنتجات هنا
]

# إعدادات قاعدة البيانات


# إعدادات الملفات الثابتة
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# تعليقات (ملاحظات) عن لفات الثابتة بعد تشغيل collectstatic
# لفات الثابتة بعد تشغيل collectstatic
