from django.urls import path
from . import views

app_name = 'lunchup'

urlpatterns = [
    # 메인 페이지 - 전체 메뉴 목록
    path('', views.lunch_menu_list, name='menu_list'),

    # 오늘의 메뉴
    path('today/', views.today_menu, name='today_menu'),

    # 특정 날짜의 메뉴
    path('menu/<int:year>/<int:month>/<int:day>/', views.menu_detail, name='menu_detail'),

    # 메뉴 추가, 수정 관련 URL 제거
    # path('add/', views.add_menu, name='add_menu'),
    # path('edit/<int:menu_id>/', views.edit_menu, name='edit_menu'),
]