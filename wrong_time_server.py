import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('localhost', 123))

with open('shifted_time.txt') as time_file:
    shift = int(time_file.readline())


def query_processing():
    data, addr = server.recvfrom(512)
    server.sendto(bytes(time.ctime(time.time() + shift), encoding="utf-8"),
                  addr)


try:
    while True:
        query_processing()
except Exception:
    pass
finally:
    server.close()
