# Sirviendo aplicaciones Php y Python

## Sitio web1

* http://php.alu5604.me

Para hacer la primera web, creamos un archivo de configuración de ngninx llamado *php*: `sudo nano php`

* Ponemos de root la ruta siguiente: `/home/alu5604/webapps/demo_php`, la cual crearemos posteriormente.

* Además añadimos un location de *php*.

![imagen](./img/web1/captura1.PNG)


Posteriormente creamos el enlace simbólico a sites enables con `ln -s`.

![imagen](./img/web1/captura2.PNG)

Después para mostrar la aplicación *demo_php* descargamos el archivo en la máquina de desarrollo.

![imagen](./img/web1/captura3.PNG)

Ahora utilizamos el comando `scp` para copiarlo a la máquina de producción.

![imagen](./img/web1/captura4.PNG)

Para comprobar que se copió vamos al *cloud* y hacemos un `ls`.

![imagen](./img/web1/captura5.PNG)

Seguidamente descomprimimos el archivo.

![imagen](./img/web1/captura6.PNG)

Ahora lo movemos a la ruta `/home/alu5604/webapps/` para que coincida con la ruta de root.

![imagen](./img/web1/captura7.PNG)

Finalmente ya solo queda reiniciar el *servicio ngninx*

![imagen](./img/web1/captura9.PNG)


![imagen](./img/web2/captura1.PNG)

![imagen](./img/web2/captura2.PNG)

![imagen](./img/web2/captura3.PNG)

![imagen](./img/web2/captura4.PNG)

![imagen](./img/web2/captura5.PNG)

![imagen](./img/web2/captura6.PNG)

![imagen](./img/web2/captura7.PNG)

![imagen](./img/web2/captura8.PNG)
