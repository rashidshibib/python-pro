import paypalrestsdk

paypalrestsdk.configure({
    "mode": "sandbox",  # غير إلى "live" عند التشغيل في الإنتاج
    "client_id": "qg6h6rvd9ht4j5fn",  # معرف العميل الخاص بك
    "client_secret": "60c092a9cff3693a648d798a223bdac0"  # المفتاح السري الخاص بك
})
