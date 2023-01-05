# Downloading a file from remote machine

ftp_client=ssh_client.open_sftp()
ftp_client.get('remotefileth','localfilepath')
ftp_client.close()



# Uploading file from local to remote machine

ftp_client=ssh_client.open_sftp()
ftp_client.put('localfilepath','remotefilepath')
ftp_client.close()
