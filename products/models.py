from django.db import models
from django.contrib.auth.models import User






# نموذج للكتب
class Book(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    file = models.FileField(upload_to='uploads/', null=True, blank=True)#تخزين الملفات في مجلد "books"

    def __str__(self):
        return self.title

# تعريف النموذج الصحيح للمنتجات
class Product(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=200)  # الحقل الصحيح هنا هو title
    description = models.TextField()          # الوصف
    price = models.DecimalField(max_digits=10, decimal_places=2)  # السعر
    download_file = models.FileField(upload_to='downloads/')  # ملف التنزيل
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # الصورة
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title  # عرض عنوان المنتج في إدارة Django

# نموذج لرسائل الاتصال
class Contact(models.Model):
    name = models.CharField(max_length=100)  # اسم المرسل
    email = models.EmailField()  # البريد الإلكتروني
    message = models.TextField()  # الرسالة

    def __str__(self):
        return self.name  # عرض اسم المرسل في إدارة Django

# نموذج للدروس
class Lesson(models.Model):
    book = models.ForeignKey(Book, related_name='lessons', on_delete=models.CASCADE)  # الكتاب المرتبط بالدرس
    title = models.CharField(max_length=200)  # عنوان الدرس
    description = models.TextField()  # وصف الدرس
    powerpoint_file = models.FileField(upload_to='powerpoint_files/', blank=True, null=True)  # ملف PowerPoint
    word_file = models.FileField(upload_to='word_files/', blank=True, null=True)  # ملف Word
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # صورة الدرس

    def __str__(self):
        return self.title  # عرض عنوان الدرس في إدارة Django
