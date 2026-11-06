from services.progresso import (
    atualizar_progresso,
    deletar_progresso,
    exibir_painel_corporativo,
    listar_progressos,
    registrar_progresso,
)
from services.trilha import atualizar_trilha, cadastrar_trilha, deletar_trilha, listar_trilhas
from services.usuario import atualizar_usuario, cadastrar_usuario, deletar_usuario, listar_usuarios


def menu_usuarios():
    while True:
        print("\n--- Usuários ---")
        print("1. Cadastrar  2. Listar  3. Atualizar  4. Remover  0. Voltar")
        opcao = input("Escolha uma opção: ").strip()
        acoes = {
            "1": cadastrar_usuario,
            "2": listar_usuarios,
            "3": atualizar_usuario,
            "4": deletar_usuario,
        }
        if opcao == "0":
            return
        acao = acoes.get(opcao)
        if acao:
            acao()
        else:
            print("Opção inválida.")


def menu_trilhas():
    while True:
        print("\n--- Trilhas ---")
        print("1. Cadastrar  2. Listar  3. Atualizar  4. Remover  0. Voltar")
        opcao = input("Escolha uma opção: ").strip()
        acoes = {
            "1": cadastrar_trilha,
            "2": listar_trilhas,
            "3": atualizar_trilha,
            "4": deletar_trilha,
        }
        if opcao == "0":
            return
        acao = acoes.get(opcao)
        if acao:
            acao()
        else:
            print("Opção inválida.")


def menu_progresso():
    while True:
        print("\n--- Progresso ---")
        print("1. Registrar  2. Listar  3. Painel corporativo  4. Atualizar  5. Remover  0. Voltar")
        opcao = input("Escolha uma opção: ").strip()
        acoes = {
            "1": registrar_progresso,
            "2": listar_progressos,
            "3": exibir_painel_corporativo,
            "4": atualizar_progresso,
            "5": deletar_progresso,
        }
        if opcao == "0":
            return
        acao = acoes.get(opcao)
        if acao:
            acao()
        else:
            print("Opção inválida.")


def main():
    while True:
        print("\n=== Sinalis — Mãos que conectam mundos ===")
        print("1. Usuários  2. Trilhas  3. Progresso  0. Sair")
        opcao = input("Escolha uma opção: ").strip()
        menus = {"1": menu_usuarios, "2": menu_trilhas, "3": menu_progresso}
        if opcao == "0":
            print("Até logo!")
            return
        menu = menus.get(opcao)
        if menu:
            menu()
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()