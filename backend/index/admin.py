from django.contrib import admin
from .models import Contact, Deceased, DeceasedGallery, CondolenceNotes

# Register your models here.

class DeceasedGalleryAdmin(admin.StackedInline):
    model = DeceasedGallery

class CondolenceNotesAdmin(admin.TabularInline):
    model = CondolenceNotes

class DeceasedAdmin(admin.ModelAdmin):
    inlines = [DeceasedGalleryAdmin, CondolenceNotesAdmin]

    class Meta:
        model = Deceased

# class CondolenceNotesAdmin(admin.ModelAdmin):
#     list_display = ['condoled_by', 'deceasedid']


admin.site.register(Contact)
admin.site.register(Deceased, DeceasedAdmin)
admin.site.register(CondolenceNotes)