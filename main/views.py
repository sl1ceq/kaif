from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import OrderForm
from .models import Order

def main(request):
    return render(request, 'main.html')


@csrf_exempt
def order_create(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            review = form.save()
            review.save()
            return redirect('order_created')
    else:
        form = OrderForm()
    context = {'form': form}
    return render(request, 'order_create.html', context)


def ordered(request):
    return render(request, 'order_created.html')