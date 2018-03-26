# -*- coding: utf-8 -*-
from unicodedata import normalize
from lib.stop_words import substituicoes, exclusoes, pontuacoes


__all__ = ["normaliza"]


def _get_py_versao():
    from platform import python_version
    versao = python_version()
    return versao[0]


def _retira_caracteres_invalidos(string):
    for c in string:
        if ord(c) > 255:
            string = string.replace(c, '')
        elif ord(c) < 31 and ord(c) != 10:
            string = string.replace(c, '')
    return string


def _retira_espacos_duplos(string):
        while '  ' in string:
            string = string.replace('  ', ' ')
        return string


def _retira_pontuacao(string):
        for pontuacao in pontuacoes:
            string = string.replace(pontuacao, '')
        return string


def _retira_stop_words(string):
    for palavras in substituicoes:
        string = string.replace(palavras[0], palavras[1])
    for palavra in exclusoes:
        palavra = ' ' + palavra + ' '
        string = string.replace(palavra, ' ')
    return string


def _remove_acentos(string):
    if _get_py_versao() == '2':
        try:
            string = string.decode('utf-8')
        except UnicodeDecodeError:
            pass
        nkfdForm = normalize('NFKD', string)
        string = nkfdForm.encode('ASCII', 'ignore')
        return string
    return normalize('NFKD', string).encode('ASCII', 'ignore').decode('ASCII')


def normaliza(string, retirar_fim_linha=True, retirar_pontuacao=True):
    string = _retira_caracteres_invalidos(string)
    string = _remove_acentos(string)
    string = string.lower()
    string = _retira_stop_words(string)
    if retirar_fim_linha:
        string = string.replace('\n', ' ')
    if retirar_pontuacao:
        string = _retira_pontuacao(string)
    string = _retira_espacos_duplos(string).strip()
    return string
