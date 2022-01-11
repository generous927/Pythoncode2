#coding=utf-8

HOST = '92.168.1.104'
PORT = '22'
USER = 'stt5'
PASSWD = 'stt5200'
PACKAGE_DIR = r'f:\tmp\restapi-teach.zip'

import paramiko
import sys

#创建SSHClient实例对象（客户端对象）
ssh = paramiko.SSHClient()

#信任远程机器，允许访问
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#连接远程机器 地址、端口、用户名密码
ssh.connect(PORT,PORT,USER,PASSWD)

def remoteRun(cmd,printOutput=True):
    stdin, stdout, stderr = ssh.exec_command(cmd)
    output = stdout.read().decode('utf8')
    errinfo = stderr.read().decode()
    if printOutput:
        print(output+errinfo)
    return output+errinfo

#----------------------------
#检查是否有先前的版本运行
print('检查是否有先前的版本运行')
output = remoteRun('ps -ef|grep apiteach|grep -v grep')


#如果存在，则杀死进程
if 'python3 project/cherry_startup.py apiteach' in output:
    print('服务运行中，停止服务...')
    #获取进程id
    parts = output.split('')

    parts = [part for part in parts if part]

    pid = parts[1]

    #杀死进程
    ssh.exec_command('kill -9{pid}')


#远程执行命令
ssh.exec_command('mkdir houge')#mkdir是创建目录的命令
ssh.exec_command('echo "ip = 192.168.1.2" > cfg.py')#创建文件，在里面输入内容，直接用echo重定向，用vi比较麻烦

#输出的返回值分别是三个变量：标准输入、输出正常信息、输出错误信息
stdin,stdout,stderr = ssh.exec_command('ps -ef|grep apiteach|grep -v grep')#检查是否有以前版本的产品在运行，如果有，需要停止
output = stdout.read().decode()

if 'python3 project/cherry_startup.py apiteach' in output:
    print('老版本程序运行中。。。准备杀死')

    parts = output.split('')
    parts = [part for part in parts if part]

    pid = parts[1]
    ssh.exec_command('kill -9{pid}')

#删除原来的代码包
ssh.exec_command('rm -f restapi-teach.zip')

#上传新的安装包
sftp = ssh.open_sftp()#打开一个用来上传的对象
sftp.put(r'f:\tmp\restapi-teach.zip','/home/stt5/restapi-teach.zip')
sftp.close()

#备份原来的安装目录
ssh.exec_command('rm -f restapi-teach.bak;mv restapi-teach restapi-teach.bak')

#解压安装包
ssh.exec_command('unzip restapi-teach.zip',printOutput=False)

#运行
ssh.exec_command('cd restapi-teach;chomd +x run.sh;dos2unix run.sh;./run.sh;sleep 5')

#检查是否运行成功
output = ssh.exec_command('ps -ef|grep apiteach|grep -v grep')
if 'python3 project/cherry_startup.py apiteach' in output:
    print('运行成功')




#批量创建20个文件以及写入内容，复用性比较高
# for x in range(20):
#     ssh.exec_command('echo "ip = 192.168.1.{X+1}" > cfg_{X+1}.py')
