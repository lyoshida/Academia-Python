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
    >>> calc.enter('/') == 0.6
    True
    
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
    
    >>> calc.enter('a')
    'Entrada invalida.'
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
        """ Retorna Visor (ultimo elemento da pilha) """
        return self._pilha[-1]
    
    def enter(self, value):
        """ Recebe numero ou operador. Se receber numero guarda na ultima posicao da pilha. 
            Se receber operador, executa a operacao com os dois ultimos numeros da pilha"""
        if value not in self.OPS:
            if self.isnumber(value)==True:
                self._pilha.append(float(value))
            else:
                return 'Entrada invalida.'
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
            
    def pilha(self):
        """ Mostra os itens da pilha. """
        return self._pilha
    
    def limpapilha(self):
        """ Apaga pilha. """
        self._pilha = []
        
    def isnumber(self,value):
        """ Testa se value é um numero. Retorna True se for um numero. """
        try:
            float(value)
            return True
        except ValueError:
            return False
                
if __name__ == "__main__":
    import doctest
    doctest.testmod()