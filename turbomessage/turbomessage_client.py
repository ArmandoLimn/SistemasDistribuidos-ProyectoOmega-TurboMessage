from colorama import Fore, Style, Cursor
import turbomessage_pb2_grpc
import turbomessage_pb2
import grpc

MAX_MAILS = 5
g_user = []
g_mailInList = []
g_mailInListAux = []
g_mailOutList = []
g_mailOutListAux = []

with grpc.insecure_channel("localhost:65065") as channel:
   stub = turbomessage_pb2_grpc.TurboMessageStub(channel)

   def init_menu():
      print("\033[2J\033[1;1f") # Limpiar pantalla
      print(Cursor.FORWARD(30) + Style.BRIGHT + "¡Bienvenid@ a " + Fore.BLUE + "TurboMessage" + Fore.WHITE + "!" + Style.RESET_ALL)
      print("\n")
      print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "[1]" + Style.NORMAL + " - Iniciar Sesión" + Style.RESET_ALL)
      print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "[2]" + Style.NORMAL + " - Registrarse" + Style.RESET_ALL)
      print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "[3]" + Style.NORMAL + " - Salir" + Style.RESET_ALL)
      print("\n")

      option = input(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "Elija una opción: " + Style.RESET_ALL)

      flag = True
      while flag:
         if option == "1":
            flag = False
            login_menu()
         elif option == "2":
            flag = False
            register_menu()
         elif option == "3":
            exit()
         else:
            print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTRED_EX + "Error. " + Fore.LIGHTBLACK_EX + "No existe esa opción." + Style.RESET_ALL)
            option = input(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "Elija una opción: " + Style.RESET_ALL)

   def login_menu():
      print("\033[2J\033[1;1f") # Limpiar pantalla
      print(Cursor.FORWARD(30) + "Inicio de Sesión - " + Style.BRIGHT + Fore.BLUE + "TurboMessage" + Style.RESET_ALL)
      print("\n")
      username = input(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "Usuario: " + Style.RESET_ALL)
      password = input(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "Contraseña: " + Style.RESET_ALL)
      print("\n")

      user = turbomessage_pb2.User(username = username, password = password)
      exists = stub.userExists(user)

      if exists.success == True:
         main_menu(user)
      else:
         print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTRED_EX + "Error. " + Fore.LIGHTBLACK_EX + "No se pudo iniciar sesión." + Style.RESET_ALL)
         print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "Presione enter para continuar.")
         input(Cursor.FORWARD(25))
         init_menu()

   def register_menu():
      print("\033[2J\033[1;1f") # Limpiar pantalla
      print(Cursor.FORWARD(35) + "Registro - " + Style.BRIGHT + Fore.BLUE + "TurboMessage" + Style.RESET_ALL)
      print("\n")
      username = input(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "Usuario: " + Style.RESET_ALL)
      password = input(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "Contraseña: " + Style.RESET_ALL)
      print("\n")

      user = turbomessage_pb2.User(username = username, password = password)
      register = stub.createUser(user)

      if register.success == True:
         print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTGREEN_EX + "Éxito. " + Fore.LIGHTBLACK_EX + "Usuario registrado exitosamente." + Style.RESET_ALL)
         print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "Presione enter para continuar.")
         input(Cursor.FORWARD(25))
         init_menu()
      else:
         print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTRED_EX + "Error. " + Fore.LIGHTBLACK_EX + "No se pudo registrar al usuario." + Style.RESET_ALL)
         print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "Presione enter para continuar.")
         input(Cursor.FORWARD(25))
         init_menu()

   def main_menu(user):
      print("\033[2J\033[1;1f") # Limpiar pantalla
      print(Cursor.FORWARD(30) + "Menú Principal - " + Style.BRIGHT + Fore.BLUE + "TurboMessage" + Style.RESET_ALL)
      print("\n")
      print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "[1]" + Style.NORMAL + " - Bandeja de entrada" + Style.RESET_ALL)
      print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "[2]" + Style.NORMAL + " - Bandeja de salida" + Style.RESET_ALL)
      print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "[3]" + Style.NORMAL + " - Enviar un correo" + Style.RESET_ALL)
      print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "[4]" + Style.NORMAL + " - Eliminar un correo" + Style.RESET_ALL)
      print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "[5]" + Style.NORMAL + " - Salir de Turbo Message" + Style.RESET_ALL)
      print("\n")

      option = input(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "Elija una opción: " + Style.RESET_ALL)

      while True:
         if option == "":
            exit()
         elif option == "1":
            show_inbox(user)
            break
         elif option == "2":
            show_outbox(user)
            break
         elif option == "3":
            send_mail(user)
            break
         elif option == "4":
            delete_mail(user)
            break
         elif option == "5":
            exit()
         else:
            option = input(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTRED_EX + "Error. " + Fore.LIGHTBLACK_EX + "Elija otra opción: " + Style.RESET_ALL)
   
   def show_inbox(user):
      print("\033[2J\033[1;1f") # Limpiar pantalla
      print(Cursor.FORWARD(30) + "Bandeja de Entrada - " + Style.BRIGHT + Fore.BLUE + "TurboMessage" + Style.RESET_ALL)
      print("\n")
      for mail in stub.readMailIn(user):
         if mail not in g_mailInListAux:
            g_mailInListAux.append(mail)
         if mail.read == True:
            print(Cursor.FORWARD(25) + Fore.LIGHTBLACK_EX + "[ID-" + str(mail.id) + "]" + " " + mail.sender + " | " + mail.subject + Style.RESET_ALL)
         else:
            print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.WHITE + "[ID-" + str(mail.id) + "]" + " " + mail.sender + " | " + mail.subject + Style.RESET_ALL)
      print("\n")
      option = input(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "Elija una opción: " + Style.RESET_ALL)
      if option == "":
         print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTRED_EX + "Error. " + Fore.LIGHTBLACK_EX + "Presione enter para continuar" + Style.RESET_ALL)
         input(Cursor.FORWARD(25))
         main_menu(user)
      elif int(option) > 0:
         for j in range(len(g_mailInListAux)):
            if str(g_mailInListAux[j]).split("\n")[0][4:] == option:
               mail = g_mailInListAux[j]
               answer = stub.mailInRead(mail)
               if answer.success == True:
                  print("\033[2J\033[1;1f") # Limpiar pantalla
                  print(Cursor.FORWARD(30) + "Bandeja de Entrada - " + Style.BRIGHT + Fore.BLUE + "TurboMessage" + Style.RESET_ALL)
                  print("\n")
                  print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "De: " + Style.NORMAL + Fore.WHITE + mail.sender + Style.RESET_ALL)
                  print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "Para: " + Style.NORMAL + Fore.WHITE + mail.receiver + Style.RESET_ALL)
                  print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "Asunto: " + Style.NORMAL + Fore.WHITE + mail.subject + "\n" + Style.RESET_ALL)
                  print(Cursor.FORWARD(25) + mail.message + "\n" + Style.RESET_ALL)
                  print("\n")
                  input(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "Presione enter para continuar." + Style.RESET_ALL)
                  main_menu(user)
               break
            else:
               continue
      else:
         print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTRED_EX + "Error. " + Fore.LIGHTBLACK_EX + "No existe ese correo." + Style.RESET_ALL)
         print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "Presione enter para continuar" + Style.RESET_ALL)
         input(Cursor.FORWARD(25))
         main_menu(user)
      print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTRED_EX + "Error. " + Fore.LIGHTBLACK_EX + "No existe ese correo." + Style.RESET_ALL)
      input(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "Presione enter para continuar" + Style.RESET_ALL)
      main_menu(user)

   def show_outbox(user):
      print("\033[2J\033[1;1f") # Limpiar pantalla
      print(Cursor.FORWARD(20) + "Bandeja de Salida - " + Style.BRIGHT + Fore.BLUE + "TurboMessage" + Style.RESET_ALL)
      print("\n")
      for mail in stub.readMailOut(user):
         if mail not in g_mailOutListAux:
            g_mailOutListAux.append(mail)
         print(Cursor.FORWARD(25) + Fore.LIGHTBLACK_EX + "[ID-" + str(mail.id) + "]" + " " + mail.receiver + " | " + mail.subject + Style.RESET_ALL)
      option = input(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "Elija una opción: " + Style.RESET_ALL)
      if option == "":
         print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTRED_EX + "Error. " + Fore.LIGHTBLACK_EX + "Presione enter para continuar" + Style.RESET_ALL)
         input(Cursor.FORWARD(25))
         main_menu(user)
      elif int(option) > 0:
         for j in range(len(g_mailOutListAux)):
            if str(g_mailOutListAux[j]).split("\n")[0][4:] == option:
               mail = g_mailOutListAux[j]
               answer = stub.mailOutRead(mail)
               if answer.success == True:
                  print("\033[2J\033[1;1f") # Limpiar pantalla
                  print(Cursor.FORWARD(30) + "Bandeja de Salida - " + Style.BRIGHT + Fore.BLUE + "TurboMessage" + Style.RESET_ALL)
                  print("\n")
                  print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "De: " + Style.NORMAL + Fore.WHITE + mail.sender + Style.RESET_ALL)
                  print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "Para: " + Style.NORMAL + Fore.WHITE + mail.receiver + Style.RESET_ALL)
                  print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "Asunto: " + Style.NORMAL + Fore.WHITE + mail.subject + "\n" + Style.RESET_ALL)
                  print(Cursor.FORWARD(25) + mail.message + "\n" + Style.RESET_ALL)
                  print("\n")
                  input(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "Presione enter para continuar." + Style.RESET_ALL)
                  main_menu(user)
               break
            else:
               continue
      else:
         print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTRED_EX + "Error. " + Fore.LIGHTBLACK_EX + "No existe ese correo." + Style.RESET_ALL)
         print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "Presione enter para continuar" + Style.RESET_ALL)
         input(Cursor.FORWARD(25))
         main_menu(user)
      print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTRED_EX + "Error. " + Fore.LIGHTBLACK_EX + "No existe ese correo." + Style.RESET_ALL)
      input(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "Presione enter para continuar" + Style.RESET_ALL)
      main_menu(user)
      
   def send_mail(user):
      print("\033[2J\033[1;1f") # Limpiar pantalla
      print(Cursor.FORWARD(30) + "Nuevo Correo - " + Style.BRIGHT + Fore.BLUE + "TurboMessage" + Style.RESET_ALL)
      print("\n")
      if len(g_mailOutList) < MAX_MAILS:
         receiver = input(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "Destino: " + Style.RESET_ALL) 
         subject = input(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "Asunto: " + Style.RESET_ALL)
         message = input(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "Mensaje: " + Style.RESET_ALL)
         mail = turbomessage_pb2.Mail(sender = user.username, receiver = receiver, subject = subject, message = message)
         send = stub.sendMail(mail)

         if send.success == True:
            g_mailInList.append(mail)
            print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTGREEN_EX + "Éxito. " + Fore.LIGHTBLACK_EX + "Correo enviado (Presione enter para continuar)" + Style.RESET_ALL)
            input(Cursor.FORWARD(25))
            main_menu(user)
         else:
            print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTRED_EX + "Error. " + Fore.LIGHTBLACK_EX + "Correo no enviado. (Presione enter para continuar)." + Style.RESET_ALL)
            input(Cursor.FORWARD(25))
            main_menu(user)
      else:
         print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTRED_EX + "Error." + Fore.LIGHTBLACK_EX + " Limpie su bandeja de salida (Presione enter para continuar)." + Style.RESET_ALL)
         input()
         main_menu()

   def delete_mail(user):
      print("\033[2J\033[1;1f") # Limpiar pantalla
      print(Cursor.FORWARD(30) + "Eliminar Correo - " + Style.BRIGHT + Fore.BLUE + "TurboMessage" + Style.RESET_ALL)
      print("\n")
      print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "[1]" + Style.NORMAL + " - Bandeja de entrada" + Style.RESET_ALL)
      print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "[2]" + Style.NORMAL + " - Bandeja de salida" + Style.RESET_ALL)
      print("\n")
      option = input(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "Elija una opción: " + Style.RESET_ALL)
      if option == "1":
         for mail in stub.readMailIn(user):
            g_mailInListAux.append(mail)
         if len(g_mailInListAux) > 0:
            print("\033[2J\033[1;1f") # Limpiar pantalla
            print(Cursor.FORWARD(30) + "Eliminar Correo Inbox - " + Style.BRIGHT + Fore.BLUE + "TurboMessage" + Style.RESET_ALL)
            print("\n")
            for mail in stub.readMailIn(user):
               if mail.read == True:
                  print(Cursor.FORWARD(25) + Fore.LIGHTBLACK_EX + "[ID-" + str(mail.id) + "]" + " " + mail.sender + " | " + mail.subject + Style.RESET_ALL)
               else:
                  print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.WHITE + "[ID-" + str(mail.id) + "]" + " " + mail.sender + " | " + mail.subject + Style.RESET_ALL)
            print("\n")
            option = input(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "Elija una opción: " + Style.RESET_ALL)
            if option == "":
               print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTRED_EX + "Error. " + Fore.LIGHTBLACK_EX + "Presione enter para continuar" + Style.RESET_ALL)
               input(Cursor.FORWARD(25))
               main_menu(user)
            elif int(option) > 0:
               for j in range(len(g_mailInListAux)):
                  if str(g_mailInListAux[j]).split("\n")[0][4:] == option:
                     mail = g_mailInListAux[j]
                     answer = stub.deleteMailIn(mail)
                     if answer.success == True:
                        print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTGREEN_EX + "Éxito. " + Fore.LIGHTBLACK_EX + "Correo eliminado." + Style.RESET_ALL)
                        input(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "Presione enter para continuar." + Style.RESET_ALL)
                        main_menu(user)
                     else:
                        print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTRED_EX + "Error. " + Fore.LIGHTBLACK_EX + "Correo no eliminado." + Style.RESET_ALL)
                        input(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "Presione enter para continuar." + Style.RESET_ALL)
                        main_menu(user)
                  else:
                     continue
         else:
            print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "No hay correos para eliminar." + Style.RESET_ALL)
      elif option == "2":
         for mail in stub.readMailOut(user):
            g_mailOutList.append(mail)
         if len(g_mailOutListAux) > 0:
            print("\033[2J\033[1;1f") # Limpiar pantalla
            print(Cursor.FORWARD(30) + "Eliminar Correo Outbox - " + Style.BRIGHT + Fore.BLUE + "TurboMessage" + Style.RESET_ALL)
            print("\n")
            for mail in stub.readMailOut(user):
               print(Cursor.FORWARD(25) + Fore.LIGHTBLACK_EX + "[ID-" + str(mail.id) + "]" + " " + mail.sender + " | " + mail.subject + Style.RESET_ALL)
            print("\n")
            option = input(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "Elija una opción: " + Style.RESET_ALL)
            if option == "":
               print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTRED_EX + "Error. " + Fore.LIGHTBLACK_EX + "Presione enter para continuar" + Style.RESET_ALL)
               input(Cursor.FORWARD(25))
               main_menu(user)
            elif int(option) > 0:
               for j in range(len(g_mailOutListAux)):
                  if str(g_mailOutListAux[j]).split("\n")[0][4:] == option:
                     mail = g_mailOutListAux[j]
                     answer = stub.deleteMailOut(mail)
                     if answer.success == True:
                        print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTGREEN_EX + "Éxito. " + Fore.LIGHTBLACK_EX + "Correo eliminado." + Style.RESET_ALL)
                        input(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "Presione enter para continuar." + Style.RESET_ALL)
                        main_menu(user)
                     else:
                        print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTRED_EX + "Error. " + Fore.LIGHTBLACK_EX + "Correo no eliminado." + Style.RESET_ALL)
                        input(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "Presione enter para continuar." + Style.RESET_ALL)
                        main_menu(user)
                  else:
                     continue
         else:
            print(Cursor.FORWARD(25) + Style.BRIGHT + Fore.LIGHTBLACK_EX + "No hay correos para eliminar." + Style.RESET_ALL)

   if __name__ == "__main__":
      init_menu()