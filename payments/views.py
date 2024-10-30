from django.shortcuts import render, redirect, get_object_or_404
from .models import Payment
from registration.models import Registration
from .forms import PaymentForm

def make_payment(request, registration_id):
    registration = get_object_or_404(Registration, id=registration_id)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.registration = registration
            payment.save()
            return redirect('payment_success')
    else:
        form = PaymentForm()
    return render(request, 'payments/make_payment.html', {'form': form, 'registration': registration})
