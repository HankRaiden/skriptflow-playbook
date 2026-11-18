# Papéis · Uma conversa, muitas perspectivas

Um CTO ouve algo diferente numa conversa do que uma diretora de marketing ou alguém do atendimento ao cliente. Você pode aproveitar isso: dê um papel à IA, e ela lê a mesma transcrição por outra lente.

**Como usar os modelos:** bloco de contexto + prompt do papel + transcrição limpa. Um papel por rodada. Depois compare os resultados – as diferenças costumam ser os insights mais valiosos.

## A forma básica

Todos os papéis seguem a mesma forma. Com ela você mesmo pode criar qualquer outro papel (compras, RH, finanças, qualidade …).

```text
{{CONTEXTO}}

Atue como {{PAPEL}} com muitos anos de experiência em {{SETOR}}.
Leia a transcrição exclusivamente da sua perspectiva e responda:
1. Do seu ponto de vista, qual é o verdadeiro tema desta conversa?
2. Quais três afirmações são mais importantes para a sua área? (citação literal + por quê)
3. Que riscos ou oportunidades você vê que outros deixariam passar?
4. Que perguntas você faria na próxima conversa?
5. O que deveria acontecer primeiro, do seu ponto de vista?
Permaneça no seu papel. Nada de conselhos gerais fora da sua área.

Transcrição:
{{TRANSCRICAO_LIMPA}}
```

## Papéis prontos

### Diretoria

```text
{{CONTEXTO}}

Atue como diretor de uma empresa de médio porte. Leia a transcrição com foco em: limites de crescimento,
dependência de pessoas específicas, decisões pendentes e o que o tema significa para o resultado e o futuro
da empresa. Responda às cinco perguntas da forma básica (tema, três afirmações mais importantes com citação,
riscos/oportunidades ignorados, próximas perguntas, primeiro passo).

Transcrição:
{{TRANSCRICAO_LIMPA}}
```

### CTO / TI

```text
{{CONTEXTO}}

Atue como CTO. Leia a transcrição com foco em: sistemas em uso, rupturas de mídia (papel, e-mail, Excel,
Word), dados duplicados, interfaces, proteção de dados e segurança da informação, manutenção.
Responda às cinco perguntas da forma básica e, além disso, descreva o cenário atual de sistemas como lista.

Transcrição:
{{TRANSCRICAO_LIMPA}}
```

### Marketing (CMO)

```text
{{CONTEXTO}}

Atue como diretor de marketing. Leia a transcrição com foco em: como os clientes encontram a empresa? Que
linguagem a outra pessoa usa para a sua oferta e os seus clientes? Que mensagens, posicionamento e canais
aparecem? Responda às cinco perguntas da forma básica e, além disso, reúna formulações literais que sirvam para textos.

Transcrição:
{{TRANSCRICAO_LIMPA}}
```

### Vendas

```text
{{CONTEXTO}}

Atue como gerente de vendas B2B. Leia a transcrição com foco em: sinais de compra, necessidade, urgência,
decisores e influenciadores, sinais de orçamento (sem valores), objeções, próximo passo. Responda às cinco
perguntas da forma básica e termine com uma avaliação: quão quente é esta oportunidade (fria/morna/quente) e por quê?

Transcrição:
{{TRANSCRICAO_LIMPA}}
```

### Atendimento ao cliente

```text
{{CONTEXTO}}

Atue como gerente de atendimento ao cliente. Leia a transcrição com foco em: perguntas e problemas
recorrentes dos clientes, tempos de espera, passagens entre pessoas em que a informação se perde e o que
frustra os clientes. Responda às cinco perguntas da forma básica.

Transcrição:
{{TRANSCRICAO_LIMPA}}
```

### Treinamento / transferência de conhecimento

Para treinamentos internos (por exemplo, um treinamento de CRM): a transcrição vira uma imagem de aprendizado para os colegas.

```text
{{CONTEXTO}}

Atue como instrutor de educação de adultos. A transcrição vem de um treinamento.
1. Resuma os princípios mais importantes em no máximo 7 frases – de forma que um colega novo entenda.
2. Crie o fluxo de trabalho mostrado como diagrama Mermaid (flowchart TD), passo a passo, marcando onde os usuários costumam errar (⚠).
3. Formule 5 perguntas de compreensão com resposta.
4. Liste perguntas do treinamento que ficaram sem resposta.

Transcrição:
{{TRANSCRICAO_LIMPA}}
```

### Consultor de IA

O papel mais forte para primeiras reuniões – veja também o [passo 6](02-phase-2-solution.md).

```text
{{CONTEXTO}}

Atue como {{por exemplo "consultor de IA com expertise em automação com IA"}}. Me dê três propostas, três
ideias, de como podemos atender ao pedido da outra pessoa. Por proposta: ideia central, primeiro passo,
maior risco. Diferencie claramente entre rápida/enxuta, equilibrada e abrangente.

Transcrição:
{{TRANSCRICAO_LIMPA}}
```

### Challenger

Para todo resultado que você quer mostrar a alguém – veja o [passo 7](02-phase-2-solution.md).

```text
Você é um challenger crítico. Encontre as três maiores fraquezas do resultado abaixo antes que a outra
pessoa encontre: afirmações sem fundamento, contradições com a transcrição, riscos ignorados.
Sugira uma melhoria concreta para cada fraqueza. Seja rigoroso, mas justo.

Resultado:
{{RESULTADO}}

Transcrição para conferência:
{{TRANSCRICAO_LIMPA}}
```

## Juntando as perspectivas

```text
Aqui estão avaliações da mesma conversa a partir de vários papéis. Crie uma tabela:
Tema | Diretoria | TI | Marketing | Vendas | Atendimento – e marque onde os papéis se contradizem.
A partir disso, derive os três temas que precisam ser esclarecidos na próxima conversa.

{{RESULTADOS_PAPEIS}}
```
