# lunchup/views.py
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import JsonResponse
from .models import LunchMenu
from datetime import datetime, timedelta


def lunch_menu_list(request):
    """전체 메뉴 목록 - 날짜별로 그룹화"""
    menus = LunchMenu.objects.all().order_by('-date', 'menu_type')[:20]  # 최근 20개

    # 날짜별로 그룹화
    menu_by_date = {}
    for menu in menus:
        date_str = menu.date.strftime('%Y-%m-%d')
        if date_str not in menu_by_date:
            menu_by_date[date_str] = {
                'date': menu.date,
                'title': menu.get_title(),
                'menus': []
            }
        menu_by_date[date_str]['menus'].append(menu)

    return render(request, '../templates/menu_list.html', {
        'menu_by_date': menu_by_date,
        'title': '급식 메뉴 목록'
    })


def today_menu(request):
    """오늘의 메뉴 - A식단, B식단 모두 표시"""
    today = timezone.now().date()
    menus = LunchMenu.objects.filter(date=today).order_by('menu_type')

    return render(request, '../templates/today_menu.html', {
        'menus': menus,
        'today': today,
        'title': '오늘의 급식 메뉴'
    })


def menu_detail(request, year, month, day):
    """특정 날짜의 메뉴 상세 - 해당 날짜의 모든 메뉴"""
    date = datetime(year, month, day).date()
    menus = LunchMenu.objects.filter(date=date).order_by('menu_type')

    if not menus.exists():
        # 404 에러 대신 빈 목록으로 처리
        menus = []

    return render(request, '../templates/menu_detail.html', {
        'menus': menus,
        'date': date,
        'title': f'{date.strftime("%Y년 %m월 %d일")} 메뉴'
    })

