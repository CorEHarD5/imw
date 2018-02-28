    <head>
        <meta charset="utf-8">
        <title>ejercicio2</title>
    </head>
    <body>
        <form action="ejercicio4.php" method="post">
            <label for="filas">¿Cuántas filas?</label>
            <input type="text" name="filas"/><br>
            <label for="columnas">¿Cuántas columnas?</label>
            <input type="text" name="columnas"/><br>
            <input type="submit" value="enviar"/>
        </form>
        <?php
            $filas = (int)$_POST["filas"];
            $columnas = (int)$_POST["columnas"];

            if ($filas < 1 or $columnas < 1){
                echo ("<p style='color:red;'>Como mínimo debe haber 1 fila y 1 columna</p>");
            }
            else{
                echo("<table border='1px'>");
                for ($i=1;$i<=$filas;$i++){
                    echo ("<tr>");
                    for ($j=1;$j<=$columnas;$j++){
                        echo("<td>columna $j</td>");
                    }
                    echo("</tr>");
                }
                echo("</table>");
            }
        ?>
    </body>
