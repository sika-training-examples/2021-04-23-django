from django.contrib import admin
from .models import Note

class NoteAdmin(admin.ModelAdmin):
  list_display = (
    "title",
    "author",
    "text",
  )
  list_filter = (
    "author",
  )

admin.site.register(Note, NoteAdmin)
