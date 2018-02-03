import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = input("URL: ")

def pscan(port):
    try:
        s.connect((server,port))
        return True
    except:
        return False

print(server,"adresi taranıyor...")  #Bu işlem zaman alabilir
for x in range(1,100):
    if pscan(x):
        print(x,'numaralı port açık!')
    else:
        print(x,'numaralı port kapalı.')
