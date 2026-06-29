from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),         # 標準の管理者URL（ここを修正）
    path('', include('apps.bookings.urls')),  # bookingsアプリのURLをルートに接続
]