# # -*- coding: utf-8 -*-
import jwt, datetime
from common.const import const_value, status_code
from .logger_handler import logger
from .redis import redis_exists, redis_get
# # 토큰 관련 클래스 - 헤더에 담긴 토큰 가져오기


# 토큰 검사 (인증) - 인증된 사용자는 True, 아니면 False
def token_authentication(received_token):

    # 토큰이 레디스에 존재 - 인증된 사용자
    if redis_exists(received_token):
        print("received_token_auth_redis_get")
        logger.debug("received_token_auth_redis_get")
        print(redis_get(received_token))
        logger.debug(redis_get(received_token))
        return True

    else:
        return False

#
# # 헤더에 담긴 토큰 가져오기 (사용자가 보낸 토큰)
# def split_header_token(request):
#     logger.debug("Split_header_token 수행 시작")
#     print("split_header_token")
#     print(request.POST)
#
#     # 헤더에 토큰이 있으면 가져오고, 없으면 None
#     header_token = request.META.get('HTTP_AUTHORIZATION', None)
#
#     if header_token is None: #헤더에 토큰이 없음
#         return None
#
#     else: #헤더에 토큰이 있어서 parsing 필요
#         splited_token = header_token.split(' ')[1]
#
#         print("split header token : " + splited_token)
#         logger.debug("split header token" + splited_token)
#
#         return splited_token
