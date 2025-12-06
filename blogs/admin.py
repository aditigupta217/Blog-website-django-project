from django.contrib import admin
from .models import category, blog
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'status','author','is_featured')
    search_fields = ('id','title','category__category_name','status')


admin.site.register(category)
admin.site.register(blog, BlogAdmin)

