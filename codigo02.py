
import random


pronomes = ['ele', 'ela', 'nos']
verbos = ['faco', 'fico', 'como'] 
adverbios = ['nessa noite', 'ao amanhecer', 'ao entardecer', 'no dia seguinte', 'no dia anterior']
substantivos = ('casa', 'tarefa', 'jantar', 'cafe da manha', 'parque', 'pistache', 
                'ovo mechido', 'esconde esconde','redacao', 'livro')




conjugar = {
    'ficar': {
        'presente': ['faço', 'faz', 'faça', 'façamos', 'fazem'],
        'pretérito': ['fiz', 'fizeste', 'fez', 'fizemos', 'fizestes', 'fizeram'],
        'futuro': ['farei', 'farás', 'fará', 'faremos', 'fareis', 'farão'] 
    },

    'fico': {
        'presente': ['fico', 'fica', 'fique', 'ficamos', 'fiquem'],
        'pretérito': ['fiquei', 'ficaste', 'ficou', 'ficamos', 'ficastes', 'ficaram'],
        'futuro': ['ficarei', 'ficarás', 'ficará', 'ficaremos', 'ficareis', 'ficarão']
    },

    'como': {
        'presente': ['como', 'coma', 'come', 'comemos', 'comam'],
        'pretérito': ['comi', 'comeste', 'comeu', 'comemos', 'comestes', 'comeram'],
        'futuro': ['comerei', 'comerás', 'comerá', 'comeremos', 'comereis', 'comerão']
    }
}

palavra_aleatoria = lambda lista: lista[random.randint(0, len(lista)-1)]

pronome_escolhido = palavra_aleatoria(pronomes)
verbo_escolhido = palavra_aleatoria(verbos)
adverbio_escolhido = palavra_aleatoria(adverbios)
substantivo_escolhido = palavra_aleatoria(substantivos)

tempo_verbal = palavra_aleatoria(['presente', 'pretérito', 'futuro'])

conjugacao_verbal = conjugar[verbo_escolhido][tempo_verbal]
[pronomes.index(pronome_escolhido)]

frase = f"{pronome_escolhido} {conjugacao_verbal} {adverbio_escolhido} {substantivo_escolhido}"

print(frase)
