from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'name': 'Baba'})


def add(request):
    try:
        num1 = int(request.GET.get('num1', 0))
        num2 = int(request.GET.get('num2', 0))
        result = num1 + num2
    except ValueError:
        return render(request, 'result.html', {
            'result': 'Please enter valid whole numbers.',
        })

    return render(request, 'result.html', {'result': result})
