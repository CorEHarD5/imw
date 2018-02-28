        <?php
            $salario = (float)$_POST["salario"];
            $edad = (float)$_POST["edad"];
            $nombre = $_POST["nombre"];

            if ($salario > 2000){
                $salario = $salario;
            }
            elseif ($salario >= 1000 and $salario <= 2000) {
                if ($edad > 45) {
                    $salario = $salario + ($salario * 0.03);
                }
                else{
                    $salario = $salario + ($salario * 0.10);
                }
            }
            else{
                if ($edad < 45 ) {
                    $salario = 1100;
                }
                elseif ($edad >= 30 and $edad <= 45) {
                    $salario = $salario + ($salario * 0.03);
                }
                else{
                    $salario = $salario + ($salario * 0.15);
                }
            }
           echo ("La persona llamada <b>$nombre</b> y con la edad <b>$edad</b> cobrará <b>$salario</b> €.");
        ?>
