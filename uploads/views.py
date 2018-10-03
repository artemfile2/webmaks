import os

from django.shortcuts import render
from .forms import UploadFileForm
from .models import FileDbf
from django.conf import settings

from .insert2base import oper


def dbf_ident(f):
    dbf_file = os.path.join(settings.FILES_ROOT, f)
    if os.path.exists(dbf_file):
        name = os.path.basename(dbf_file)
        if name.lower() == 'oper.dbf':
            oper(dbf_file)
        elif name.lower() == 'sp_tarif.dbf':
            pass
        elif name.lower() == 'rg.dbf':
            pass
        elif name.lower() == 'podush.dbf':
            pass
        elif name.lower() == 'met_hmp.dbf':
            pass
        elif name.lower() == 'klpu.dbf':
            pass
        elif name.lower() == 's_lpu.dbf':
            pass
        elif name.lower() == 'umer.dbf':
            pass
        elif name.lower() == 'stacotd.dbf':
            pass
        elif name.lower() == 'profot.dbf':
            pass
        elif name.lower() == 'prikr.dbf':
            pass

def delete_file(f):
    fullname = os.path.join(settings.FILES_ROOT, f)
    if os.path.exists(fullname):
        os.remove(fullname)


def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            delete_file(request.FILES['file'].name)
            newfile = FileDbf(file=request.FILES['file'])
            newfile.save()
            dbf_ident(request.FILES['file'].name)
            return render(request, 'uploads.html', {'form':form, 'message':'Загрузка завершенна!'})
            # return HttpResponseRedirect('/uploads')
    else:
        form = UploadFileForm()
    return render(request, 'uploads.html', {'form':form, 'test':'text test'})
