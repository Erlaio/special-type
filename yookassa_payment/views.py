import uuid
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from yookassa import Configuration, Payment

from core.settings import API_YOOKASSA_KEY, SHOP_ID


@api_view(['post',])
def create_payment(request):
    Configuration.account_id = SHOP_ID
    Configuration.secret_key = API_YOOKASSA_KEY
    idempotence_key = str(uuid.uuid4())
    payment = Payment.create({
        'amount': {
            'value': request.query_params['value'],
            'currency': 'RUB'
        },
        'confirmation': {
            'type': 'redirect',
            'return_url': request.query_params['return_url']
        },
        'capture': True,
        'description': request.query_params['description'],
    }, idempotence_key)
    print(payment.confirmation.confirmation_url)
    return redirect(payment.confirmation.confirmation_url)
