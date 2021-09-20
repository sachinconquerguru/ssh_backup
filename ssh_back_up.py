import paramiko
import time
import datetime
import os

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
timestamp = str(datetime.datetime.now().timestamp()).split(".")[0]
print("connecting...........")
ssh_client.connect(hostname="127.0.0.1",port=22,
		username="sachin",password="1234")
print("compressing....................")
stdin,stdout,stderr = ssh_client.exec_command("tar -cvf backup"+timestamp+".bz2 temp/\n")
print(stdout.read().decode())
time.sleep(2)
print("copying zib file to home ")
os.system("scp sachin@127.0.0.1:/home/sachin/sac/main_projec/seperate_proj/backup.bz2 ~/backups1")