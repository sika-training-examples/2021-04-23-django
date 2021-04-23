from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from .models import Note

def index_view(request):
  notes = Note.objects.all().order_by("-id")
  return render(request, "notes/index.html", {
    "notes": notes,
  })

def author_view(request, author_id):
  author = get_object_or_404(User, id=author_id)
  notes = Note.objects.filter(author_id=author_id).order_by("-id")
  return render(request, "notes/author_list.html", {
    "author": author,
    "notes": notes,
  })

def detail_view(request, note_id):
  note = get_object_or_404(Note, id=note_id)
  return render(request, "notes/detail.html", {
    "note": note,
  })
