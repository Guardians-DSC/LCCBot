import paramiko


def statusByHost(host):
    status = True
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, port=23456)
        ssh.close()
    except paramiko.AuthenticationException:
        pass
    except Exception as e:
        status = False
    return status
