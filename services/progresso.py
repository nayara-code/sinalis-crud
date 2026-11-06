from db import consultar_db, salvar_db
from services.trilha import listar_trilhas
from services.usuario import listar_usuarios


CAMINHO_DB = "database/db_progresso.json"
CHAVE = "progresso"


def _ler_inteiro(mensagem, minimo=0, maximo=None):
    while True:
        try:
            valor = int(input(mensagem))
            if valor >= minimo and (maximo is None or valor <= maximo):
                return valor
        except ValueError:
            pass
        limite = f" e no máximo {maximo}" if maximo is not None else ""
        print(f"Informe um número inteiro entre {minimo}{limite}.")


def _proximo_id(registros):
    return max((registro.get("id", 0) for registro in registros), default=0) + 1


def registrar_progresso():
    print("\nUsuários disponíveis")
    usuarios = listar_usuarios()
    print("\nTrilhas disponíveis")
    trilhas = listar_trilhas()
    if not usuarios or not trilhas:
        print("Cadastre pelo menos um usuário e uma trilha antes de registrar progresso.")
        return

    usuario_ids = {usuario["id"] for usuario in usuarios}
    trilha_ids = {trilha["id"] for trilha in trilhas}
    while True:
        usuario_id = _ler_inteiro("ID do usuário: ", minimo=1)
        if usuario_id in usuario_ids:
            break
        print("Usuário não encontrado.")
    while True:
        trilha_id = _ler_inteiro("ID da trilha: ", minimo=1)
        if trilha_id in trilha_ids:
            break
        print("Trilha não encontrada.")

    setor = input("Setor/equipe (ex.: Atendimento, Financeiro, Tecnologia): ").strip()
    pontuacao = _ler_inteiro("Pontuação do quiz: ")
    streak = _ler_inteiro("Dias consecutivos (streak): ")
    percentual = _ler_inteiro("Percentual concluído (0 a 100): ", maximo=100)
    progressos = consultar_db(CAMINHO_DB, CHAVE)
    progressos.append(
        {
            "id": _proximo_id(progressos),
            "usuario_id": usuario_id,
            "trilha_id": trilha_id,
            "setor": setor,
            "pontuacao_quiz": pontuacao,
            "streak_dias": streak,
            "percentual_concluido": percentual,
            "certificado_emitido": percentual == 100,
        }
    )
    salvar_db(CAMINHO_DB, CHAVE, progressos)
    print("Progresso registrado com sucesso.")


def listar_progressos():
    progressos = consultar_db(CAMINHO_DB, CHAVE)
    print("\nProgressos registrados")
    if not progressos:
        print("Nenhum progresso registrado.")
    for progresso in progressos:
        print(
            f"ID: {progresso['id']} | Usuário: {progresso['usuario_id']} | "
            f"Trilha: {progresso['trilha_id']} | Setor: {progresso['setor']} | "
            f"Quiz: {progresso['pontuacao_quiz']} | Streak: {progresso['streak_dias']} dias | "
            f"Conclusão: {progresso['percentual_concluido']}% | "
            f"Certificado: {'Sim' if progresso['certificado_emitido'] else 'Não'}"
        )
    return progressos


def exibir_painel_corporativo():
    progressos = consultar_db(CAMINHO_DB, CHAVE)
    total = len(progressos)
    media = (
        sum(item.get("percentual_concluido", 0) for item in progressos) / total
        if total
        else 0
    )
    certificados = sum(bool(item.get("certificado_emitido")) for item in progressos)
    setores = {}
    for progresso in progressos:
        setor = progresso.get("setor", "Não informado")
        setores.setdefault(setor, []).append(progresso.get("percentual_concluido", 0))

    print("\nPainel corporativo de progresso e inclusão")
    print(f"Atividades monitoradas: {total}")
    print(f"Taxa média geral de conclusão: {media:.1f}%")
    print(f"Certificados emitidos: {certificados}")
    print("Média de conclusão por setor/equipe:")
    if not setores:
        print("Nenhum dado disponível.")
    for setor, percentuais in sorted(setores.items()):
        media_setor = sum(percentuais) / len(percentuais)
        print(f"- {setor}: {media_setor:.1f}%")


def atualizar_progresso():
    progressos = consultar_db(CAMINHO_DB, CHAVE)
    try:
        progresso_id = int(input("ID do progresso que deseja atualizar: "))
    except ValueError:
        print("ID inválido.")
        return
    progresso = next((item for item in progressos if item.get("id") == progresso_id), None)
    if progresso is None:
        print("Progresso não encontrado.")
        return

    print("Deixe em branco para manter o valor atual.")
    for campo, rotulo, minimo, maximo in (
        ("pontuacao_quiz", "Pontuação do quiz", 0, None),
        ("streak_dias", "Dias consecutivos", 0, None),
        ("percentual_concluido", "Percentual concluído", 0, 100),
    ):
        valor = input(f"{rotulo} [{progresso[campo]}]: ").strip()
        if valor:
            try:
                numero = int(valor)
                if numero < minimo or (maximo is not None and numero > maximo):
                    raise ValueError
                progresso[campo] = numero
            except ValueError:
                print(f"Valor inválido; {rotulo.lower()} foi mantido.")

    progresso["certificado_emitido"] = progresso["percentual_concluido"] == 100
    salvar_db(CAMINHO_DB, CHAVE, progressos)
    print("Progresso atualizado com sucesso.")


def deletar_progresso():
    progressos = consultar_db(CAMINHO_DB, CHAVE)
    try:
        progresso_id = int(input("ID do progresso que deseja remover: "))
    except ValueError:
        print("ID inválido.")
        return
    atualizados = [item for item in progressos if item.get("id") != progresso_id]
    if len(atualizados) == len(progressos):
        print("Progresso não encontrado.")
        return
    salvar_db(CAMINHO_DB, CHAVE, atualizados)
    print("Progresso removido com sucesso.")