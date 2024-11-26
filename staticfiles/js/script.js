// يمكنك إضافة أي جافا سكريبت تحتاجه هنا
console.log("موقعنا جاهز!");

document.getElementById('filterButton').addEventListener('click', function() {
    let filterValue = document.getElementById('filterInput').value;
    let products = document.querySelectorAll('.product-item');
    products.forEach(function(product) {
      if (product.innerText.includes(filterValue)) {
        product.style.display = 'block';
      } else {
        product.style.display = 'none';
      }
    });
  });
  document.getElementById('productForm').addEventListener('submit', function(event) {
    let productName = document.getElementById('productName').value;
    let productPrice = document.getElementById('productPrice').value;
  
    if (!productName || !productPrice) {
      alert('يرجى إدخال جميع الحقول.');
      event.preventDefault();
    }
  });
    
// مثال بسيط لتطبيق تأثير تمرير سلس
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});
function openBookPopup(bookId) {
  document.getElementById(`popup-${bookId}`).style.display = 'block';
}

function closeBookPopup(bookId) {
  document.getElementById(`popup-${bookId}`).style.display = 'none';
}
