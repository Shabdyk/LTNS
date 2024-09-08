from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import UserID, ImportFile
from .forms import ImportFileForm
from django.core.exceptions import ObjectDoesNotExist

import string
import random


new_id = ''.join(random.choices(string.ascii_letters, k=10))

def index(request):

    if request.method == 'POST':
        import_files = request.FILES.getlist('files')
        
        # import_file = ImportFile.objects.create(file=new_file)
        print("FILES POSTED: ", import_files)

        for uploaded_file in import_files:
            # Create an ImportFile instance for each uploaded file
            import_file = ImportFile.objects.create(file=uploaded_file)                               
            try:
                new_user = UserID.objects.get(user_id = new_id)
                new_user.imported = import_file
                print('EXISTING USER')
            except UserID.DoesNotExist:
                print('NEW USER')
                new_user = UserID.objects.create(
                    user_id = new_id,
                    imported = import_file
                )
    try: 
        # print("Current user", UserID.objects.filter(user_id = new_id))
        user_files = UserID.objects.filter(user_id = new_id)
        for i in user_files:
            print(i.imported)
        
    except UserID.DoesNotExist:
        user_files = list()
        
    print("All users ", UserID.objects.all())



    

    return render(request, 'main/index.html')