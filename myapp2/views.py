from django.shortcuts import render
from django.db.models import Sum
from myapp2.models import Product


# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        print(name)

    return render(request, 'example.html')





def total_in_db(request):
    total = Product.objects.aggregate(Sum('quantity'))
    print(f'---------------------{total}')
    context = {'title': 'Общее количество посчитано в базе данных', 'total': total, }
    
    return render(request, 'myapp2/site.html', context)



def total_in_view(request):
    products = Product.objects.all()
    print(f'---------------------{products}')
    print(products)
    total = sum(product.quantity for product in products)
    context = {'title': 'Общее количество посчитано в представлении', 'total': total,}

    return render(request, 'myapp2/site.html', context)


def total_in_template(request):
    context = {'title': 'Общее количество посчитано в шаблоне', 'products': Product,}
    
    return render(request, 'myapp2/site.html', context)
