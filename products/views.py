from django.shortcuts import render, redirect
from products.models import *
from .forms import FeedbackForm


def product(request, product_id):
    product = Product.objects.get(id=product_id)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)

    return render(request, 'product.html', locals())


def feedback(request, feedback_id):
    feedback = Feedback.objects.get(id=feedback_id)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)

    return render(request, 'product.html', locals())

# def feedback(request):
#
#     feedbacks = Feedback.objects
#
#     return render(request, 'product.html', { 'feedbacks':feedbacks } )

# Create your views here.
