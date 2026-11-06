from db import consultar_db, salvar_db


CAMINHO_DB = "database/db_usuario.json"
CHAVE = "user"


def _ler_opcao(mensagem, opcoes):
    while True:
        try:
            valor = int(input(mensagem))
            if valor in opcoes:
                return valor
        except ValueError:
            pass
        print("Opção inválida. Tente novamente.")


def _proximo_id(registros):
    return max((registro.get("id", 0) for registro in registros), default=0) + 1


def cadastrar_usuario():
    usuarios = consultar_db(CAMINHO_DB, CHAVE)
    print("\nCadastro de usuário")
    nome = input("Nome: ").strip()
    email = input("E-mail: ").strip()

    perfis = {
        1: "Pessoa Surda",
        2: "Ouvinte",
        3: "Professor",
        4: "Gestor Corporativo",
    }
    print("Perfil: 1. Pessoa Surda | 2. Ouvinte | 3. Professor | 4. Gestor Corporativo")
    perfil = perfis[_ler_opcao("Escolha o perfil: ", perfis)]
    empresa_escola = input("Empresa ou escola: ").strip()

    niveis = {1: "Iniciante", 2: "Intermediário", 3: "Avançado"}
    print("Nivelamento rápido: escolha o nível que melhor representa sua experiência.")
    print("1. Estou começando | 2. Já conheço o básico | 3. Tenho experiência avançada")
    nivel = niveis[_ler_opcao("Resultado do nivelamento: ", niveis)]

    usuarios.append(
        {
            "id": _proximo_id(usuarios),
            "nome": nome,
            "email": email,
            "perfil": perfil,
            "empresa_escola": empresa_escola,
            "nivel": nivel,
        }
    )
    salvar_db(CAMINHO_DB, CHAVE, usuarios)
    print("Usuário cadastrado com sucesso.")


def listar_usuarios():
    usuarios = consultar_db(CAMINHO_DB, CHAVE)
    print("\nUsuários cadastrados")
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    for usuario in usuarios:
        print(
            f"ID: {usuario['id']} | {usuario['nome']} | {usuario['email']} | "
            f"{usuario['perfil']} | {usuario['empresa_escola']} | Nível: {usuario['nivel']}"
        )
    return usuarios


def atualizar_usuario():
    usuarios = consultar_db(CAMINHO_DB, CHAVE)
    try:
        usuario_id = int(input("ID do usuário que deseja atualizar: "))
    except ValueError:
        print("ID inválido.")
        return

    usuario = next((item for item in usuarios if item.get("id") == usuario_id), None)
    if usuario is None:
        print("Usuário não encontrado.")
        return

    print("Deixe em branco para manter o valor atual.")
    for campo, rotulo in (("nome", "Nome"), ("email", "E-mail"), ("empresa_escola", "Empresa/escola")):
        valor = input(f"{rotulo} [{usuario[campo]}]: ").strip()
        if valor:
            usuario[campo] = valor

    niveis = {1: "Iniciante", 2: "Intermediário", 3: "Avançado"}
    print("Nível: 1. Iniciante | 2. Intermediário | 3. Avançado")
    opcao = input(f"Novo nível [{usuario['nivel']}] (Enter mantém): ").strip()
    if opcao:
        try:
            nivel_id = int(opcao)
            if nivel_id not in niveis:
                raise ValueError
            usuario["nivel"] = niveis[nivel_id]
        except ValueError:
            print("Nível inválido; o nível atual foi mantido.")

    salvar_db(CAMINHO_DB, CHAVE, usuarios)
    print("Usuário atualizado com sucesso.")


def deletar_usuario():
    usuarios = consultar_db(CAMINHO_DB, CHAVE)
    try:
        usuario_id = int(input("ID do usuário que deseja remover: "))
    except ValueError:
        print("ID inválido.")
        return

    atualizados = [usuario for usuario in usuarios if usuario.get("id") != usuario_id]
    if len(atualizados) == len(usuarios):
        print("Usuário não encontrado.")
        return
    salvar_db(CAMINHO_DB, CHAVE, atualizados)
    print("Usuário removido com sucesso.")