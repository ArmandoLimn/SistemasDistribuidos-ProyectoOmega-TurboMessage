from colorama import Fore, Style, Cursor
from concurrent import futures
import turbomessage_pb2_grpc
import turbomessage_pb2
import threading
import grpc
import time

class TurboMessageServer(turbomessage_pb2_grpc.TurboMessageServicer):
   lock_create_user = threading.Lock()
   lock_send_mail = threading.Lock()
   lock_mail_read = threading.Lock()
   lock_read_mail_in = threading.Lock()
   lock_read_mail_out = threading.Lock()
   lock_delete_mail_in = threading.Lock()
   lock_delete_mail_out = threading.Lock()
   
   MAX_MAILS = 5
   id_mail = 1
   users = []
   inbox_per_user = {}
   outbox_per_user = {}

   def createUser(self, request, context):
      for user in TurboMessageServer.users:
         if request.username == user.username:
            return turbomessage_pb2.Status(success = False)

      TurboMessageServer.lock_create_user.acquire()
      TurboMessageServer.users.append(request)
      TurboMessageServer.inbox_per_user[request.username] = []
      TurboMessageServer.outbox_per_user[request.username] = []
      TurboMessageServer.lock_create_user.release()

      print(Style.BRIGHT + Fore.LIGHTBLACK_EX + "Usuarios registrados: " + Style.NORMAL + str(list(TurboMessageServer.users)) + Style.RESET_ALL)

      return turbomessage_pb2.Status(success = True)

   def userExists(self, request, context):
      for user in TurboMessageServer.users:
         if request.username == user.username and request.password == user.password:
            return turbomessage_pb2.Status(success = True)
      return turbomessage_pb2.Status(success = False)

   def sendMail(self, request, context):
      origin = request.sender
      destination = request.receiver

      for user in TurboMessageServer.users:
         if user.username == destination:
            TurboMessageServer.lock_send_mail.acquire()
            if len(TurboMessageServer.outbox_per_user[origin]) >= TurboMessageServer.MAX_MAILS:
               TurboMessageServer.lock_send_mail.release()
               return turbomessage_pb2.Status(success = False)
            if len(TurboMessageServer.inbox_per_user[destination]) >= TurboMessageServer.MAX_MAILS:
               TurboMessageServer.lock_send_mail.release()
               return turbomessage_pb2.Status(success = False)
            else:
               new_mail = turbomessage_pb2.Mail(id = TurboMessageServer.id_mail, sender = origin, receiver = destination, subject = request.subject, message = request.message, read = False)
               TurboMessageServer.id_mail += 1
               TurboMessageServer.outbox_per_user[origin].append(new_mail)
               TurboMessageServer.inbox_per_user[destination].append(new_mail)
               TurboMessageServer.lock_send_mail.release()
               return turbomessage_pb2.Status(success = True)
      
      return turbomessage_pb2.Status(success = False)
   
   def mailInRead(self, request, context):
      mails = TurboMessageServer.inbox_per_user[request.receiver]
      i = 0
      for mail in mails:
         if mail.id == request.id:
            TurboMessageServer.lock_read_mail_in.acquire()
            TurboMessageServer.inbox_per_user[request.receiver][i] = turbomessage_pb2.Mail(id = mail.id, sender = mail.sender, receiver = mail.receiver, subject = mail.subject, message = mail.message, read = True)            
            TurboMessageServer.lock_read_mail_in.release()
            return turbomessage_pb2.Status(success = True)
         i += 1
      
      return turbomessage_pb2.Status(success = False)

   def mailOutRead(self, request, context):
      mails = TurboMessageServer.outbox_per_user[request.sender]
      i = 0
      for mail in mails:
         if mail.id == request.id:
            TurboMessageServer.lock_read_mail_out.acquire()
            TurboMessageServer.outbox_per_user[request.sender][i] = turbomessage_pb2.Mail(id = mail.id, sender = mail.sender, receiver = mail.receiver, subject = mail.subject, message = mail.message, read = mail.read)            
            TurboMessageServer.lock_read_mail_out.release()
            return turbomessage_pb2.Status(success = True)
         i += 1
      
      return turbomessage_pb2.Status(success = False)

   def deleteMailIn(self, request, context):
      mails = TurboMessageServer.inbox_per_user[request.receiver]
      i = 0
      for mail in mails:
         if mail.id == request.id:
            TurboMessageServer.lock_delete_mail_in.acquire()
            TurboMessageServer.inbox_per_user[request.receiver].pop(i)
            TurboMessageServer.lock_delete_mail_in.release()
            return turbomessage_pb2.Status(success = True)
         i += 1

      return turbomessage_pb2.Status(success = False)
   
   def deleteMailOut(self, request, context):
      mails = TurboMessageServer.outbox_per_user[request.sender]
      i = 0
      for mail in mails:
         if mail.id == request.id:
            TurboMessageServer.lock_delete_mail_out.acquire()
            TurboMessageServer.outbox_per_user[request.sender].pop(i)
            TurboMessageServer.lock_delete_mail_out.release()
            return turbomessage_pb2.Status(success = True)
         i += 1
      
      return turbomessage_pb2.Status(success = False)

   def readMailIn(self, request, context):
      try:
         TurboMessageServer.lock_read_mail_in.acquire()
         mails = TurboMessageServer.inbox_per_user[request.username]
         for mail in mails:
            yield mail
         TurboMessageServer.lock_read_mail_in.release()
      except Exception:
         print(Style.BRIGHT + Fore.LIGHTRED_EX + "Error. " + Fore.LIGHTBLACK_EX + "No se pudo cargar la bandeja de entrada." + Style.RESET_ALL)

   def readMailOut(self, request, context):
      try:
         TurboMessageServer.lock_read_mail_out.acquire()
         mails = TurboMessageServer.outbox_per_user[request.username]
         for mail in mails:
            yield mail
         TurboMessageServer.lock_read_mail_out.release()
      except Exception:
         print(Style.BRIGHT + Fore.LIGHTRED_EX + "Error. " + Fore.LIGHTBLACK_EX + "No se pudo cargar la bandeja de salida." + Style.RESET_ALL)

def run():
   puerto = "65065"
   server = grpc.server(futures.ThreadPoolExecutor(max_workers = 10))
   turbomessage_pb2_grpc.add_TurboMessageServicer_to_server(TurboMessageServer(), server = server)
   server.add_insecure_port("[::]:" + puerto)
   server.start()
   server.wait_for_termination()

if __name__ == "__main__":
   print("\033[2J\033[1;1f") # Limpiar pantalla
   print(Cursor.FORWARD(30) + Style.BRIGHT + "¡Bienvenid@ a " + Fore.BLUE + "TurboMessage" + Fore.WHITE + "!" + Style.RESET_ALL)
   print(Cursor.FORWARD(23) + Style.BRIGHT + "¡" + Fore.BLUE + "TurboMessage" + Fore.LIGHTBLACK_EX + " Server ha iniciado con éxito! " + Style.RESET_ALL)
   run()