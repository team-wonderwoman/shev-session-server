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
