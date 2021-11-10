from django.shortcuts import render, redirect
from .models import MyNote
from .forms import CreateNote
from django.http import HttpResponse

# Create your views here.
def index(request):
    notes = MyNote.objects.all()
    return render(request, 'notes/home.html', {'notes':notes})

def upload(request):
    upload = CreateNote()
    if request.method == 'POST':
        upload = CreateNote(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'notes/upload_note.html', {'upload_note': upload})

def update_note(request, note_id):
    note_id = int(note_id)
    try:
        note_sel = MyNote.objects.get(id=note_id)
    except MyNote.DoesNotExist:
        return redirect('index')
    
    note_form = CreateNote(request.POST or None, instance=note_sel)
    if note_form.is_valid():
        note_form.save()
        return redirect('index')
    return render(request, 'notes/upload_note.html', {'upload_note': note_form})

def delete_note(request, note_id):
    note_id = int(note_id)
    try:
        note_sel = MyNote.objects.get(id=note_id)
    except MyNote.DoesNotExist:
        return redirect('index')
    note_sel.delete()
    return redirect('index')