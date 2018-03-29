# py_assuntos_classific

## Classificador de Assuntos em Documentos

**py_assuntos_classific** é um classificador de assuntos em documentos que faz a busca a partir de listas de palavras. Para o resultado da busca, considera, além das palavras encontradas, a distância média entre essas palavras. Quanto menor a média desta distância, melhor é o resultado.

O algoritmo foi desenvolvido para triagem de petições em processos eletrônicos de Execução Fiscal e inicialmente, para evitar falsos positivos, utilizava uma técnica de busca em profundidade baseada numa sequência E/OU. O algoritmo percorria todo o texto em busca da sequência que identificasse o assunto do texto.

Nesta nova versão, as listas de busca continuam aceitando sequências do tipo E/OU ('OU' é uma lista de palavras sinônimas).

O algoritmo, agora, normaliza o texto (retirando acentos e palavra descartáveis) e o converte em uma lista. Com esta lista "em maõs", segue a sequência abaixo:
* Primeiro procura todas as palavras independente da posição encontrada no texto e retorna suas posicoes.
* Depois cria uma matriz com as sequências possíveis destas palavras.
* Por fim, calcula a sequência com a menor distância média e, se ela estiver dentro da distância mínima definida, retorna a classe encontrada.

Por considerar a proximidade das palavras e não uma sequência exata, o classificador consegue bons resultados mas fica sujeito a ser "enganado" pela presença de palavras que podem inverter o teor do assunto. Para evitar esses "falsos positivos", a função classificadora aceita uma lista de palavras que, se estiverem próximas ou dentro da sequência das palavras encontradas, descartam o assunto encontrado.

A página [py_assuntos_classif Prova de Conceito](https://github.com/FranciscoACLima/py_assuntos_classific/blob/master/py_assuntos_classific%20prova%20de%20conceito.ipynb) é o jupyter notebook utilizado para o desenvolvimento do algoritmo e contém alguns exemplos como prova de conceito de sua aplicação.

Na pasta [lib](https://github.com/FranciscoACLima/py_assuntos_classific/tree/master/lib) estão as ferramentas utilizadas na padronização do texto de entrada: retirada da acentuação e das palavras que não alteram o sentido da frase, etc.
