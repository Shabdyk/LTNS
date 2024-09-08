from django.shortcuts import render
from django.http import JsonResponse
from .models import UserID
from .forms import ImportFileForm
import string
import random

def index(request):
    new_id = ''.join(random.choices(string.ascii_letters, k=10))
    new_user = UserID(user_id = new_id)

    if request.method == 'POST':
        form = ImportFileForm(request.POST, request.FILES)
        if form.is_valid():
            
            new_user.imported = form
            form.save()  # Save the uploaded file
            new_user.save()
            
            files = new_user.imported.objects.all()  # Get the list of uploaded files
            return JsonResponse({
                'success': True,
                'files': [{'name': f.file.name} for f in files]
            })
        else:
            return JsonResponse({'success': False})

    form = ImportFileForm()

    return render(request, 'main/index.html', {
        'form': form
    })
