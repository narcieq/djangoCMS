from django.contrib import admin
from member.models import Member
# Register your models here.

#admin.site.register(Member)


class MemberAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = (
        'id', 'email', 'user_name',
        'permission', 'is_certificated',
        'certification_date', 'post_count', )
    list_editable = ('permission', )
    list_filter = ('permission', )
    search_fields = ('username', )
    ordering = ('id', 'email', 'permission',)

    def post_count(self, obj):
        return Post.objects.filter(member=obj).count()

    post_count.short_description = '작성한 글 수'

admin.site.register(Member, MemberAdmin)
