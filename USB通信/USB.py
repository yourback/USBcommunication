from socket import *
from threading import *

client_socket = None


def client_send(conn):
    while True:
        sd = input('发送内容：')
        conn.sendall(bytes(sd, encoding='utf-8'))


def client_recv(conn):
    while True:
        rd = conn.recv(1024)
        print('\r收到数据：' + str(rd, encoding='utf-8') + '\n发送内容：', end='')
        # print('发送内容：', end='')
        if not rd:
            print('连接断开')
            conn.close()
            break


def main():
    global client_socket
    print('启动')
    client_socket = socket(AF_INET, SOCK_STREAM)

    client_socket.connect(('127.0.0.1', 5000))

    tr = Thread(target=client_recv, args=(client_socket,))
    ts = Thread(target=client_send, args=(client_socket,))
    tr.start()
    ts.start()
    tr.join()
    ts.join()


if __name__ == '__main__':
    main()
