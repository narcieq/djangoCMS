from django.contrib import admin
from post.models import Category, Post, Comment
from post.forms import MyPostAdminForm
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    form = MyPostAdminForm
    list_per_page = 10
    list_display = (
        'id',  'title', 'member',
        'is_deleted', 'created_at',
    )
    list_editable = ('is_deleted',)

    #fields = ('member', 'category', 'title',)
    fieldsets = (
        ('기본정보', {
            'fields' : (('member', 'category', ), )
        }),
        ('제목 및 내용', {
            'fields' : (
                'title', 'subtitle', 'content',
            )
        }),
        ('삭제', {
            'fields' : ('is_deleted', 'deleted_at', )
        }),
    )



admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
