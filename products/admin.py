from django.contrib import admin
from .models import Product, Contact, Book, Lesson
# products/admin.py




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # تأكد من أن الحقول التالية موجودة في نموذج Product
    fields = ('title', 'description', 'price', 'image', 'download_file')  
    list_display = ('title', 'description', 'price')  # عرض الحقول في قائمة الـ admin

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'book')
