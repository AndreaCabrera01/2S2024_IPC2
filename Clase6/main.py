from os import startfile, system

class Node:
    def __init__(self, dato):
        self.dato = dato
        self.next = None

class Lista:
    def __init__(self):
        self.first = None
        self.size = 0

        # Atributos extra:
        self.rows = 0 # dimensión de filas
        self.columns = 0 # dimensión de columnas
        self.nombreMatriz = ""

    def insertar(self, data):
        nuevo = Node(data)
        if self.first == None:
            self.first = nuevo
        else:
            actual = self.first
            while actual.next != None:
                actual = actual.next
            actual.next = nuevo
        self.size +=1

    def crearGraphviz(self):
        if self.rows == 0 or self.columns == 0:
            print("Dimensiones inválidas")
            return
        
        textoDOT = ''' digraph G { \n
            node[shape=plaintext]; \n
            edge[style=invis]; \n

            label=\"nombre Matriz = '''+ self.nombreMatriz + '''\"\n
            matriz [\n label=<<TABLE border =\"1\" cellspacing=\"0\" cellpadding=\"10\">\n
            '''
        
        actual = self.first
        for i in range(self.rows):
            textoDOT += "   <tr>\n"
            for j in range(self.columns):
                textoDOT += f"<td>"+actual.dato+"</td>\n"
                actual = actual.next
            textoDOT += "   </tr>\n"

        textoDOT += ''' </TABLE>\n
            >];
        }
        '''

        # print(textoDOT)

        with open("ejemploDot1.dot", "w") as dot_file:
            dot_file.write(textoDOT)

        system('dot -Tpdf ejemploDot1.dot -o '+self.nombreMatriz+".pdf " )
        startfile(self.nombreMatriz+".pdf ")

    def crearGraphviz2(self):
        if self.rows == 0 or self.columns == 0:
            print('DIMENSIONES INVÁLIDAS:')
            return

        textoDot = ''' digraph G {
        rankdir=LR
        rankdir=TB

        subgraph cluster_1 {
            fontname=\"Century Gothic\"
            label=\"Matriz - '''+self.nombreMatriz+'''\"
            edge[dir=\"none\"]

            '''
            
            # Generar los nodos
        actual = self.first
        for i in range(self.rows):
            for j in range(self.columns):
                textoDot+= f'''
                node{i}{j} [shape=square fillcolor="gray" style=filled fontname="Century Gothic" label="{actual.dato}"]
                ''' 
                actual = actual.next   


            # Generar conexiones horizontales
        for i in range(self.rows):
            for j in range(self.columns - 1):
                textoDot += f'''
                node{i}{j} -> node{i}{j+1} [dir=none];
                '''



            # Generar conexiones verticales
        for i in range(self.rows - 1):
            for j in range(self.columns):
                textoDot += f'''
                node{i}{j} -> node{i+1}{j} [dir=none];
                '''

        # Ranks:
        for i in range(self.rows):
            textoDot += "{rank=same; "
            for j in range(self.columns):
                textoDot += f'''node{i}{j};'''
            textoDot += "}\n"

        textoDot +='''
            }
        
        }
        '''

        #print(textoDot)
        with open("EjemploDot2.dot", "w") as dot_file:
            dot_file.write(textoDot)

        system('dot -Tpdf ejemploDot2.dot -o '+self.nombreMatriz+"2.pdf " )
        startfile(self.nombreMatriz+"2.pdf ")

if __name__ == '__main__':
    lista = Lista()
    # listaTupla = tuple()
    # listaTupla2 = ()
    # listaTupla3 = (1,2,3)
    pattern = "2304006310150031"

    # 2304
    # 0063
    # 1015
    # 0031

    for num in pattern:
        lista.insertar(num)
        print("Se agregó el número: ", num, "a la lista.")

    lista.rows = 4
    lista.columns = 4
    lista.nombreMatriz = "Ejemplo"

    lista.crearGraphviz2()

