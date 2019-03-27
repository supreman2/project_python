import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 8080))
s.listen(5)

try:
    # while 1:
        conn, addr = s.accept()
        print("New connection from " + addr[0])
        try:
            //get_on(conn, addr)
        except:
            //send_answer(conn, "500 Internal Server Error", data="Ошибка")
        finally:
            conn.close()
finally:
    s.close()


