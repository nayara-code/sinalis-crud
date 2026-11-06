import json
import os


def consultar_db(caminho_arquivo, chave):
    """Retorna a lista associada à chave ou uma lista vazia."""
    if not os.path.exists(caminho_arquivo):
        return []

    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
        if not conteudo.strip():
            return []
        dados = json.loads(conteudo)
    except (OSError, json.JSONDecodeError):
        return []

    if not isinstance(dados, dict):
        return []
    registros = dados.get(chave, [])
    return registros if isinstance(registros, list) else []


def salvar_db(caminho_arquivo, chave, lista_dados):
    """Salva a lista em JSON, preservando outras chaves existentes."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
        dados = json.loads(conteudo) if conteudo.strip() else {}
        if not isinstance(dados, dict):
            dados = {}
    except (OSError, json.JSONDecodeError):
        dados = {}

    dados[chave] = lista_dados
    diretorio = os.path.dirname(caminho_arquivo)
    os.makedirs(diretorio or ".", exist_ok=True)
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)