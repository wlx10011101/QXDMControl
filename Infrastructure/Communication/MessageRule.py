# coding=utf-8
ALL_IP_OF_HOST = '0.0.0.0'
CLIENT_PORT = 8088
SERVER_PORT = 8089
MESSAGE = {
    "ClientRegister": "Register {0}",
    "RegisterSucc": "Client {0} Register Success",
    "ExcuteResult": "ExcuteResult {0}",
    "UeAttach": "QxdmCmd ue_attach",
    "UeDetach": "QxdmCmd ue_dettach",
    "ClientRegisterAgain": 'ClientRegisterAgain',
    }

MESSAGEREX = {
    "ClientRegister": "Register (.+)$",
    "RegisterSucc": "Client (.+) Register Success",
    "QxdmCmd": "QxdmCmd (.*)$",
    "ExcuteResult": "ExcuteResult (.+)$",
    "ClientRegisterAgain": 'ClientRegisterAgain',
    }
