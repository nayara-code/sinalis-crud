# Sinalis — Mãos que conectam mundos 🤟

O **Sinalis** é uma plataforma educacional e corporativa voltada para a inclusão, qualificação profissional e ensino bilíngue (Libras, Português e línguas estrangeiras) para pessoas surdas e ouvintes. Este repositório contém o sistema CRUD em Python que gerencia os usuários, trilhas de aprendizagem e métricas de inclusão corporativa do projeto.

## Cenário e Problema

No Brasil, a exclusão comunicacional e educacional gera barreiras severas para a comunidade surda no mercado de trabalho e na sociedade:

* **População impactada:** 10,7 milhões de pessoas possuem algum grau de deficiência auditiva no país (IBGE).
* **Barreira corporativa:** 85% das empresas não possuem intérpretes de Libras (FENEIS).
* **Escolaridade:** Apenas 7,4% das pessoas com deficiência concluíram o Ensino Superior (IBGE).
* **Estagnação profissional:** 89,1% das vagas para PcD concentram-se em funções operacionais e auxiliares (MTE).

Esses fatores resultam diretamente em isolamento social, estagnação de carreira e vulnerabilidade socioeconômica.

## Nossa Solução

O Sinalis atua na ponta educacional e corporativa por meio de cinco pilares principais:

* **Gamificação adaptativa:** Módulos interativos, desafios diários, *quizzes* e controle de ofensiva (*streak* de acertos) para manter o engajamento no letramento corporativo e no aprendizado de sinais.
* **Painel corporativo de progresso e inclusão:** Acompanhamento de metas trimestrais de inclusão, emissão de certificados e progresso segmentado por equipes (como Atendimento, Financeiro e Tecnologia).
* **Trilhas de qualificação profissional:** Cursos práticos e acessíveis em Libras (ex.: Informática Básica, Cozinha e Padaria) voltados para a empregabilidade e ascensão de carreira.
* **Apoio bilíngue e línguas estrangeiras:** Ensino visual que conecta Libras (L1), Português escrito (L2) e idiomas estrangeiros como Inglês e Espanhol (L3) com vídeos de sinais validados.
* **Ensino de Libras para ouvintes:** Capacitação de colaboradores ouvintes com foco em atendimento, cultura inclusiva e boas práticas de comunicação no dia a dia.

## Diferenciais Competitivos

Comparativo de funcionalidades entre o Sinalis e outras soluções do mercado:

| Funcionalidade | Sinalis | Hands Talk | LibrasLab | Lingvano |
| :--- | :---: | :---: | :---: | :---: |
| Gamificação adaptativa do letramento corporativo para surdos | ✅ | ❌ | ❌ | ❌ |
| Painel corporativo de progresso e inclusão | ✅ | ❌ | ❌ | ❌ |
| Trilhas de qualificação profissional | ✅ | ❌ | ✅ | ❌ |
| Apoio bilíngue em Libras e línguas estrangeiras | ✅ | ✅ | ❌ | ✅ |
| Ensino de Libras para funcionários ouvintes | ✅ | ❌ | ✅ | ✅ |

## UX Research e Descoberta

O desenvolvimento do Sinalis foi fundamentado em pesquisas de experiência do usuário e mapeamento de dores reais documentadas pelo Squad 02:

* **Personas mapeadas:**
  * **Julia Ferreira (21 anos, Pessoa Surda):** Auxiliar de estoque que busca qualificação acessível em Libras, aprendizado de novos idiomas e crescimento profissional para alcançar independência financeira.
  * **Saulo Pereira (34 anos, Professor de Inglês):** Atua em escola bilíngue e necessita de materiais visuais que conectem Libras, Português e Inglês sem dependência de áudio, além de relatórios pedagógicos para acompanhar suas turmas.
  * **Juliana / Eduarda Albuquerque (34 anos, CEO):** Lidera uma empresa com mais de 100 funcionários e busca cumprir a Lei de Cotas (Lei 8.213/91) de maneira genuína, capacitando gestores e integrando profissionais surdos sem depender de processos improvisados.
* **Artefatos de Design:** O projeto conta com **Matriz CSD** (Certezas, Suposições e Dúvidas), **Mapas de Empatia** e **Jornadas do Usuário** detalhadas (desde o cadastro e teste de nivelamento até a realização de atividades e acompanhamento de progresso).

## Modelo de Negócios (B2B2C / B2G)

* **B2B (Empresas):** Assinatura corporativa para capacitação de equipes, painel de métricas de inclusão e adequação à legislação.
* **B2G (Governo e Instituições):** Licenças institucionais para apoiar a aprendizagem de alunos surdos na rede de ensino e a formação continuada de professores.
* **B2C (Individual):** Planos e recursos adicionais para usuários que desejam desenvolver leitura, escrita, Libras e outros idiomas no próprio ritmo.

## Estrutura do Repositório (Arquitetura CRUD)

Seguindo o padrão modular em Python com persistência em arquivos JSON, o repositório está organizado da seguinte forma:

```text
sinalis-crud/
├── database/
│   ├── db_usuario.json      # Dados de usuários (surdos, ouvintes, professores e gestores)
│   ├── db_trilha.json       # Cursos, módulos de idiomas, desafios e trilhas de qualificação
│   └── db_progresso.json    # Diagnósticos de nivelamento, pontuações, certificados e métricas
├── services/
│   ├── usuario.py           # CRUD de usuários (cadastro, login, listagem, atualização e exclusão)
│   ├── trilha.py            # CRUD de trilhas, aulas e módulos bilíngues
│   └── progresso.py         # Registro de nivelamento, cálculo de progresso e feedbacks
├── db.py                    # Funções de leitura e escrita nos arquivos JSON
├── main.py                  # Ponto de entrada da aplicação (menu interativo via terminal)
└── README.md                # Documentação do projeto
```

## Como Executar o Projeto

1. Clone este repositório no seu ambiente local:
   ```bash
   git clone [https://github.com/seu-usuario/sinalis-crud.git](https://github.com/seu-usuario/sinalis-crud.git)
   ```
2. Acesse a pasta raiz do projeto:
   ```bash
   cd sinalis-crud
   ```
3. Certifique-se de ter o **Python 3.10+** instalado e execute o arquivo principal:
   ```bash
   python main.py
   ```

## Nosso Squad (Squad 02)

Projeto desenvolvido por:

* Aline
* Gustavo Tavares
* Matheus Alexandre
* Nayara
* Thyago
