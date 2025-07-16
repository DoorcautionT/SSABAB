# myproject/urls.py (메인 프로젝트의 urls.py)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lunchup.urls')),  # lunchup 앱의 URLs 포함
    # 또는 특정 경로로 설정하고 싶다면:
    # path('lunch/', include('lunchup.urls')),
]
