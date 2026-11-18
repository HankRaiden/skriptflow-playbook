# Fase 3 · Conceito

**Objetivo da fase:** a solução escolhida vira um conceito que dá para mostrar, discutir e implementar.

Antes: [Fase 2 · Solução](02-phase-2-solution.md). Comece a fase 3 somente depois que um humano decidiu no passo 8.

---

## Passo 9 · IA: documento estratégico e conceito

**Quem:** IA · **Resultado:** documento estratégico (2–4 páginas)

```text
{{CONTEXTO}}

Com base na solução escolhida, escreva um documento estratégico para a outra pessoa.

Estrutura:
1. Situação – nas palavras dela (citações curtas da transcrição).
2. Objetivo – o que muda depois da implementação, descrito como dia a dia, não como tecnologia.
3. Solução – a variante escolhida, em palavras simples.
4. Argumentação de benefícios – por bloco: característica → vantagem → benefício para exatamente esta pessoa.
5. Implementação em fases – com um primeiro ganho rápido após poucas semanas.
6. O que precisamos de você – decisões, acessos, contatos.
7. Riscos e como lidamos com eles.
8. Próximos passos.

Regras:
- Tratamento formal ou informal conforme o contexto.
- NADA de números, depoimentos, estudos ou garantias inventados. Onde faltar um número, escreva "[a esclarecer]".
- Sem jargão sem explicação.

Solução escolhida e decisão:
{{DECISAO}}

Análise da situação atual:
{{SITUACAO_ATUAL}}
```

**Revisar:** procure especificamente por evidências inventadas. Textos de IA tendem a "Nossos clientes relatam 25% mais …". Se você não consegue provar uma frase assim, apague-a. Confiança é a única coisa que você realmente vende numa primeira reunião.

Mais: [Argumentação de benefícios](benefit-argument.md)

---

## Passo 10 · IA: fluxograma da implementação

**Quem:** IA · **Resultado:** diagrama da implementação (fases, pacotes, dependências)

```text
{{CONTEXTO}}

A partir do documento estratégico, crie um fluxograma da IMPLEMENTAÇÃO como código Mermaid (flowchart LR).
- Uma coluna (subgraph) por fase.
- Em cada fase, os pacotes ou etapas de trabalho como caixas.
- Setas para dependências ("B precisa de A").
- Marque com ◆ os pontos em que o cliente precisa decidir ou entregar algo.
- No máximo 14 caixas.
Depois, gere uma lista de marcos nos quais verificamos juntos se está funcionando.

Documento estratégico:
{{DOCUMENTO_ESTRATEGICO}}
```

---

## Passo 11 · IA: conteúdo da apresentação

**Quem:** IA · **Resultado:** conteúdo slide a slide

```text
{{CONTEXTO}}

Crie o conteúdo de uma apresentação de no máximo 12 slides para a reunião de retorno.
Para cada slide: título (máx. 8 palavras), mensagem principal (uma frase), 3 tópicos, sugestão de imagem ou diagrama.

Slides obrigatórios:
- "Isto foi o que eu entendi" – com o diagrama atual confirmado.
- "Assim poderia ficar" – com o diagrama-alvo.
- "O que isso te traz" – argumentação de benefícios.
- "Como começamos" – primeiro passo, prazo, o que precisamos de você.

Regras: fale a língua da outra pessoa. Nada de números inventados. Nenhum slide sem mensagem clara.

Documento estratégico:
{{DOCUMENTO_ESTRATEGICO}}
Diagrama da implementação:
{{DIAGRAMA_IMPLEMENTACAO}}
```

---

## Passo 12 · Humano: montar e discutir a apresentação

**Quem:** humano · **Resultado:** apresentação pronta e uma conversa de igual para igual

A IA forneceu o conteúdo. A apresentação você monta sozinho – na sua linguagem, com a sua sensibilidade para quem está do outro lado. Este último prompt prepara você para a conversa:

```text
{{CONTEXTO}}

Amanhã apresento o conceito. Me prepare:
1. As cinco objeções mais prováveis da outra pessoa – e uma resposta honesta e curta para cada uma.
2. Três perguntas para abrir a conversa, em vez de começar pelos slides.
3. Como vou perceber que algo não se encaixa – e como reajo então.

Material:
{{DOCUMENTO_ESTRATEGICO}}
{{SITUACAO_ATUAL}}
```

**Revisar:** o objetivo não é "vender", e sim uma imagem em comum. Se a outra pessoa reconhece a própria empresa no diagrama atual, o passo mais importante já foi dado.

De volta à visão geral: [Checklist](checklist.md)
