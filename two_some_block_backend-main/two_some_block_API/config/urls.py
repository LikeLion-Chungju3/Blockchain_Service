from django.contrib import admin
from django.urls import path
# 추가
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 추가
    path('users/', include('mytokens.urls')),
]