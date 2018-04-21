#!coding: utf-8
"""
本文件存放从服务配置文件
`# ！`为系统核心项
"""
# ----------------------------心跳服务--------------------------- #
# !主服务心跳通信端口
HEARTBEAT_PORT_VAR = 10000
# !主服务所在IP
SERVICE_HOST_VAR = '10.42.0.10'

# ------------------------主从通信服务--------------------------------#
# !主从服务通信端口
SLAVE_SERVICE_PORT_VAR = 11000

# ----------------------------系统配置---------------------------- #
# !本机IP
THE_MACHINE_IP = '0.0.0.0'
# 镜像服务器与从服务通讯端口
IMAGE_SERVER_SLAVE_PORT = 13000
# --------------------------------------------------------------- #
