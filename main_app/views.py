import logging

from django.shortcuts import render

from main_app import mpesa

# Create your views here.
logger = logging.getLogger(__name__)


def initiate_payment(request):
    if request.method == "POST":
        phone = request.POST["phone"]
        amount = request.POST["amount"]
        logger.info(f"{phone} {amount}")

        data = {
            "BusinessShortCode": mpesa.get_business_shortcode(),
            "Password": mpesa.generate_password(),
            "Timestamp": mpesa.get_current_timestamp(),
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": mpesa.get_business_shortcode(),
            "PhoneNumber": phone,
            "CallBackURL": mpesa.get_callback_url(),
            "AccountReference": "123456",
            "TransactionDesc": "Payment for merchandise"
        }

    return render(request, 'payment.html')


def callback(request):
    return None
