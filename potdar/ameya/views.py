from django.shortcuts import render, get_object_or_404, redirect
from .models import Person
from .forms import PersonForm

def home(request):
    people = Person.objects.all()
    return render(request, 'home.html', {'people': people})

def create(request):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('person:home')
    return render(request, 'create.html', {'form': form})

def update(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonForm(request.POST or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('person:home')
    return render(request, 'update.html', {'form': form, 'person': person})

def delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    return render(request, 'delete.html', {'person': person})

def confirm_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    person.delete()
    return redirect('person:home')
