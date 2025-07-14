import random
from django.shortcuts import render, get_object_or_404
from citate.models import Citata
from django.http import JsonResponse
from django.views.decorators.http import require_POST

def find_random_citate(citates):
    score = 0
    for citate in citates:
        score+=citate.weight
    index = random.randint(0, score)
    for citate in citates:
        if index-citate.weight>0:
            index-=citate.weight
        else:
            return citate

def main(request):
    citates = Citata.objects.all()
    citate = find_random_citate(citates)
    if citate:
        citate.views=citate.views+1
        citate.save(update_fields=['views'])
    return render(request, 'main.html', {'citate':citate})

@require_POST
def update_rating(request):
    citate_id = request.POST.get('citate_id')
    action = request.POST.get('action')
    
    try:
        citate = get_object_or_404(Citata, pk=citate_id)
        if action=='Like':
            citate.raiting=citate.raiting+1
        elif action=='Dislike':
            citate.raiting=citate.raiting-1
        citate.save()
        return JsonResponse({
            'status': 'success',
            'new_rating': citate.raiting,
        })
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


def top(request):
    return render(request, 'top.html')