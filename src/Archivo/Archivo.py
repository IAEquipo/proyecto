class Archivo:

    def read(self, ruta):
        with open(ruta, 'r') as leer:
            contenido = leer.read().split('\n')
        i = 0
        leer.close()
        for line in contenido:
            contenido[i] = line.split(',')
            i = i + 1

        out = list()
        for col in range(len(contenido[0])):
            aux = list()
            for line in range(len(contenido)-1):
                aux.append(contenido[line][col])
            out.append(aux)
            del aux

        return out

    def read_being(self, ruta):
        with open(ruta, 'r') as leer:
            contenido = leer.read().split('\n')
        i = 0
        for line in contenido:
            contenido[i] = line.split(',')
            i = i + 1
        leer.close()
        return contenido[:-1]

    def readOut(self, ruta):
        with open(ruta, 'r') as leer:
            contenido = leer.read().split('\n')
        i = 0
        leer.close()
        for line in contenido:
            contenido[i] = line.split(',')[:-1]
            i = i + 1
        return contenido

    def write(self, ruta, contenido):
        escribir = open(ruta , 'w')
        escribir.write(contenido)
        escribir.close()

    def copiar(self, RutaOrigen, RutaDestino):
        if os.path.exists(RutaOrigen):
            with open(RutaOrigen, 'rb') as FileOrigen:
                with open(RutaDestino, 'wb') as FileDestino:
                    shutil.copyfileobj(FileOrigen, FileDestino)
                    print("Archivo copiado")
