class BinaryTree:

    class __Node:#nos permite crear el nodo 
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left= left
            self.right = right
    
    def __init__(self):
        self.root=None  #root es raiz 


# obtiene la altura
    def height(self,root):
         if root is None:
              return-1#si no hay nada me returna -1
         else:#caso contrario me retorna la altura del arbol
              return root.height


#actualiza la altura del arbol
    def update_height(self,root):
         if root is not None:
              print(f"actualizar altura de {root.value}")
              left_height= self.height(root.left)
              right_height= self.height(root.right)
              root.height= max(left_height,right_height)+1#llamo a la funcion max y e devuelve el mayor valor 
              print(f"altura de {root.value} es {root.height}")
              print(f"altura de {root.value}es {root.height}")


    def simple_rotation(self,root,control):
        if control:
            aux=root.left
            root.left=aux.right
            aux.right=root

        else:
            aux=root.right#sacamos lo que estaba 
            root.right = aux.left#sin esta linea queda en un bucle infinito 
            #porque sirve para reacer el puntero
            aux.left=root#se movienron los nodos
        self.update_height(root)#actualizamos las altura
        self.update_height(aux)
        root=aux
        return root


#doble rotacion
    def double_rotation(self,root,control):
        if control:
            root.left=self.simple_rotation(root.left,False)#izquieda derecha
            root=self.simple_rotation(root,True)

        else:
            root.right=self.simple_rotation(root.right,True)#derecha izquierda
            root=self.simple_rotation(root,False)
        return root


#balanceo nos permite no aplicar la rotacion por mano propia 
#primero determino para donde esta desbalaciado el arbol hacia la iz o der
    def balancing (self,root):
        if root is not None:
            if self.height(root.left)- self.height(root.right)==2:#desbalancia hacia a la izquierda
                print("desbalanceado a la izquierda") 
            #detectar si aplico rotacion simple o doble
                if self.height(root.left.left)>=self.height(root.left.right):
                    print("rotar simple derecha")
                    root =self.simple_rotation(root,True)#rotacion a la derecha simple
                else:
                    print("rotar doble derecha")
                    root=self.double_rotation(root,True)#rotacion a la derecha doble
            
            elif self.height(root.right)- self.height(root.left)==2:#desbalancia hacia a la derecha
                 print("desbalancia a la derecha")
                 if self.height(root.right.right)>=self.height(root.right.left):
                    print("rotar simple izquierda")
                    root =self.simple_rotation(root,False)#rotacion a la izquierda simple
                 else:
                    print("rotar doble izquierda")
                    root=self.double_rotation(root,False)#rotacion a la izquierda doble
        return root
              





    def insert__node(self, value):
        def __insert(root,value):
            if root is None:
                return BinaryTree.__Node(value)
            elif value < root.value:
                root.left=__insert(root.left,value)
            else:
                root.right=__insert(root.right,value)
            self.balancing(root)
            self.update_height(root)#le paso esta funcion para que se vaya actualizando el arbol
            return root
            
        self.root=__insert(self.root,value)

          
#tree = BinaryTree()
#tree.insert__node(19)
#tree.insert__node(7)
#tree.insert__node(31)
#tree.insert__node(11)
#con este print muestro todos los numeros que inserto 
#print(tree.root.value, tree.root.left.value,tree.root.right.value, tree.root.left.right.value) 


#barrido del arbol
    def preorden(self):
        def __preorden(root):
            if self.root is not None:
                print(root.value) #primero muestro donde estoy parado la raiz
                a= input()  #despues me voy izq y der
                print(f"izquierda de {root.value}")
                __preorden(root.left)
                print(f"derecha de {root.value}")
                __preorden(root.right)

            if self.root is not None:
                __preorden(self.root)
#tree=BinaryTree()
#tree.insert__node(19)
#tree.insert__node(7)
#tree.insert__node(11)
#tree.insert__node(31)
#tree.insert__node(22)
#tree.insert__node(27)
#tree.insert__node(45)

    def inorden(self):
        def __inorden(root):

            if root is not None:
                __inorden (root.left)
                print(root.value)
                __inorden(root.right)

            if self.root is not None:
                 __inorden(self.root)


    def postorden (self):
        def __postorden (root):
            if root is not None:
                __postorden (root.right)
                print(root.value)
                __postorden(root.left)

        if self.root is not None:
                 __postorden(self.root)



#buscado
    def search(self, key):
        def __search(root, key):
            if root is not None:
                if root.value == key:
                    print ("lo encontre")
                    return root
                elif key < root.value:
                    print(f"buscalo a la izquierda de {root.value}")
                    return __search(root.left,key)
                else:
                    print(f"buscalo a la derecha de {root.value}")
                    return __search(root.right , key)
            else:
                print("no hay nada")

        aux=None
        if self.root is not None:
            aux =__search(self.root,key)
        return aux

#tree=BinaryTree()
#tree.insert__node(19)
#tree.insert__node(7)
#tree.insert__node(11)
#tree.insert__node(31)
#tree.insert__node(22)
#tree.insert__node(27)
#tree.insert__node(45)


#pos=tree.search(27)
#if pos:
#    print("lo encontre", pos.value)
#else:
#    print("no esta")

    def delete_node(self, value):#eliminacion
        def _replace(root):
            if root.right is None:
                print (f"no tiene derecha es el mayor{root.value}")
                return root.left, root
            else:
                print("seguir buscando nodo para reemplazar a la dercha")
                root.right, replace_node=_replace(root.right)
                return root, replace_node

        def _delete(root,value):
            #value_delete=None  # es lo mismo que abajo en el else 
            if root is not None:#b
                if root.value > value:#la raiz es menor a lo que quiero eliminar
                    print(f"buscar a la izquierda de {root.value}")
                    root.left, value_delete =_delete(root.left,value)#izquierda estoy parado en f cuando realize la llamada
                elif root.value < value:
                    print(f"buscar a la derecha de {root.value}")
                    root.right, value_delete =_delete(root.right,value)#derecha
                else:
                    print("valor encontrado")
                    value_delete=root.value#saco el valor del nodo que quiero eliminar
                    if root.left is None:#aca me tengo que asegurar que uno de las dos hojas sea vacia
                        print("a la izquierda no hay nada")
                        return root.right, value_delete
                    elif root.right is None:
                        print("a la derecha no hay nada")
                        return root.left, value_delete
                    else:
                        print("tiene ambos hijos")
                        root.left,replace_node= _replace(root.left)
                        root.value=replace_node.value
                        #return root, value_delete
                    root=self.balancing(root)
                    self.update_height(root)
            return root, value_delete   
                        
        delete_value = None
        if self.root is not None:
            self.root, delete_value= _delete(self.root, value)
        return delete_value
    
tree=BinaryTree()
tree.insert__node("L")
a=input()
tree.insert__node("D")
a=input()
tree.insert__node("B")
