from socket import *
import datetime

# إعدادات الخادم
serverPort = 5000  # تغيير المنفذ لتجنب التداخل
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)  # زيادة عدد الاتصالات المسموح بها

print(f'The server is listening on localhost : {serverPort}')
print('-----------------------------------------------------')

while True:
    try:
        connectionSocket, addr = serverSocket.accept()
        print('Client connected from', addr)
        
        request_count = 0  # عداد الطلبات

        while True:
            try:
                sentence = connectionSocket.recv(1024)
                if not sentence:
                    break  # إذا لم يتم استلام أي بيانات، نغلق الاتصال
                request_count += 1  # زيادة عدد الطلبات
                numOfCharacters = len(sentence)
                connectionSocket.send(str(numOfCharacters).encode())
                print(f'--> message received and processed on {datetime.datetime.now()} | Total requests from this client: {request_count}')
            except Exception as e:
                print(f'Error during data reception: {e}')
                break

        connectionSocket.close()
        print(f'Connection closed with {addr} | Total requests received: {request_count}')
        print('-----------------------------------------------------')

    except Exception as e:
        print(f'Error: {e}')