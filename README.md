# Steg
Aplicación hecha en python para ocultar texto en imágenes png

La aplicación no soporta imágenes de ningún otro tipo, aún soy Junior y necesito práctica :c

-e)     Para codificar el texto.
      steg.py -e ImagenEntrada -f|-s TextoEntrada ImagenSalida 

                 -f|--InputFile  Si la cadena de texto se encuentra dentro de un archivo.      
                 -s|--InputString        Si la cadena de texto se va a introducir directamente.

-d)      Para decodificar el texto.
       steg.py -d ImagenEncodeada -f|-s SalidaDelTexto 

                 -f|--OutputFile         Si la salida se va a guardar en un archivo.
                 -s|--OutputString       Si la salida va a salir directamente por pantalla.    
