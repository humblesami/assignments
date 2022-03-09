# payments/views.py
import stripe
from django.conf import settings # new
from django.http.response import JsonResponse, HttpResponse  # new
from django.views.decorators.csrf import csrf_exempt # new
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = 'payments/home.html'


def payment_success(request):
    res = {'status': 'success', 'message': 'payment done'}
    res = JsonResponse(res)
    return res


def payment_cancel(request):
    res = {'status': 'success', 'message': 'cancelled'}
    res = JsonResponse(res)
    return res

# new
@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)
    

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        amount = request.GET.get('amount')
        dfi = request.GET.get('file_id')
        if not dfi:
            res = {'error': 'Invalid file id to download' }
            return JsonResponse(res)
        if amount:
            amount = int(amount)
        if not amount:
            res = {'error': 'No amount provided'}
            return JsonResponse(res)
        domain_url = settings.SITE_URL
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + '?session_id={CHECKOUT_SESSION_ID}&download_file_id='+dfi,
                cancel_url=domain_url + '/payments/cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'name': 'File-Download',
                        'quantity': 1,
                        'currency': 'usd',
                        'amount': amount
                    }
                ]
            )
            session_id = checkout_session['id']
            res = {'sessionId': session_id}
            return JsonResponse(res)
        except Exception as e:
            res = {'error': str(e)}
            return JsonResponse(res)

        
@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        print("Payment was successful.")
        # TODO: run some custom code here

    return HttpResponse(status=200)
