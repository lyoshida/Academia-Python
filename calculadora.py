# encoding: utf-8

"""
    Testes
    >>> calc = RPN()
    >>> calc.enter(5)
    >>> calc.visor()
    5.0
    >>> calc.pilha()
    [5.0]
    
    >>> calc.enter(10)
    >>> calc.pilha()
    [5.0, 10.0]
    >>> calc.enter('+')
    15.0
    >>> calc.visor()
    15.0
    >>> calc.pilha()
    [15.0]
    
    >>> calc.enter(5)
    >>> calc.enter(2)
    >>> calc.pilha()
    [15.0, 5.0, 2.0]
    >>> calc.enter('**')
    25.0
    >>> calc.pilha()
    [15.0, 25.0]
    >>> calc.enter('/')
    0.6
    
    >>> calc.limpapilha()
    >>> calc.pilha()
    []
    >>> calc.enter(10)
    >>> calc.pilha()
    [10.0]
    >>> calc.enter('+')
    20.0
    >>> calc.pilha()
    []
        
"""

import operator as op

class RPN():
    
    _pilha = []
    
    OPS = {'+':op.add,
             '-':op.sub,
             '*':op.mul,
             '/':op.div,
             '**':op.pow,
             }
    
    def visor(self):
        """ Retorna Visor (�ltimo elemento da pilha) """
        return self._pilha[-1]
    
    def enter(self, value):
        """ Recebe número ou operador. Se receber número guarda na ultima posicao da pilha. 
            Se receber operador, executa a operacao com os dois ultimos numeros da pilha"""
        if value not in self.OPS:
            self._pilha.append(float(value))
        elif value in self.OPS:
            if len(self._pilha)>=2:
                resultado = self.OPS[value](self._pilha[-2],self._pilha[-1])
                self._pilha.pop(),self._pilha.pop()
                self._pilha.append(resultado)
                return resultado
            elif len(self._pilha)==1:
                resultado = self.OPS[value](self._pilha[0],self._pilha[0])
                self._pilha[0] = resultado
                self.limpapilha()
                return resultado 
                
            else:
                pass
            
    def pilha(self):
        """ Mostra os itens da pilha """
        print self._pilha
    
    def limpapilha(self):
        self._pilha = []
                
if __name__ == "__main__":
    import doctest
    doctest.testmod()