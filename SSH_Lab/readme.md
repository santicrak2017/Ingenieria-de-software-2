# Metodo SSH
## -**Introduccion:**
---
Durante la clase hemos visto varias maneras en la que podremos asegurar de una mejor manera nuestra información como JSON, Pero se miro una nueva alternativa como lo es SSH.

Este es una protocolo en el cual permite al cliente y servidor ponerse de acuerdo para un metodo de autenticación , con el cual los dos dispositivos de podran comunicar y de esa manera poder tener una conexión segura de los archivos que se vayan transmitiendo.

La manera en la que funciona el protocolo esta basado en:
### - **Establecimiento de la conexión**
  Cuando el cliente (tu PC) se conecta al servidor:

Se ponen de acuerdo en:
  Algoritmos de cifrado 
  Algoritmos de hash 
  Se crea una clave de sesión usando criptografía como Diffie-Hellman


### -**Autenticación**
  aquí el servidor verifica tu identidad. Hay dos formas principales:

  Usuario + contraseña
  Más simple, pero menos seguro
  Llaves públicas/privadas (lo que mencionaste)


### -**Canal de cifrado**
  En donde vamos a enviar y recibir archivos, contraseñas e informacion de interes cifrada.

---
# Proceso de instalación.
Si estamos en linux, pues ya tenemos un cliente SH , entonces no debemos crear uno como lo tendriamos que hacer en windows
![Descripción de la imagen](SSH_Lab/VirtualBox_2024_Logo.svg.png)
