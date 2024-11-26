from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Contact, Book, Lesson
from .forms import ProductForm, ContactForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import paypalrestsdk
from django.conf import settings
# في ملف views.py الخاص بالتطبيق products
from django.shortcuts import render, get_object_or_404
from .models import Product  # افترض أن نموذج المنتج اسمه Product
from django.shortcuts import render, redirect
from .models import Product

def buy_product(request, product_id):
    product = Product.objects.get(id=product_id)

    # تحقق مما إذا كان الطلب POST
    if request.method == "POST":
        # يمكن إضافة منطق إضافي هنا، مثل التحقق من الدفع أو أي متطلبات أخرى
        # على سبيل المثال، يمكنك تخزين الطلب في نموذج جديد يسمى Order
        # أو يمكنك فقط عرض رسالة نجاح
        return redirect('products')  # توجيه المستخدم إلى صفحة المنتجات

    return render(request, 'buy_product.html', {'product': product})


def buy_product(request, product_id):
    # جلب المنتج بناءً على معرفه
    product = get_object_or_404(Product, id=product_id)
    
    # عرض صفحة الشراء مع تفاصيل المنتج
    return render(request, 'products/buy.html', {'product': product})


# إعداد PayPal SDK
'''paypalrestsdk.configure({
    "mode": "sandbox",  # "live" للإنتاج
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET
})'''

def product_list(request):
    query = request.GET.get('q', '')
    products = Book.objects.filter(title__icontains=query) if query else Book.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def buy_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # إضافة المنتج إلى السلة
    cart = Cart(request)
    cart.add(product)

    # إعداد الدفع باستخدام PayPal
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "redirect_urls": {
            "return_url": "http://localhost:8000/payment/execute",
            "cancel_url": "http://localhost:8000/payment/cancel"
        },
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": product.name,
                    "sku": "item",
                    "price": str(product.price),
                    "currency": "USD",
                    "quantity": 1
                }]
            },
            "amount": {
                "total": str(product.price),
                "currency": "USD"
            },
            "description": f"Purchase of {product.name}",
            "payee": {
                "merchant_id": settings.PAYPAL_MERCHANT_ID  # معرف التاجر الخاص بك
            }
        }]
    })

    if payment.create():
        for link in payment.links:
            if link.rel == "approval_url":
                return redirect(link.href)
    else:
        return render(request, 'error.html', {'message': 'Error creating payment'})

def payment_execute(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        return render(request, 'success.html')
    else:
        return render(request, 'error.html', {'message': 'Payment failed.'})

def home(request):
    return render(request, 'home.html')  # تأكد من وجود 'home.html' في مجلد القوالب

def success(request, book_id):
    context = {'book_id': book_id}
    return render(request, 'products/success.html', context)

def download_file(request, book_id):
    product = get_object_or_404(Product, id=book_id)
    response = HttpResponse(open(product.file.path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{product.file.name}"'
    return response

def purchase_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    messages.success(request, f"تم شراء الكتاب: {book.title}")
    return redirect('success')

def logout_view(request):
    logout(request)
    messages.success(request, "لقد تم تسجيل الخروج بنجاح.")
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"مرحباً {username}! تم تسجيل الدخول بنجاح.")
                return redirect('index')
            else:
                messages.error(request, "اسم المستخدم أو كلمة المرور غير صحيح.")
        else:
            messages.error(request, "يرجى التحقق من البيانات المدخلة.")
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

def index(request):
    return render(request, 'products/index.html')

def about(request):
    return render(request, 'products/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'products/contact.html', {'form': form})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'products/book_detail.html', {'book': book})

def cancel(request):
    return render(request, 'cancel.html')

@staff_member_required
def products_view(request):
    books = Book.objects.all()
    return render(request, 'products/products.html', {'books': books})

@login_required
@staff_member_required
def admin_page(request):
    products = Product.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_page')
    else:
        form = ProductForm()
    return render(request, 'products/admin_page.html', {'products': products, 'form': form})

def book_lessons_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    lessons = Lesson.objects.filter(book=book)
    return render(request, 'products/book_lessons.html', {'book': book, 'lessons': lessons})

def buy_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    return redirect('product_list')
from django.shortcuts import render, get_object_or_404
from .models import Product

def buy_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/buy_product.html', {'product': product})
