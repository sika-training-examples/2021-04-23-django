from django.shortcuts import render

from .models import Note

def index_view(request):
  notes = Note.objects.all().order_by("-id")
  return render(request, "notes/index.html", {
    "notes": notes,
  })

def author_view(request, author_id):
  notes = Note.objects.filter(author_id=author_id).order_by("-id")
  return render(request, "notes/index.html", {
    "notes": notes,
  })
