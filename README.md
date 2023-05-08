# Sistemas Distribuidos - [X] Proyecto Omega - [X] TurboMessage

## TurboMessage

- [X] En pocas palabras, **TurboMessage** debe replicar la funcionalidad de un servidor de e-mails con ciertas reestricciones descritas a continuación.
- [X] Para que el proyecto sea considerado, **TurboMessage** debe implementar todas sus comunicaciones usando **gRPC** y **Protocol Buffers**.
- [X] Los usuarios podrán tener una **interfaz de consola**.
- [X] Los usuarios deben tener un **menú de opciones** (en la consola) que permita acceder a todas las funcionalidades solicitadas.
- [X] Los usuarios podrán **registrarse** de forma *persistente* en TurboMessage creando un nombre de usuario y una contraseña.
- [X] Con un nombre de usuario y contraseña, los usuarios podrán **ingresar** a TurboMessage para enviar y consultar emails.
- [X] Para facilitar la implementación y el uso de la interfaz, un usuario **no puede tener más de 5 correos en su bandeja de entrada**. Si alguien manda un correo a un usuario con una bandeja de entrada llena, el usuario emisor debe recibir un *mensaje de error indicándosele que el receptor tiene la bandeja de entrada llena*.
- [X] Para facilitar la implementación y el uso de la interfaz, un usuario **no puede tener más de 5 correos en su bandeja de salida**.
- [X] Un usuario debe poder *escribir un correo* **a cualquier otro usuario siempre y cuando el usuario exista**.
- [X] Un usuario debe poder *leer* **cualquier correo de su bandeja de entrada y/o de su bandeja de salida**.
- [X] Un usuario debe poder *borrar* **cualquier correo de su bandeja de entrada y/o de su bandeja de salida**.
- [X] Un correo tiene un identificador, un tema, un solo emisor, un solo destinatario y un cuerpo de mensaje. El **identificador del correo se debe autogenerar por el servidor**.
- [X] **No** se permite adjuntar **archivos** a los correos.
- [X] Un correo debe tener los estados: **no leído** y **leído**, y dichos estados deben ser persistentes.
- [X] Una vez que un **usuario lea por primera vez un correo**, el estado del correo debe **cambiar a leído**. No debe haber ninguna otra manera de cambiar el estado de un correo.
- [X] Los correos enviados entre los usuarios deben ser persistentes (salvo que sean borrados por el usuario que los recibió).
- [X] TurboMessage App **debe poder dar servicio a $n$ usuarios concurrentemente. No deben existir condiciones de carrera**.
- [X] Para que un email se pueda enviar, el nombre de usuario del receptor debe existir.
- [X] Cada usuario de TurboMessage tiene un **identificador alfanumérico** único con el cual puede ser contactado.
- [X] Un usuario debe poder **enviar $k$ mensajes a cualquier otro usuario existente**.
- [X] Un usuario puede **recibir $q$ mensajes de cualquier otro usuario existente** siempre y cuando tenga espacio en su bandeja de entrada.
- [X] Los receptores **no necesitan estar en línea/conectados/vivos/activos** para que eventualmente reciban los mensajes cuando se conecten a TurboMessage.
- [X] Un emisor puede mandar tantos mensajes como **desee sin necesidad de que el potencial receptor esté conectado/vivo/activo**.
- [X] Cuando un usuario se conecte al sistema, debe poder **recibir todos los mensajes que le enviaron en su ausencia** independientemente del número de emails que le hayan enviado (siempre y cuando tenga espacio en su bandeja de entrada).
- [X] Para facilitar la persistencia de la información, se puede asumir que el servidor nunca se apaga. Sin embargo, los clientes se podrán ejecutar y cerrar arbitrariamente y la información persistente deberá conservarse.
- **NOTA:** No se tomará en cuenta la estética de las interfaces gráficas. De hecho, se espera que el cliente utilice como interfaz la consola. Sin embargo, la interfaz debe ser usable y sin errores que afecten la interacción con el usuario.


## Criterios de evaluación:

- Equipo de 1 a 3 personas.
- Peso total del proyecto: 20% de su calificación final.
- Ejecución del proyecto con todos los requerimientos indicados en su descripción (18%).
- Calidad y presentación de la documentación (2%).
- Fecha de entrega de software funcional, documentación y código fuente **Miércoles 10 de Mayo de 2023** a la hora de clase.
- **NOTA 1:** 20% por cada día natural de retraso.
- **NOTA 2:** Si se entrega después de la hora de entrega, en automático aplica un día menos.