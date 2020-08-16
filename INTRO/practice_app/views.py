import random
from django.shortcuts import render

# Create your views here.


def page1(request):
    nums = random.sample(range(1,46), 6)
    context = {
        'nums': nums
    }
    return render(request, 'nums.html', context)