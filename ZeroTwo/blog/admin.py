from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditor5Widget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    form = PostAdminForm
    save_as = True
    list_display = ('id', 'title', 'slug', 'category', 'created_at', 'get_photo', 'views')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        else:
            return '-'

    get_photo.short_description = 'фото'
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('category', 'tags')
    save_on_top = True
    readonly_fields = ('views', 'created_at', 'get_photo')
    fields = ('title', 'slug', 'category', 'tags', 'content', 'photo', 'get_photo', 'views', 'created_at', )


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Post, PostAdmin)
# Register your models here.
