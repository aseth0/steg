from PIL import Image

# COMPROBACIONES
def CheckFormat(imagen):
    imagen = imagen.split('.')
    if imagen[1] == 'png':
        return True
    else:
        return False

def CheckImagen(imagenEntradaPng):
    try:
        Image.open(imagenEntradaPng)

        if CheckFormat(imagenEntradaPng):
            pass
        else:
            print("[*] Lo sentimos, solo podemos procesar imagenes png.")
            exit()

        print("     Imagen Correcta")
    except FileNotFoundError:
        print(f"[*] ERROR: La imagen {imagenEntradaPng} no se ha encontrado.")
        exit()


##### OBTENCION Y TRANSFORMACIÓN DEL TEXTO CLARO A BINARIO ######
def TextoClaroABinario(textoClaro):
    # Primero obtenemos el texto:
    textoEnBinario = [] #Lista para recomponer el texto en binario
    caracterDeTerminacion = [1, 1, 1, 1, 1, 1, 1, 1]
    #Extraemos los caracteres del texto:
    for caracter in textoClaro:
        # Pasamos cada caracter a Ascii
        caracterAscii = ord(caracter)
        
        # Con bin() rasamos el caracter de Ascii a binario,
        # Con [2:] le quitamos la indicación binaria de string (0b),
        # Con .zfill(8) reyenamos los huecos que faltas para el byte con 0s.
        caracterBinario = bin(caracterAscii)[2:].zfill(8)

        # Añadimos cada bit del caracter a la lista que contendrá el texto completo
        for bit in caracterBinario:
            textoEnBinario.append(bit)
       #  print('Caracter: {} | Ascii: {} | Binario: {} ({}).'.format(caracter,caracterAscii,caracterBinario,len(caracterBinario)))
    for bit in caracterDeTerminacion:
        textoEnBinario.append(bit)

    return textoEnBinario

##### CAMBIAR LOS COLORES DE LA IMAGEN #####

def CambiaUltimoBit(byteString, nuevoBit):
    return byteString[:-1] + str(nuevoBit)

# Devuelve un entero desde la representacion binaria del byte
def BinarioADecimal(byteString):
    return int(byteString, 2)

# Pasa de decimal a Binario
def SacaBinario(decimal):
    return bin(decimal)[2:].zfill(8)

# Devuelve el color modificado
def ModificarColor(colorOriginal, nuevoBit):
    colorBinario = SacaBinario(colorOriginal)
    colorModificado = CambiaUltimoBit(colorBinario, nuevoBit)
    return BinarioADecimal(colorModificado)

def HideText(imagenEntradaPng,textoClaro,imagenSalida):
    import funciones
    import os
    from PIL import Image

    #Pasamos a binario el texto claro
    textoBinario = funciones.TextoClaroABinario(textoClaro)

    # Cargamos la imagen
    imagen = Image.open(imagenEntradaPng)

    # Resolución de la imagen
    anchuraX = imagen.size[0]
    alturaY = imagen.size[1]

    # Comprobamos la cantidad de carácteres injectables en la imagen
    imagenTotalBits =  anchuraX * alturaY * 3
    posiblesCaracteres = int(imagenTotalBits/8)-1

    # Establecemos la posicion del bit (dentro de textoBinario) que queremos injectar en la imagen
    posicionTextoBin = 0
    # Cogemos el numero máximo de bits que tiene el textoBinario
    longitudTextoBin = len(textoBinario)
    print("Comprobando si el texto es injectable...")

    if longitudTextoBin <= imagenTotalBits:
        print("     CORRECTO.")

        for x in range(anchuraX):
            for y in range(alturaY):
                if posicionTextoBin < longitudTextoBin:
                    pixel = imagen.getpixel((x,y))

                    # Sacamos el valor DECIMAL de cada color del pixel
                    rojo = pixel[0]
                    verde = pixel[1]
                    azul = pixel[2]
                    alpha = pixel[3]

                    # Modificamos el color rojo
                    nuevoRojo = funciones.ModificarColor(rojo,textoBinario[posicionTextoBin])
                    posicionTextoBin += 1

                    # Modificamos el color Verde
                    if posicionTextoBin < longitudTextoBin:
                        nuevoVerde = funciones.ModificarColor(verde,textoBinario[posicionTextoBin])
                        posicionTextoBin += 1
                    else:
                        nuevoVerde = verde
                    
                     # Modificamos el color Azul
                    if posicionTextoBin < longitudTextoBin:
                        nuevoAzul = funciones.ModificarColor(azul,textoBinario[posicionTextoBin])
                        posicionTextoBin += 1
                    else:
                        nuevoAzul = azul

                    # Guardamos cada pixel con sus nuevos valores.
                    imagen.putpixel((x,y), (nuevoRojo, nuevoVerde, nuevoAzul, alpha))
                else:
                    exit = True
                    break
            if exit:
                break

            

            try:
                Image.open(imagenSalida)
                print("La imagen se ha guardado con éxito")
            except IOError:
                print(f"Error al guardar {imagenSalida}")

        print("Fin de la injeccioón.")
        imagen.save(imagenSalida, quality=95)
        print("# La nueva imagen se ha guardado en: {}/{}".format(os.getcwd(),imagenSalida))

    else:
        print("El texto es demasiado largo...")
        print("La imagen puede contener {} caracteres.".format(posiblesCaracteres))
        print("El texto que quieres ocultar tiene: {} caracteres".format(len(textoClaro)))
        exit()

#DECODIFICA LA IMAGEN

def Decode(imagen):
    # Cada 8 bits se comprueba si byteString es igual al finalString
    # Si es igual se sale el programa, si no es igual, a texto se le suma ByteATexto(byteString) y se resetea byteString
    finalString = "11111111"
    byteString = ""
    texto = ""

    CheckImagen(imagen)

    imagen = Image.open(imagen)

    anchuraX = imagen.size[0]
    alturaY = imagen.size[1]

    for x in range(anchuraX):
        for y in range(alturaY):
            pixel = imagen.getpixel((x,y))

            rojo = pixel[0]
            verde = pixel[1]
            azul = pixel[2]

            byteString += SacaBinario(rojo)[-1:]

            if len(byteString) == 8:
                if byteString == finalString:
                    exit = True
                    break
                else:
                    texto += chr(BinarioADecimal(byteString))
                    byteString = ""

            byteString += SacaBinario(verde)[-1:]

            if len(byteString) == 8:
                if byteString == finalString:
                    exit = True
                    break
                else:
                    texto += chr(BinarioADecimal(byteString))
                    byteString = ""
            
            byteString += SacaBinario(azul)[-1:]

            if len(byteString) == 8:
                if byteString == finalString:
                    exit = True
                    break
                else:
                    texto += chr(BinarioADecimal(byteString))
                    byteString = ""
        if exit:
            print("El programa ha finalizado.")
            break
    return texto