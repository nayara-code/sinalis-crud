# Sinalis — Mãos que conectam mundos

O **Sinalis** é uma plataforma educacional e corporativa bilíngue que aproxima pessoas surdas e ouvintes por meio de aprendizagem visual e acessível. A proposta conecta Libras, Português escrito e línguas estrangeiras, oferecendo qualificação profissional, recursos de aprendizagem e acompanhamento de inclusão.

Este repositório contém um sistema CRUD em Python executado pelo terminal. Usuários, trilhas e registros de progresso são persistidos localmente em arquivos JSON, sem dependências externas.

## Cenário e Problema no Brasil

A exclusão comunicacional e educacional cria barreiras para a comunidade surda no acesso à educação e ao mercado de trabalho. Os dados de contexto adotados pelo projeto são:

* **10,7 milhões** de pessoas com deficiência auditiva no Brasil (IBGE).
* **85%** das empresas sem intérpretes de Libras (FENEIS).
* **7,4%** das pessoas com deficiência com Ensino Superior (IBGE).
* **89,1%** das vagas PcD concentradas em funções operacionais ou auxiliares (MTE).

Esses indicadores ajudam a contextualizar a necessidade de ampliar o acesso à comunicação, à formação e a oportunidades de desenvolvimento profissional.

## Os Cinco Pilares

1. **Gamificação adaptativa:** atividades, quizzes e streaks para incentivar a aprendizagem contínua e acompanhar resultados.
2. **Painel corporativo de progresso e inclusão:** visão de conclusão por atividade e setor, com acompanhamento de certificados.
3. **Trilhas de qualificação profissional:** percursos práticos, como Informática Básica e Cozinha e Padaria, com conteúdo acessível em Libras.
4. **Apoio bilíngue e línguas estrangeiras:** conexão entre Libras, Português e idiomas como Inglês e Espanhol em uma experiência visual.
5. **Ensino de Libras para ouvintes:** formação de colaboradores para comunicação e atendimento mais inclusivos.

## Diferenciais Competitivos

Comparativo de posicionamento do projeto frente às soluções consideradas na pesquisa:

| Funcionalidade | Sinalis | Hands Talk | LibrasLab | Lingvano |
| :--- | :---: | :---: | :---: | :---: |
| Gamificação adaptativa do letramento corporativo para surdos | Sim | Não | Não | Não |
| Painel corporativo de progresso e inclusão | Sim | Não | Não | Não |
| Trilhas de qualificação profissional | Sim | Não | Sim | Não |
| Apoio bilíngue em Libras e línguas estrangeiras | Sim | Sim | Não | Sim |
| Ensino de Libras para funcionários ouvintes | Sim | Não | Sim | Sim |

## UX Research e Descoberta (Squad 02)

A descoberta do produto considera necessidades de pessoas aprendizes, educadores e organizações:

* **Julia Ferreira (21 anos, Pessoa Surda):** auxiliar de estoque que busca qualificação acessível em Libras, aprendizado de novos idiomas e crescimento profissional para alcançar independência financeira.
* **Saulo Pereira (34 anos, Professor de Inglês):** atua em escola bilíngue e precisa de materiais visuais que conectem Libras, Português e Inglês sem dependência de áudio, além de acompanhamento pedagógico das turmas.
* **Juliana / Eduarda Albuquerque (34 anos, Gestora Corporativa):** lidera uma empresa com mais de 100 funcionários e busca capacitar gestores e integrar profissionais surdos de maneira consistente, para além do cumprimento formal da Lei de Cotas (Lei 8.213/91).

Os artefatos de descoberta incluem **Matriz CSD** (Certezas, Suposições e Dúvidas), **Mapas de Empatia** e **Jornadas do Usuário**. As jornadas cobrem desde o cadastro e nivelamento até a realização de atividades e o acompanhamento do progresso.

## Modelo de Negócios

* **B2B (empresas):** assinatura para capacitação de equipes, métricas de inclusão e formação de gestores e colaboradores.
* **B2G (governo e instituições):** licenças para apoiar a aprendizagem de estudantes surdos e a formação continuada de educadores.
* **B2C (pessoas):** acesso individual a recursos de leitura, escrita, Libras e outros idiomas no próprio ritmo.

## Estrutura do Repositório

```text
sinalis-crud/
├── database/
│   ├── db_usuario.json
│   ├── db_trilha.json
│   └── db_progresso.json
├── services/
│   ├── usuario.py
│   ├── trilha.py
│   └── progresso.py
├── .gitignore
├── db.py
├── main.py
└── README.md
```

`db.py` centraliza a leitura e a gravação JSON. Os módulos em `services/` implementam as operações de cadastro, listagem, atualização e remoção, além do painel de progresso. Os dados de exemplo ficam em `database/`.

## Execução

Requisito: Python 3 instalado. O projeto usa somente a biblioteca padrão.

```bash
python main.py
```

Use os menus no terminal para gerenciar usuários, trilhas e progresso. Os arquivos JSON são lidos e gravados em relação ao diretório de execução.

## Integrantes do Squad 02

Aline David, Ana Clara, Geraldo, Gustavo Tavares, Hanna Chateaubriand, Marcos Gabriel, Matheus Alexandre, Nayara e Thyago.
