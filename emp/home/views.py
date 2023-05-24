from django.shortcuts import render, redirect,get_object_or_404
from .form import DataForm
from .models import Data
# Create your views here.


def form(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('modify')
    else:
        form = DataForm()

    context = {'form': form}
    return render(request, 'forms.html', context)



def modify(request):
    if request.method == 'GET':
        Datas = Data.objects.all()
        
    context = {'Datas': Datas}
    return render(request,'modify.html',context)


def delete(request, id):
    form = Data.objects.get(id=id)
    if request.method == 'POST':
        form.delete()
        return redirect('/')
    return render(request, 'delete.html')




def edit(request, id):
    data = get_object_or_404(Data, id=id)
    if request.method == 'POST':
        form = DataForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('modify')
    else:
        form = DataForm(instance=data)
    
    return render(request, 'edit.html', {'form': form, 'data': data})











