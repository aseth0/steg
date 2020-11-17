import funciones
try: 
    from PIL import Image
except ImportError:
    print("ERROR: Es necesario instalar 'PILLOW'\nPARA INSTALARLO PRUEBA: pip -m install pip")

import sys

menu = "STEG.PY\n -e)\t Para codificar el texto.\n      steg.py -e ImagenEntrada -f|-s TextoEntrada ImagenSalida \n\n \t\t -f|--InputFile\t Si la cadena de texto se encuentra dentro de un archivo.\n \t\t -s|--InputString\t Si la cadena de texto se va a introducir directamente.\n\n-d)\t Para decodificar el texto.\n       steg.py -d ImagenEncodeada -f|-s SalidaDelTexto \n\n \t\t -f|--OutputFile\t Si la salida se va a guardar en un archivo.\n \t\t -s|--OutputString\t Si la salida va a salir directamente por pantalla."

try:
    argumento = sys.argv[1]
    if argumento == '-e':

        print("--------\nENCODE")
         # ARGUMENTO 2, LA IMAGEN
        imagenEntradaPng = sys.argv[2]
        if funciones.CheckImagen(imagenEntradaPng):
            imagen = Image.open(imagenEntradaPng)

        #ARGUMENTOS 3 Y 4, EL TEXTO
        procedenciaInput = sys.argv[3]
        inputTexto = sys.argv[4]
        if (procedenciaInput == "-f") or (procedenciaInput == "--InputFile"):
            try:
                    textoClaro = open(inputTexto, 'r')
                    textoClaro = textoClaro.read()
                    print("     Texto claro correcto")
            except FileNotFoundError:
                print(f"[*] ERROR: El archivo '{inputTexto}' no se encuentra.")
                exit()

        elif (procedenciaInput == "-s") or (procedenciaInput == '--InputString'):

            print("     Texto claro correcto.")
            textoClaro = inputTexto


        # ARGUMENTO 5, LA SALIDA
        try:
            imagenSalida = sys.argv[5]
            if funciones.CheckFormat(imagenSalida):
                pass
            else:
                print("[*] Lo sentimos, solo podemos procesar imagenes png.")
        except IndexError:
            print("[*] ERROR: No hay imagen de salida.")
            exit()

        funciones.HideText(imagenEntradaPng,textoClaro,imagenSalida)

    elif argumento == '-d':
        print("----\nDECODE")
        imagen = sys.argv[2]
        texto = funciones.Decode(imagen)

        formaOut = sys.argv[3]

        print("Aqui llega")

        if (formaOut == "-f") or (formaOut == "--OutputFile"):
            finalOut = sys.argv[4]
            archivo = open(finalOut, "w")
            archivo.write(texto)

        elif (formaOut == "-s") or (formaOut == "--OutputString"):
            print(f"EL TEXTO ES: {texto}")
    else:
        print("[*] ERROR: Argumento inválido.")

except IndexError:
    print(menu)
    exit()

        
