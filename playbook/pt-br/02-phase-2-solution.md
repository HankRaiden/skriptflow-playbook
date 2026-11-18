# Fase 2 · Solução

**Objetivo da fase:** uma imagem confirmada da situação atual vira vários caminhos de solução – testados por um oponente crítico e escolhidos por um humano.

Antes: [Fase 1 · Situação atual](01-phase-1-current-state.md). Comece a fase 2 somente depois que a outra pessoa confirmar o diagrama atual.

---

## Passo 5 · IA: 30 ideias de automação e melhoria

**Quem:** IA · **Resultado:** lista de ideias com avaliação aproximada

Por que 30? Porque as dez primeiras ideias são as óbvias. As interessantes vêm depois.

```text
{{CONTEXTO}}

Você é consultor de automação de processos e IA para pequenas e médias empresas.
Com base na análise da situação atual e no diagrama confirmado, desenvolva 30 ideias concretas para
melhorar ou automatizar o processo.

Gere uma tabela com as colunas:
Nº | Ideia (uma frase) | Resolve o ponto de dor | Esforço (pequeno/médio/grande) | Impacto (pequeno/médio/grande) | Risco / pré-requisito

Regras:
- Misture: ganhos rápidos sem software novo, automações com ferramentas existentes, uso de IA, mudanças organizacionais.
- Cada ideia precisa tratar de um ponto de dor da análise.
- Sem propaganda de fornecedores; cite ferramentas apenas como exemplo.
- No final, marque as 5 ideias com a melhor relação entre impacto e esforço.

Análise da situação atual:
{{SITUACAO_ATUAL}}

Diagrama confirmado:
{{DIAGRAMA_ATUAL}}
```

**Revisar:** risque o que obviamente não serve para esta empresa. Você conhece a cultura, o orçamento e as pessoas – a IA não.

---

## Passo 6 · IA: a solução como fluxograma – a IA como consultora

**Quem:** IA num papel de especialista · **Resultado:** três propostas de solução, cada uma como diagrama-alvo

Aqui você dá à IA um papel que combina com o pedido. Se a outra pessoa procura alguém para automação com IA, por exemplo, o papel é "consultor de IA com expertise em automação com IA". Se for um processo de vendas, é "consultor de vendas B2B para empresas de médio porte".

```text
{{CONTEXTO}}

Atue como {{PAPEL, por exemplo "consultor de IA com expertise em automação com IA"}} com 15 anos de experiência prática.

Me dê TRÊS propostas diferentes de como podemos atender aos requisitos da outra pessoa. As três devem
ser realmente diferentes, por exemplo:
- A: rápida e enxuta (com ferramentas existentes, viável em semanas),
- B: equilibrada (alguns blocos novos, impacto claramente maior),
- C: abrangente (reestruturação maior, maior alavanca).

Para cada proposta:
1. Ideia central em duas frases.
2. Quais ideias da lista de 30 ela reúne (números).
3. Processo-alvo como código Mermaid (flowchart TD), mesma notação do diagrama atual; marque passos novos ou automatizados com ✦.
4. O que a outra pessoa precisa fazer ou decidir para isso.
5. Maior risco.

Requisitos e análise da situação atual:
{{SITUACAO_ATUAL}}

30 ideias:
{{IDEIAS}}
```

**Revisar:** coloque o diagrama atual e o diagrama-alvo lado a lado. A diferença cabe numa frase? Se não, a proposta é complicada demais.

---

## Passo 7 · IA: challenger – avaliar e otimizar

**Quem:** IA como oponente · **Resultado:** propostas avaliadas e melhoradas

Todo rascunho ganha um oponente. De preferência num **chat novo**, para que a IA não defenda as próprias propostas.

```text
{{CONTEXTO}}

Você é um challenger crítico. Sua tarefa NÃO é gostar das propostas, e sim encontrar as fraquezas delas
antes que o cliente encontre.

Para cada uma das três propostas:
1. Inversão: como este projeto teria fracassado daqui a seis meses? Cite os três motivos mais prováveis.
2. Qual suposição tem menos fundamento?
3. O que o consultor deixou passar (proteção de dados, aceitação da equipe, manutenção, dependência de fornecedor, custos após o início)?
4. Nota de 1 a 10 para: benefício ao cliente, viabilidade, risco (10 = menor risco).
5. Uma melhoria concreta que corrige a maior fraqueza.

Por fim: qual proposta – depois de melhorada – você mostraria primeiro ao cliente, e por quê?

Propostas:
{{PROPOSTAS}}

Análise da situação atual para conferência:
{{SITUACAO_ATUAL}}
```

**Revisar:** adote melhorias de forma consciente, não automática. Um challenger que acha tudo ruim ajuda tão pouco quanto um que acha tudo bom.

---

## Passo 8 · Humano: decidir o que seguir

**Quem:** humano – você e/ou quem decide do outro lado · **Resultado:** solução ou pacotes escolhidos

Aqui nenhuma IA decide. A IA forneceu material; agora escolhe um humano que arca com as consequências. Este prompt só ajuda a preparar a decisão:

```text
{{CONTEXTO}}

Prepare um documento de decisão em UMA página:
- Tabela das três propostas (melhoradas): benefício, viabilidade, risco, o que o cliente precisa contribuir.
- Uma frase por proposta: "Escolha esta se …".
- Três perguntas que quem decide deveria responder antes de escolher.
NÃO tome a decisão você mesmo.

Material:
{{PROPOSTAS}}
{{RESULTADO_CHALLENGER}}
```

**Revisar:** registre a decisão por escrito – com data e o motivo em uma frase. Esse é o ponto de partida da fase 3.

Próximo: [Fase 3 · Conceito](03-phase-3-concept.md)
