# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from django.views.decorators import csrf

from django.contrib.auth import views as auth_views

# SessionSer/urls.py

urlpatterns = [

    #session/create
    # 로그인 된 사용자의 토큰 저장
    url(r'^create/$', views.SessionCreateAPIView().as_view()),

    # session/check
    # 로그인 된 사용자의 세션 체크
    url(r'^check/$',views.SessionCheckAPIView.as_view()),
]