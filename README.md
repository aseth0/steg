# Steg
Hide plain text files in a PNG image

# The  OWN requirement 

                  pip install pillow
				  
<h2>USAGE</h2>

	-e)     Para codificar el texto.
      steg.py -e ImagenEntrada -f|-s TextoEntrada ImagenSalida 

                 -f|--InputFile  Si la cadena de texto se encuentra dentro de un archivo.      
                 -s|--InputString        Si la cadena de texto se va a introducir directamente.

	-d)      Para decodificar el texto.
       steg.py -d ImagenEncodeada -f|-s SalidaDelTexto 

                 -f|--OutputFile         Si la salida se va a guardar en un archivo.
                 -s|--OutputString       Si la salida va a salir directamente por pantalla.    
		 
Si queremos guardar Codigo en una imagen, basta con poner el nombre del archivo en la opción de ENCODE:
			Ej: Steg.py -e ImagenEntrada.png -f CodigoEntrada.bat ImagenSalida.png

De igual manera si el texto a sacar es código, se puede guardar en un archivo directamente escribiendo el nombre y la extensión del archivo en la opcion de DECODE:
			Ej: Steg.py -d ImagenConTexto.png -f CodigoSalida.bat
			

