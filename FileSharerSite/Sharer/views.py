from django.shortcuts import render, redirect
from Sharer.models import SharedFile
from django.utils.datastructures import MultiValueDictKeyError

def index(request, page: int = 1):
    shares = SharedFile.objects.filter(pk__lte=page*10, pk__gte=page*10-10)

    context = {
        'title': f'Files (page{page})',
        'shares': shares,
    }

    return render(request, template_name='index.html', context=context)

def share(request):

    context = {
        'title': f'Share your data',
    }

    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        try:
            shared_file = request.FILES['file']
        except MultiValueDictKeyError:
            shared_file = None

        shared = SharedFile()

        if title:
            shared.title = title
        if text:
            shared.text = text
            print(text)
        if shared_file:
            shared.shared_file = shared_file
        
        shared.save()

        return redirect('home')
    return render(request, template_name='share.html', context=context)
