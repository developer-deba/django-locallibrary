from django.contrib import admin
from django.db import models
from .models import Genre,Book,Bookinstance,Author
# Register your models here.
class BookInstanceInline(admin.TabularInline):
    model = Bookinstance
    
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','date_of_birth','date_of_death')
    fields = ['first_name','last_name',('date_of_birth','date_of_death')]
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','display_genre')
    inlines = [BookInstanceInline]

class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book','status','due_back','id')
    list_filter = ('status','due_back')
    fieldsets = (
        (None,{'fields':('book','imprint','id')}),
        ('Ailibility',{'fields':('status','due_back')}),
    )

admin.site.register(Genre)
# admin.site.register(Book)
# admin.site.register(Bookinstance)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Bookinstance,BookInstanceAdmin)
