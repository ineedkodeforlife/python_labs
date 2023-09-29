import server
import collector

# em_adress, msg = input('Введите адрес электронной почты, на который хотите отправить сообщение\n'), \
#     input('Введите сообщение, которое вы хотите отправить\n')

status = "OK"

while status == 'OK':
    em_adress, msg = input('Введите адрес электронной почты, на который хотите отправить сообщение\n'), \
        input('Введите сообщение, которое вы хотите отправить\n')
    status = server.verify_server(em_adress, msg)
