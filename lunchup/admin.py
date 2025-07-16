# lunchup/admin.py
from django.contrib import admin
from .models import LunchMenu


@admin.register(LunchMenu)
class LunchMenuAdmin(admin.ModelAdmin):
    list_display = ['get_title', 'menu_type', 'menu_preview', 'created_at']
    list_filter = ['date', 'menu_type', 'created_at']
    search_fields = ['menu_content']
    date_hierarchy = 'date'

    # 같은 날짜의 A식단, B식단을 쉽게 구분하기 위해 정렬
    ordering = ['-date', 'menu_type']

    def menu_preview(self, obj):
        return obj.menu_content[:50] + "..." if len(obj.menu_content) > 50 else obj.menu_content

    menu_preview.short_description = "메뉴 미리보기"

    def get_title(self, obj):
        return obj.get_title()

    get_title.short_description = "날짜"

    # 필드 그룹화
    fieldsets = (
        ('기본 정보', {
            'fields': ('date', 'menu_type')
        }),
        ('메뉴 내용', {
            'fields': ('menu_content',)
        }),
    )
