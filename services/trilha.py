from db import consultar_db, salvar_db


CAMINHO_DB = "database/db_trilha.json"
CHAVE = "trilha"


def _ler_inteiro(mensagem, minimo=1):
    while True:
        try:
            valor = int(input(mensagem))
            if valor >= minimo:
                return valor
        except ValueError:
            pass
        print(f"Informe um número inteiro maior ou igual a {minimo}.")


def _proximo_id(registros):
    return max((registro.get("id", 0) for registro in registros), default=0) + 1


def cadastrar_trilha():
    trilhas = consultar_db(CAMINHO_DB, CHAVE)
    categorias = {
        1: "Qualificação Profissional",
        2: "Apoio Bilingue",
        3: "Corporativo / Ouvintes",
    }
    print("\nCadastro de trilha")
    titulo = input("Título: ").strip()
    print("Categoria: 1. Qualificação Profissional | 2. Apoio Bilingue | 3. Corporativo / Ouvintes")
    while True:
        try:
            categoria_id = int(input("Escolha a categoria: "))
            if categoria_id in categorias:
                break
        except ValueError:
            pass
        print("Categoria inválida. Tente novamente.")
    idiomas = input("Idiomas abordados: ").strip()
    total_aulas = _ler_inteiro("Total de aulas: ")
    trilhas.append(
        {
            "id": _proximo_id(trilhas),
            "titulo": titulo,
            "categoria": categorias[categoria_id],
            "idiomas": idiomas,
            "total_aulas": total_aulas,
        }
    )
    salvar_db(CAMINHO_DB, CHAVE, trilhas)
    print("Trilha cadastrada com sucesso.")


def listar_trilhas():
    trilhas = consultar_db(CAMINHO_DB, CHAVE)
    print("\nTrilhas cadastradas")
    if not trilhas:
        print("Nenhuma trilha cadastrada.")
    for trilha in trilhas:
        print(
            f"ID: {trilha['id']} | {trilha['titulo']} | {trilha['categoria']} | "
            f"Idiomas: {trilha['idiomas']} | Aulas: {trilha['total_aulas']}"
        )
    return trilhas


def atualizar_trilha():
    trilhas = consultar_db(CAMINHO_DB, CHAVE)
    try:
        trilha_id = int(input("ID da trilha que deseja atualizar: "))
    except ValueError:
        print("ID inválido.")
        return
    trilha = next((item for item in trilhas if item.get("id") == trilha_id), None)
    if trilha is None:
        print("Trilha não encontrada.")
        return

    print("Deixe em branco para manter o valor atual.")
    for campo, rotulo in (("titulo", "Título"), ("idiomas", "Idiomas")):
        valor = input(f"{rotulo} [{trilha[campo]}]: ").strip()
        if valor:
            trilha[campo] = valor
    aulas = input(f"Total de aulas [{trilha['total_aulas']}]: ").strip()
    if aulas:
        try:
            total_aulas = int(aulas)
            if total_aulas < 1:
                raise ValueError
            trilha["total_aulas"] = total_aulas
        except ValueError:
            print("Quantidade inválida; o valor atual foi mantido.")
    salvar_db(CAMINHO_DB, CHAVE, trilhas)
    print("Trilha atualizada com sucesso.")


def deletar_trilha():
    trilhas = consultar_db(CAMINHO_DB, CHAVE)
    try:
        trilha_id = int(input("ID da trilha que deseja remover: "))
    except ValueError:
        print("ID inválido.")
        return
    atualizadas = [trilha for trilha in trilhas if trilha.get("id") != trilha_id]
    if len(atualizadas) == len(trilhas):
        print("Trilha não encontrada.")
        return
    salvar_db(CAMINHO_DB, CHAVE, atualizadas)
    print("Trilha removida com sucesso.")