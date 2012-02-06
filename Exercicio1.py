#encoding: utf-8
class Listcomps(object):
    
    mulheres = ['Mariana', 'Ana', 'Paula']
    homens = ['Pedro', 'Juca', 'Tom', 'Joaquim' ]
    
    #1. Use uma listcomp para gerar uma lista de homens com nomes de 4 ou menos letras.
    def ex1(self):
        return [x for x in self.homens if len(x)<4]
    #2. Use uma listcomp para gerar uma lista de duplas (tambem conhecida em computacaoo como uma lista associativa) formada pela letra inicial e o nome de cada homem. Por exemplo, a resposta para a lista mulheres seria:
    #[('M', 'Mariana'), ('A', 'Ana'), ('P', 'Paula')]
    def ex2(self):
        return [[x[0],x] for x in self.mulheres]
    
    #3. Use o resultado do exercicio 2 para gerar um dicionario associando iniciais aos nomes de homens. Quantos itens tera o dicionario assim produzido?
    def ex3(self):
        return dict([[x[0],x] for x in self.homens])
        #retorna 3 itens pois o identificador deve ser unico e ha duas pessoas com a mesma inicial
    
    #4. Use a funcao zip para gerar uma lista associativa, e com ela carregar um dicionario associando cada mulher a um homem. Quantos itens tera o dicionario assim produzido?
    def ex4(self):
        return dict(zip(self.mulheres,self.homens))
        #terá 3 itens
        
    #5. Bônus: Gere uma lista associativa para organizar uma aula de dança na qual todos devem dançar com todos. Quantos casais serão formados?
    #Dica: o nome da operação a ser feita neste exercício é produto cartesiano, e para fazer isso em uma listcomp ou genexp você precisa usar mais de um for dentro da expressão.
    def ex5(self):
        return [(x,y) for x in self.mulheres for y in self.homens]
    
    #6. Bônus: Repita o exercício 5, acrescentando um filtro com if para remover os nomes com menos de 4 letras das duas listas. Quantos casais serão formados?
    def ex6(self):
        return [(x,y) for x in self.mulheres for y in self.homens if len(x)>4 and len(y)>4]
