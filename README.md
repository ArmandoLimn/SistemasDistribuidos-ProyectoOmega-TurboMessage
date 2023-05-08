# Sistemas Distribuidos - Proyecto Omega: TurboMessage

> Elaborado por Armando Limón y Lorena Mondragón.

Repositorio que contiene el **Proyecto Omega: TurboMessage**, el cual replica la implementación de servidor/cliente de correos electrónicos programado en **Python**, y que utiliza **gRPC** y **Protocol Buffers** para asemejar su funcionalidad.

## Requerimientos Funcionales

En pocas palabras, **TurboMessage** debe replicar la funcionalidad de un servidor de correos electrónicos. A continuación, se describen los requerimientos funcionales que debe incluir el proyecto:

- [X] Para que el proyecto sea considerado, **TurboMessage** debe implementar todas sus comunicaciones usando **gRPC** y **Protocol Buffers**.
- [X] Los usuarios podrán tener una **interfaz de consola**.
   - [X] Los usuarios deben tener un **menú de opciones** (en la consola) que permita acceder a todas las funcionalidades solicitadas.
- [X] Los usuarios podrán **registrarse** de forma *persistente* en TurboMessage creando un nombre de usuario y una contraseña.
   - [X] Cada usuario de TurboMessage tiene un **identificador alfanumérico** único con el cual puede ser contactado.
- [X] Con un nombre de usuario y contraseña, los usuarios podrán **ingresar** a TurboMessage para enviar y consultar e-mails.
- [X] Para facilitar la implementación y el uso de la interfaz, un usuario **no puede tener más de 5 correos en su bandeja de entrada**.
   - Si alguien manda un correo a un usuario con una bandeja de entrada llena, el usuario emisor debe recibir un *mensaje de error indicándosele que el receptor tiene la bandeja de entrada llena*.
- [X] Para facilitar la implementación y el uso de la interfaz, un usuario **no puede tener más de 5 correos en su bandeja de salida**.
- [X] Un usuario debe poder *escribir un correo* **a cualquier otro usuario siempre y cuando el usuario exista**.
- [X] Un usuario debe poder *leer* **cualquier correo de su bandeja de entrada y/o de su bandeja de salida**.
- [X] Un usuario debe poder *borrar* **cualquier correo de su bandeja de entrada y/o de su bandeja de salida**.
- [X] Un correo tiene un identificador, un tema, un solo emisor, un solo destinatario y un cuerpo de mensaje. El **identificador del correo se debe autogenerar por el servidor**.
- [X] **No** se permite adjuntar **archivos** a los correos.
- [X] Un correo debe tener los estados: **leído** y **no leído**, y dichos estados deben ser persistentes.
- [X] Una vez que un **usuario lea por primera vez un correo**, el estado del correo debe **cambiar a leído**.
   - No debe haber ninguna otra manera de cambiar el estado de un correo.
- [X] Los correos enviados entre los usuarios deben ser persistentes (salvo que sean borrados por el usuario que los recibió).
- [X] TurboMessage App **debe poder dar servicio a $n$ usuarios concurrentemente. No deben existir condiciones de carrera**.
- [X] Para que un email se pueda enviar, el nombre de usuario del receptor debe existir.
- [X] Un usuario debe poder **enviar $k$ mensajes a cualquier otro usuario existente**.
- [X] Un usuario puede **recibir $q$ mensajes de cualquier otro usuario existente** siempre y cuando tenga espacio en su bandeja de entrada.
- [X] Un emisor puede mandar tantos mensajes como **desee sin necesidad de que el potencial receptor esté conectado/vivo/activo**.
   - [X] Los receptores **no necesitan estar en línea/conectados/vivos/activos** para que eventualmente reciban los mensajes cuando se conecten a TurboMessage.
- [X] Cuando un usuario se conecte al sistema, debe poder **recibir todos los mensajes que le enviaron en su ausencia** independientemente del número de emails que le hayan enviado (siempre y cuando tenga espacio en su bandeja de entrada).
- [X] Para facilitar la persistencia de la información, se puede asumir que el servidor nunca se apaga. Sin embargo, los clientes se podrán ejecutar y cerrar arbitrariamente y la información persistente deberá conservarse.

## Instalación de TurboMessage

1. Clona el repositorio en la nube a un repositorio local.

```powershell
git clone https://github.com/ArmandoLimn/SistemasDistribuidos-ProyectoOmega-TurboMessage
```

2. Crea un ambiente virtual (Python 3.10).

```powershell
py -m venv env
```

3. Activa el ambiente virtual.

```powershell
.\env\Scripts\activate
```

4. Instala las librerías.

```powershell
pip install -r requirements.txt
```

## Ejecución de TurboMessage

1. Abra dos terminales (recomendado: PowerShell).

2. Muévase al directorio `turbomessage` en ambas terminales.

```powershell
cd turbomessage
```

3. Ejecute el servidor de TurboMessage en una de las terminales.

```powershell
py .\turbomessage_server.py
```

4. Ejecute el cliente de TurboMessage en la otra terminal.

```powershell
py .\turbomessage_cliente.py
```