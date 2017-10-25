# Sirviendo aplicaciones Php y Python

## Sitio web1

> * http://php.alu5604.me

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

Finalmente ya solo queda reiniciar el *servicio ngninx*:

![imagen](./img/web1/captura2.2.PNG)

Ahora vamos a al navegador y probamos la dirección.

![imagen](./img/web1/captura9.PNG)

## Sitio web2

> * http://now.alu5604.me

Para hacer la segunda web, creamos un archivo de configuración de ngninx llamado *now*: `sudo nano now`

![imagen](./img/web2/captura6.PNG)

Posteriormente hacemos el enlace simbólico en *sites-enable* al igual que en todas la prácticas anteriores.

![imagen](./img/web2/captura2.PNG)

Reiniciamos el servicio *nginx*.

![imagen](./img/web2/captura2.2.PNG)

A continuación creamos un entorno virtual.

![imagen](./img/web2/captura3.PNG)

* Instalamos los siguientes paquetes:
  * *uwsgi*
  * *flask*
  * *pytz*


![imagen](./img/web2/captura4.PNG)

![imagen](./img/web2/captura20.PNG)

![imagen](./img/web2/captura21.PNG)

A continuación creamos fichero en *python*, dentro de la carpeta now que creamos,este va a contener el código de la aplicación web.

![imagen](./img/web2/captura5.PNG)

`nano main.py`

![imagen](./img/web2/captura19.PNG)

En este punto podemos lanzar el proceso para escuchar peticiones.
![imagen](./img/web2/captura7.PNG)

Por esto vamos a un navegador y probamos la dirección. (Utilizando el puerto 8080 que definimos en el proceso anterior).

![imagen](./img/web2/captura8.PNG)

Después de haber salido del entorno virtual (mediante `deactivate`) creamos un fichero de configuración para *uWSGI* dentro de la carpeta `now`.

![imagen](./img/web2/captura9.PNG)

![imagen](./img/web2/captura10.PNG)

Ahora tenemos que crear un  script llamado `run.sh` que será el encargado de activar el entorno virtual de nuestra aplicación y de lanzar el proceso *uwsgi* para que escuche peticiones en el socket especificado.

![imagen](./img/web2/captura11.PNG)

Para que se pueda ejecutar le modificamos los permisos.

![imagen](./img/web2/captura12.PNG)

En este punto lanzamos el script sin necesidad de activar el entorno virtual.

![imagen](./img/web2/captura14.PNG)

Vamos a un navegador y comprobamos que esta funcionando correctamete.

![imagen](./img/web2/captura15.PNG)

Ahora creamos un supervisor.
Vamos a la siguiente ruta(`/etc/supervisor/conf.d/`) y hacemos un archivo de configuración de supervisor `now.conf`.

![imagen](./img/web2/captura16.1.PNG)

![imagen](./img/web2/captura16.PNG)

Iniciamos el supervisor:

![imagen](./img/web2/captura22.PNG)

Realizamos los siguientes comandos de comprobación.

![imagen](./img/web2/captura18.PNG)


Comprobamos el resultado final mirando la página en un navegador solo con el supervisor activo,

![imagen](./img/web2/captura17.PNG)
