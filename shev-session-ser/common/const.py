const_value = {
    'TTL' : 3600000,
    'HEADER_DOES_NOT_EXIST' : 'NO_token_in_header',
    'SESSION_EXIST' : 'Session_exist',
    'SESSION_CREATED' : 'Session_created',
    'SESSION_DOES_NOT_EXIST': 'Session does not exist',
    'TOKEN_DOES_NOT_EXIST' : 'Token does not exist'
}

status_code = {
    'SUCCESS' :{
            "code" : 1,
            "msg": "Request Sucess",
            "data": ""
    },

    'FAILURE': {
        "code": 0,
        "msg": "Request Failure",
        "data": ""
    },

    'SIGNUP_SUCCESS' : {
        "code": 1200,
        "msg": "SignUp Success",
        "data": ""
    },

    'SIGNUP_WRONG_PARAMETER': {
        "code": 1401,
        "msg": "SignUp Wrong Parameter",
        "data": ""
    },

    'SIGNUP_INVALID_EMAIL' : {
        "code": 1402,
        "msg": "SignUp Invalid Email",
        "data": ""
    },

    'USER_SIGNOUT_SUCCESS': {
        "code": 1203,
        "msg": "User signout success",
        "data": ""
    },
    'USER_SIGNOUT_FAILURE': {
        "code": 1403,
        "msg": "User signout failure",
        "data": ""
    },


    'LOGIN_SUCCESS' : {
        "code" : 2200,
        "msg" : "Login success",
        "data" : ""
    },
    'LOGIN_WRONG_PARAMETER' : {
        "code" : 2401,
        "msg" : "Login Wrong Parameter",
        "data" : ""
    },
    'LOGIN_INVALID_EMAIL' : {
        "code" : 2402,
        "msg" : "Login Invalid Email",
        "data" : ""
    },
    'LOGIN_INVALID_PASSWORD': {
        "code": 2403,
        "msg": "Login Invalid Password",
        "data": ""
    },
    'LOGIN_SESSION_EXISTS' : {
        "code" : 2304,
        "msg" : "Session Exists",
        "data" : ""
    },

    'LOGOUT_SUCCESS' : {
        "code" : 3200,
        "msg" : "Logout Success",
        "data" : ""
    },
    'LOGOUT_FAILURE' : {
        "code" : 3401,
        "msg" : "Logout Failure",
        "data" : ""
    },

    'USER_INFO_GET_SUCCESS' : {
        "code" : 4200,
        "msg" : "User information Retrieve",
        "data" : ""
    },
    'USER_INFO_GET_FAILURE' : {
        "code" : 4401,
        "msg" : "User information retrieve fail",
        "data" : ""
    },
    'USER_INFO_MODIFY_SUCCESS' : {
        "code" : 4202,
        "msg" : "User information modified success",
        "data" : ""
    },
    'USER_INFO_MODIFY_FAILURE' : {
        "code" : 4403,
        "msg" : "User information modification failure",
        "data" : ""
    },
}