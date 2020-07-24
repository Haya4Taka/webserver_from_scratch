import socket  # ソケットを作成するモジュール

HOST, PORT = '', 8888

# ソケットの作成
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket(address_family, type, protocol)
# AF_INET => Address FamilyとしてIPv4を指定
# SOCK_STREAM => ソケットの種類としてストリームソケットを指定

#  作成されるソケットオブジェクト
#  <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('0.0.0.0', 0)>

#  ソケットのオプション設定
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# ソケットのタイムアウトを待たずに再利用する設定
# https://docs.python.org/ja/3/library/socket.html


# ソケットが待ち受けるアドレスとポートを指定
listen_socket.bind((HOST, PORT))


# ソケットの待ち受けを開始
listen_socket.listen(1)
#  listen([backlog])
#     backlog = 蓄えるconnect要求の数。この数を超えるとOSがエラーを出す。


print(f'Serving HTTP on port {PORT} ...')
while True:
    #  クライアントからのSYN要求に対応し、３ウェィハンドシェイクを実行する。完了すれば、コネクション用の新しいソケットを生成する。
    client_connection, client_address = listen_socket.accept()
    #  client_connection : データのやりとりで使用する新しいソケットオブジェクト
    #  <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8888), raddr=('127.0.0.1', 54862)>
    #  client_address : クライアントソケットのされたアドレスとポート

    #  クライアントからのsendで送信されたデータを読む
    request_data = client_connection.recv(1024)
    print(request_data.decode('utf-8'))

    http_response = b"""\
        HTTP/1.1 200 OK

        Hello, World!
        """

    #  データの送信
    client_connection.sendall(http_response)

    #  ソケットのクローズ
    client_connection.close()