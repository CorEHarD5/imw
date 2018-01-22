# Implantación de Wordpress

* Para instalar *Wordpress* necesitamos crearle un usuario y contraseña para que acceda a la base de datos.Para ello utilizaremos *Mysql*.

![imagen](./img/captura1.PNG)

* Creamos la base de datos, el usuario y le asignamos privilegios:

![imagen](./img/captura2.PNG)

* A continuación, descargamos el código fuente de *Wordpress* directamente de su página web.

![imagen](./img/captura3.PNG)

* Descomprimimos el código y lo copiamos en `/usr/share`:

![imagen](./img/captura4.PNG)

![imagen](./img/captura5.PNG)

* Ahora cambiamos el propietario de la carpeta `/usr/share/wordpress/`.

![imagen](./img/captura6.PNG)

* También debemos especificar el nombre de la base de datos, el usuario y la contraseña, para que *Wordpress* pueda usarlos (utilizamos una plantilla por defecto y cambiamos los campos necesarios):

![imagen](./img/captura7.PNG)

![imagen](./img/captura8.PNG)

![imagen](./img/captura9.PNG)

* Para que nuestro sitio *Wordpress* sea accesible desde un navegador web, debemos incluir las directivas necesarias en la configuración del servidor web *Nginx*.Para ello tendremos que crear un nuevo virtual host de la siguiente manera:

![imagen](./img/captura10.PNG)

![imagen](./img/captura11.PNG)

> corrijo el error que cometí  en el nombre del archivo.

![imagen](./img/captura12.PNG)

* Enlazamos la configuración para que el virtual host esté disponible.

![imagen](./img/captura13.PNG)

* Recargamos el servidor web Nginx.

![imagen](./img/captura14.PNG)

* Ahora podemos acceder a la dirección de nuestro servidor para configurar nuestro Wordpress vía web. (`wordpress.alu5604.me`)

![imagen](./img/captura15.PNG)

* Elegimos el idioma Español y le damos a `Continuar`:

![imagen](./img/captura16.PNG)

* Rellenamos los campos que nos piden y pulsamos `Instalar Wordpress`:

![imagen](./img/captura17.PNG)

* Pulsamos en el botón `Acceder` e ingresamos el usuario y contraseña que pusimos anteriormente:

![imagen](./img/captura18.PNG)

* Una vez dentro de la interfaz administrativa, vamos a descargarnos un tema e instalarlo.Para ello pinchamos sobre `cambia tu tema por completo`.

![imagen](./img/captura19.PNG)

* Seguidamente seleccionamos algún tema de wordpress.Y pulsamos en `Instalar y previsualizar`.

![imagen](./img/captura20.PNG)

* En mi caso es necesario instalr un plugin.

![imagen](./img/captura21.PNG)

* Una vez instalado el plugin, te lleva a una pestaña para activarlo.

![imagen](./img/captura22.PNG)

* Finalmente solo nos queda activar el tema que nos hemos descargado, para ello nos vamos a la pestaña de la izquierda llamada `Apariencia` y seleccionamos `Temas`. Una vez ahí solo tenemos que poner el cursor del ratón sobre el tema que queremos y pulsamos en `Activar`.

![imagen](./img/captura23.PNG)

* Para ver como queda el nuevo tema debemos hacer lo siguiente:

![imagen](./img/captura24.PNG)

![imagen](./img/captura25.PNG)

* Ahora vamos a configurar los enlaces permanentes.Nos situamos en el `Escritorio` de nuesto *Wordpress*.

![imagen](./img/captura26.PNG)

* Y nos vamos a la pestaña de la izquierda llamada `Ajustes` y pinchamos sobre `Enlaces permanentes`.

![imagen](./img/captura27.PNG)

* Una vez ahi seleccionamos la opción de día y nombre. Guardamos los cambios.

![imagen](./img/captura28.PNG)

![imagen](./img/captura29.PNG)

* Ahora debemos indicar a Nginx que procese estas URLs:

![imagen](./img/captura30.PNG)

![imagen](./img/captura31.PNG)

* Recargamos *Nginx*:

![imagen](./img/captura32.PNG)

* Ahora vamos a cambiar el límite de tamaño en la subida de archivos.Para incrementarlo, debemos hacer lo  siguiente, como `root` en la *máquina de producción*:

![imagen](./img/captura33.PNG)

![imagen](./img/captura34.PNG)

![imagen](./img/captura35.PNG)

![imagen](./img/captura36.PNG)

* Ahora reinciamos el servicio *php-fpm*:

![imagen](./img/captura37.PNG)

* Además de esto, debemos añadir una línea en el fichero de configuración de *Nginx*:

![imagen](./img/captura38.PNG)

![imagen](./img/captura39.PNG)

* Reiniciamos el servicio *Nginx*:

![imagen](./img/captura32.PNG)

* Ahora vamos a añadir un post con  las estadísticas de uso de *Wordpress*. Para ello pulsamos en lo siguiente:

![imagen](./img/captura40.PNG)

* A continuación, le ponemos un título y copiamos las estadísticas de *Wordpress*

![imagen](./img/captura41.PNG)

* Ya solo nos queda publicarlo.

![imagen](./img/captura42.PNG)

* Una vez publicado, nos saldra una notificación, la cual aprovecharemos para ver el resultado final del post.

![imagen](./img/captura43.PNG)

![imagen](./img/captura44.PNG)

![imagen](./img/captura45u.PNG)
