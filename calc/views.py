from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'name': 'Baba'})


def add(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')

    try:
        result = int(num1) + int(num2)
    except (TypeError, ValueError):
        return render(
            request,
            'result.html',
            {'result': 'Please enter valid whole numbers.'},
        )

    return render(request, 'result.html', {'result': result})
