# py_texto_classif

## Classificador de Assuntos em Documentos

py_texto_classif é um classificador de assuntos em documentos que faz a busca a partir de listas pré-formatadas e que considera, além da presença das palavras no texto, a distância média entre essa palavras.

O algoritmo foi desenvolvido para triagem de petições em processos eletrônicos de Execução Fiscal e inicialmente, para evitar falsos positivos nos resultados, utilizava uma busca em profundidade baseada em sequências E/OU até encontrar a frase que identificasse o assunto do texto.

Nesta nova versão, por considerar a proximidade das palavras e não a sequência exata, o classificador tem conseguido melhores resultados. Para evitar a presença de palavras que possam produzir falsos positivos, a função classificadora aceita uma lista de palavras que, se estiverem próximas ao texto, negativa o assunto, descartando-o.
