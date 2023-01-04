import paramiko

hostname = "127.0.0.1"
port = 22
user = "karanam"
pass = "pythoncode"

try:
    client = paramiko.SSHClient()
    client.load_sysytem_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    cleint.connect(hostname, port=port, username=user, password=pass)
    while True:
        try:
            cmd = input("$>")
            if cmd == "exit": break
            stdin, stdout, stderr = client.exec_command(cmd)
            print(stdout.read().decode())
        except KeyboardInterrupt:
            break
    client.close()
except Exception as err:
    print(str(err)) 
