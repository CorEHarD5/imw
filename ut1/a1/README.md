# Mis Series Favoritas

 <h2>1. Carpeta series<h2>

* Primero creamos la carpeta *webapps* y dentro de ella otra carpeta *series*.

![imagen](./img/captura3.PNG)

* Después creamos el *index* que posteriormente vamos a editarlo a nuestro gusto.

![imagen](./img/captura4.PNG)

<h2>2. Location dentro de Virtual Host<h2>
* Creamos el archivo de configuración nginx *alu5604* en la ruta. */etc/nginx/sites-available/alu5604*.

![imagen](./img/captura.001.PNG)

* Una vez dentro lo editamos de la siguiente forma.

![imagen](./img/captura2.1.PNG)

>el location /blog no es necesario en esta actividad

* Nos movemos al directorio */etc/nginx/sites-enabled*

![imagen](./img/captura.002.PNG)

* Seguidamente creamos un enlace simbólico del archivo "sites-available/alu5604" a "sites-enabled/alu5604" para que pase a ser un sitio disponible.

![imagen](./img/captura.01.PNG)

* Para que cargue la configuración hay que reiniciar el servicio con el siguiente comando:

![imagen](./img/captura2.2.PNG)

<h2>3. Modificar el index <h2>

* Modificamos el archivo index para que se muestre tal y como pide en la practica.

![imagen](./img/captura4.PNG)

![imagen](./img/captura5.PNG)

<h2>4.Resultado final<h2>

![imagen](./img/captura6.PNG)

Link de la [página](alu5604.me/series)
