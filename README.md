# py_texto_classif

## Classificador de Assuntos em Documentos

py_texto_classif é um classificador de assuntos em documentos que procura os assuntos a partir de listas pré-formatadas e que 
considera, além da presença das palavras no texto, a distância média entre essa palavras.

Inicialmente, foi desenvolvido para triagem de petições em processos eletrônicos de Execução Fiscal e, para garantir uma maior
acuridade nos resultados, usava um algoritmo de busca sequencial que acabou tornando a configuração das listas de procura, algo
um tanto complexo.

Nesta nova versão, por considerar a proximidade das palavras e não a sequência exata, este classificador tem conseguido melhores
resultados que o anterior, baseado em uma busca sequencial.

Para evitar a presença de palavras que possam produzir falsos positivos, pode ser passado ao classificador uma lista de palavras que,
se estiverem próximas ao texto 
