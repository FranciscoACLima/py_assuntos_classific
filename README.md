# py_assuntos_classific

## Classificador de Assuntos em Documentos

**py_assuntos_classific** é um classificador de assuntos em documentos que faz a busca a partir de listas pré-formatadas e que considera, além da presença das palavras no texto, a distância média entre essa palavras.

O algoritmo foi desenvolvido para triagem de petições em processos eletrônicos de Execução Fiscal e inicialmente, para evitar falsos positivos nos resultados, utilizava uma busca em profundidade baseada em sequências E/OU até encontrar a frase que identificasse o assunto do texto.

Nesta nova versão, por considerar a proximidade das palavras e não a sequência exata, o classificador tem conseguido melhores resultados. Para evitar a presença de palavras que possam produzir falsos positivos, a função classificadora aceita uma lista de palavras que, se estiverem próximas ao texto, negativa o assunto, descartando-o.

Na página [py_assuntos_classif Prova de Conceito](https://github.com/FranciscoACLima/py_assuntos_classific/blob/master/py_assuntos_classific%20prova%20de%20conceito.ipynb) há notebook utilizado no desenvolvimento do algoritmo, assim como uma prova de conceito de sua utilização.

Na pasta [lib](https://github.com/FranciscoACLima/py_assuntos_classific/tree/master/lib) estão as ferramentas utilizadas na padronização do texto de entrada: retiradada da acentuação e das palavras que não alteram o sentido da frase, etc.
