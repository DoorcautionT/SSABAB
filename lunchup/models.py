# lunchup/models.py
from django.db import models
from django.utils import timezone
import datetime


class LunchMenu(models.Model):
    MENU_TYPE_CHOICES = [
        ('normal', '일반식'),
        ('special', '특별식'),
        # 또는 다른 분류를 원한다면:
        # ('normal', '일반식'),
        # ('special', '특식'),
    ]

    # 날짜 필드
    date = models.DateField(
        verbose_name="급식 날짜",
        default=timezone.now,
        help_text="급식을 제공하는 날짜"
    )

    # 메뉴 타입 필드 (새로 추가)
    menu_type = models.CharField(
        verbose_name="메뉴 타입",
        max_length=10,
        choices=MENU_TYPE_CHOICES,
        default='A',
        help_text="일반식단 또는 특별식단 선택"
    )

    # 메뉴 내용 필드
    menu_content = models.TextField(
        verbose_name="점심 메뉴",
        help_text="점심 메뉴 내용을 입력하세요"
    )

    # 메타 정보
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "급식 메뉴"
        verbose_name_plural = "급식 메뉴들"
        ordering = ['-date', 'menu_type']  # 최신 날짜순, 메뉴 타입순으로 정렬
        unique_together = ['date', 'menu_type']  # 같은 날짜, 같은 타입의 중복 방지

    def __str__(self):
        return f"{self.get_title()} - {self.get_menu_type_display()} - {self.menu_content[:30]}..."

    def get_title(self):
        """날짜와 요일이 포함된 제목 생성"""
        weekdays = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
        weekday_name = weekdays[self.date.weekday()]
        return f"{self.date.strftime('%Y년 %m월 %d일')} ({weekday_name})"

    def get_full_title(self):
        """날짜, 요일, 메뉴 타입이 포함된 완전한 제목 생성"""
        return f"{self.get_title()} - {self.get_menu_type_display()}"

    def get_menu_list(self):
        """메뉴를 리스트로 반환 (줄바꿈 기준)"""
        return [menu.strip() for menu in self.menu_content.split('\n') if menu.strip()]

    def is_today(self):
        """오늘 메뉴인지 확인"""
        return self.date == timezone.now().date()

    def is_weekend(self):
        """주말인지 확인"""
        return self.date.weekday() >= 5  # 5=토요일, 6=일요일
