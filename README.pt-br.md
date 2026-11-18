# SkriptFlow · Transcrições viram fluxos de trabalho

[Deutsch](README.md) · [English](README.en.md) · **Português (Brasil)**

> **Aviso legal:** Não assumo nenhuma responsabilidade por quaisquer resultados que possam ser obtidos em conexão com este playbook. Não é aconselhamento jurídico, de proteção de dados ou empresarial. Detalhes: [DISCLAIMER.md](DISCLAIMER.md).

Um playbook de prompts gratuito que transforma **uma única transcrição de conversa** em uma imagem em comum, três caminhos de solução e um conceito pronto, em doze passos – com qualquer IA, sem código.

Página do projeto: **https://skriptflow.vercel.app/pt-br/**

---

## Por quê

Gravações e resumos de reuniões são provavelmente o caso de uso de IA mais comum nos países de língua alemã. É um bom primeiro passo. Mas é como ter uma Ferrari e dirigir a 30 km/h.

Uma transcrição não é ata para o arquivo. É **matéria-prima**:

- **Perspectivas:** um CTO percebe uma conversa de forma diferente de uma diretora de marketing ou do atendimento. Você pode controlar isso dando um papel à IA.
- **Imagens:** uma primeira reunião vira um fluxograma do processo de hoje. Você e a outra pessoa passam a ter na hora a mesma imagem – e ela pode confirmá-la.
- **Soluções:** dê à IA o papel de consultora, por exemplo "consultor de IA com expertise em automação com IA", e peça três caminhos de solução diferentes para trabalhar junto com a outra pessoa.
- **Trabalho:** a conversa vira tarefas, leads e oportunidades no CRM – como rascunho que um humano aprova.

## O método: 3 fases, 12 passos

| Fase | Nº | Passo | Quem |
|---|---|---|---|
| **1 · Situação atual** | 1 | Criar a transcrição (com consentimento, anonimizada) | Humano |
| | 2 | Revisar ortografia e erros de audição | IA |
| | 3 | Análise da situação atual e requisitos | IA |
| | 4 | Visualizar o processo atual – e pedir confirmação | IA → humano |
| **2 · Solução** | 5 | 30 ideias de automação e melhoria | IA |
| | 6 | Três soluções como fluxograma (IA como consultora) | IA |
| | 7 | Challenger: avaliar e otimizar | IA |
| | 8 | Decidir o que seguir | **Humano** |
| **3 · Conceito** | 9 | Documento estratégico com argumentação de benefícios | IA |
| | 10 | Fluxograma da implementação | IA |
| | 11 | Conteúdo da apresentação | IA |
| | 12 | Montar e discutir a apresentação | **Humano** |

## Conteúdo

| Arquivo | Para quê |
|---|---|
| [00 · Preparação](playbook/pt-br/00-prepare.md) | consentimento, anonimização, bloco de contexto |
| [Fase 1 · Situação atual](playbook/pt-br/01-phase-1-current-state.md) | passos 1–4 |
| [Fase 2 · Solução](playbook/pt-br/02-phase-2-solution.md) | passos 5–8 |
| [Fase 3 · Conceito](playbook/pt-br/03-phase-3-concept.md) | passos 9–12 |
| [Papéis](playbook/pt-br/roles.md) | diretoria, CTO, marketing, vendas, atendimento, treinamento, consultor de IA, challenger |
| [Rascunho para o CRM](playbook/pt-br/crm-draft.md) | tarefas, lead, oportunidade, CSV – rascunho, não piloto automático |
| [Argumentação de benefícios](playbook/pt-br/benefit-argument.md) | característica → vantagem → benefício |
| [Checklist](playbook/pt-br/checklist.md) | todos os passos para marcar |
| [Exemplo](examples/fiktive-tischlerei/README.md) | conversa fictícia com resultados de exemplo (em alemão) |

## Início rápido em 10 minutos

1. Leia [00 · Preparação](playbook/pt-br/00-prepare.md) e obtenha o consentimento para a sua próxima conversa.
2. Preencha o bloco de contexto.
3. Abra um chat novo na sua IA (Claude, ChatGPT, Gemini, Copilot – tanto faz).
4. Faça os passos 2 a 4 e envie o diagrama atual para a outra pessoa com a pergunta: "Entendi corretamente?"

Já esta primeira rodada muda a conversa seguinte.

## Princípios-chave

1. **Uma transcrição é matéria-prima, não arquivo.**
2. **Perspectiva é um papel que você atribui.**
3. **Primeiro a imagem, depois a solução.** Um diagrama atual confirmado pela outra pessoa vale mais do que qualquer conceito.
4. **Três caminhos em vez de uma resposta.** Rápido, equilibrado, abrangente – e escolher juntos.
5. **Todo rascunho ganha um oponente.** O challenger encontra as fraquezas antes do cliente.
6. **A IA propõe, o humano decide.** Os passos 8 e 12 pertencem ao humano.
7. **Consentimento antes de gravar, anonimização antes da IA.**
8. **Nada de evidências inventadas.** Melhor "[a esclarecer]" do que um número inventado.

## Como surgiu

Testei este método numa conversa com um empresário amigo: gravei a primeira reunião e fiz análise da situação atual, diagrama atual, ideias, solução como diagrama, challenger, documento estratégico e apresentação – tudo a partir de uma única transcrição.

Como administrador Salesforce, também dou treinamentos regularmente. Transformamos a transcrição de um treinamento num fluxograma com os princípios mais importantes, para que os colegas tenham uma visão geral mais rápido.

Testado por mim: avaliação por papéis, visualização, IA como consultora com três propostas e integração com o CRM.

## Perspectiva: o podcast pessoal de destaques

Usuários avançados de IA marcam momentos importantes nas reuniões com um botão de destaque. No fim da semana, transformam todos os destaques num podcast pessoal, feito sob medida, e ouvem uma revisão da semana no fim de semana ou na segunda de manhã. A ideia vem de um podcast de Geoff Woods – eu ainda não a implementei. Ela mostra para onde isso pode ir.

## Limites – com honestidade

- **A IA erra de forma convincente.** Por isso há evidências (citações), confirmação pela outra pessoa, um challenger e dois passos humanos.
- **Proteção de dados é responsabilidade sua.** Grave apenas com consentimento. Verifique onde as suas ferramentas armazenam dados.
- **Um diagrama é uma hipótese** até a outra pessoa confirmá-lo.
- **Não substitui ouvir.** O playbook torna uma boa conversa mais produtiva; não transforma uma conversa ruim numa boa.

## Contribuir

Melhorias, novos papéis e traduções são bem-vindos – por issue ou pull request. Os testes (`python3 -m pytest -q`) verificam se todos os idiomas têm os mesmos passos e se nenhum nome real ou valor entra no repositório.

## Licença

MIT – veja [LICENSE](LICENSE). Uso livre, inclusive comercial.
