class Stack:
    def __init__(seft):
        seft._elements=[]

    def push(self,element):
        self._elements.append(element)

    def pop (self):
        if len (self._elements)>0:
            return self._elements.pop()
        else:
            return None
        
    def on_top(self):
        if len(self._elements)>0:
            return self._elements[-1]
        else:
            return None
        
    def size(self):
        return len(self._elements)
    