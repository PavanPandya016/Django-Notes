from django.shortcuts import render, redirect
from myapp.forms import myapp_form
from myapp.models import myapp_db
from django.contrib import messages

def edit_item(request, id):
    item = myapp_db.objects.get(id=id)  

    if request.method == 'POST':
        form = myapp_form(request.POST, instance=item)  
        if form.is_valid():
            form.save()  
            messages.success(request, 'Item updated successfully!')
            return redirect('home')
    else:
        form = myapp_form(instance=item)  

    return render(request, 'edit.html', {'form': form})
   
def delete_item(request, id):
    if request.method == 'POST':
        item = myapp_db.objects.get(id=id)
        item.delete()
        messages.success(request, 'Item deleted successfully!')
    return redirect('home')

def home(request):
    form = myapp_form()

    if request.method == 'POST':
        form = myapp_form(request.POST)
        if form.is_valid():
            topics = form.cleaned_data['topics']
            notes = form.cleaned_data['notes']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']

            savetodb = myapp_db(
                topics=topics,
                notes=notes,
                date=date,
                time=time,
            )
            savetodb.save()
            messages.success(request, 'Form submitted successfully!')
            return redirect("home")  

    
    all_data = myapp_db.objects.all()  

    context = {
        'form': form,
        'all_data': all_data  
    }
    return render(request, 'index.html', context)
