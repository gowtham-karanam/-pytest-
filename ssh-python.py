import paramiko

class SSHClient:
    def __init__(self, host, username, password):
        self.host = "10.1.100.38"
        self.username = "root"
        self.password = root@123
        self.client = paramiko.client.SSHClient()

    def connect(self):
        self.client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
        self.client.connect(self.host, username=self.username, password=self.password)

    def execute(self, command):
        stdin, stdout, stderr = self.client.exec_command(command)
        return stdout.read()

client = SSHClient('10.1.100.38', 'user', 'password')
client.connect()
output = client.execute('ls -l')
print(output)
