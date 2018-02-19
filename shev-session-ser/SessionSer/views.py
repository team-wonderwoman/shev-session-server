# -*- coding: utf-8 -*-
import json
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework import status
from .tokens import token_authentication
from common.const import const_value, status_code
from .redis import redis_set, redis_expire, redis_delete


@csrf_exempt
def session_create(request):
    if request.method == 'POST':
        print("session_create 들어옴?")

        created_token = request.POST['Token']
        user_email = request.POST['User']

        print("In Session Restore - ")
        print(created_token)
        print(user_email)

        # 레디스에 토큰 저장
        redis_set(created_token, user_email)
        redis_expire(created_token)

        status_code['SUCCESS']['data'] = const_value['SESSION_CREATED']
        return JsonResponse({'result' : status_code['SUCCESS']}, status=status.HTTP_200_OK)


@csrf_exempt
def session_check(request):
    if request.method == 'POST':
        # 토큰 검사 (인증) - 인증된 사용자는 True, 아니면 False
        print("session_check")
        print(request.POST)
        # print(request.META)
        # print("request.META.HEADER")
        received_token = request.POST['Token']

        if token_authentication(received_token):# 토큰이 레디스에 존재 - 인증된 사용자
            status_code['SUCCESS']['data'] = const_value['SESSION_EXIST']
            return JsonResponse({'result' : status_code['SUCCESS']}, status=status.HTTP_200_OK)

        else: # 레디스에 토큰이 없음
            status_code['FAIL']['data'] = const_value['TOKEN_DOES_NOT_EXIST']
            return JsonResponse({'result' : status_code['FAIL']}, status=status.HTTP_200_OK)


@csrf_exempt
def session_destroy(request):
    if request.method == 'POST':
        received_token = request.POST['Token']

        redis_delete(received_token)

        status_code['SUCCESS']['data'] = const_value['SESSION_EXPIRE']
        return JsonResponse({'result' : status_code['SUCCESS']}, status=status.HTTP_200_OK)
