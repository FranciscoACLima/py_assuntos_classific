# py_assuntos_classific

## Classificador de Assuntos em Documentos

**py_assuntos_classific** é um classificador de assuntos em documentos que utiliza em suas buscas listas pré-formatadas e considera, além da presença das palavras no texto, a distância média entre essa palavras como forma de identificar os assuntos presentes texto.

O algoritmo foi desenvolvido para triagem de petições em processos eletrônicos de Execução Fiscal e inicialmente, para evitar falsos positivos nos resultados, utilizava uma busca em profundidade baseada em sequências E/OU que percorriam todo o texto até encontrar a frase que identificasse o assunto do texto.

Nesta nova versão, o algoritmo continua aceitando lista do tipo E/OU (no caso OU equivale a uma lista de palavras sinônimas), mas agora, está dividido em fases:
* Na primeira procura todas as palavras independente da posição encontrada no texto
* Depois cria uma matriz com as sequências possíveis destas palavras
* Por fim, calcula a sequência com a menor distância média e, se ela estiver dentro da distância mínima definida, retorna a classe encontrada.

Por considerar a proximidade das palavras e não a sequência exata, o classificador tem conseguido melhores resultados. Mas para evitar falsos positivos, a função classificadora aceita uma lista de palavras que, se estiverem próximas ou dentro da sequência de palavras encontradas, negativa o assunto, descartando-o.

Na página [py_assuntos_classif Prova de Conceito](https://github.com/FranciscoACLima/py_assuntos_classific/blob/master/py_assuntos_classific%20prova%20de%20conceito.ipynb) há notebook utilizado no desenvolvimento do algoritmo, assim como uma prova de conceito de sua utilização.

Na pasta [lib](https://github.com/FranciscoACLima/py_assuntos_classific/tree/master/lib) estão as ferramentas utilizadas na padronização do texto de entrada: retiradada da acentuação e das palavras que não alteram o sentido da frase, etc.
