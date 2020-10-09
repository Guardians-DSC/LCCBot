import paramiko

def statusByHost(host):
  try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, port=23456)
    ssh.close()
    return True
  except Exception as e:
    return False