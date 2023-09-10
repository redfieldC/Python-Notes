from django.shortcuts import render, redirect
from .models import Person
from .serializers import PersonSerializers
from django.http import Http404

def person_list(request):
    persons = Person.objects.all()
    return render(request, 'person_list.html', {'persons': persons})

def person_detail(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        raise Http404("Person does not exist")
    
    return render(request, 'person_detail.html', {'person': person})

def create_person(request):
    if request.method == 'POST':
        serializer = PersonSerializers(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('person_list')
    else:
        serializer = PersonSerializers()
    
    return render(request, 'create_person.html', {'serializer': serializer})

def update_person(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        raise Http404("Person does not exist")
    
    if request.method == 'POST':
        serializer = PersonSerializers(instance=person, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('person_list')
    else:
        serializer = PersonSerializers(instance=person)
    
    return render(request, 'update_person.html', {'serializer': serializer, 'person': person})

def delete_person(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        raise Http404("Person does not exist")
    
    if request.method == 'POST':
        person.delete()
        return redirect('person_list')
    
    return render(request, 'delete_person.html', {'person': person})
