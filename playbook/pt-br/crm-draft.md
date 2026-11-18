# Rascunho para o CRM · Da conversa ao fluxo de trabalho

Uma transcrição só se torna produtiva quando gera trabalho: uma tarefa, um lead, uma oportunidade. Este prompt gera um **rascunho** que um humano revisa e depois transfere para o CRM – à mão, por importação (CSV) ou por uma automação.

> **Princípio: rascunho, não piloto automático.** A IA não cria nada sozinha. Ela prepara, você aprova. Só quando o rascunho for confiável por semanas vale a pena automatizar a transferência – e mesmo assim com um ponto de aprovação.

## O prompt

```text
{{CONTEXTO}}

Você é um assistente de CRM. Leia a transcrição e crie um RASCUNHO para o CRM.

1. Tarefas
   Tabela: título | descrição (1 frase) | responsável (papel) | prazo (data ou "[a esclarecer]") | evidência (citação)
   Somente tarefas que foram prometidas ou claramente combinadas na conversa.

2. Lead / contato
   Campos: empresa (marcador) | papel do contato | setor | porte | origem | necessidade em uma frase.

3. Oportunidade
   Campos: nome | fase (por exemplo qualificação / análise de necessidade / proposta) | necessidade | decisor |
   próxima atividade | avaliação fria/morna/quente com motivo. NÃO invente valores nem probabilidade de fechamento em percentual.

4. Nota da conversa
   5–8 frases para o histórico de atividades do contato.

5. CSV
   Gere também as tarefas como CSV com linha de cabeçalho: Subject,Description,Owner,DueDate

Regras:
- Não invente nada. O que não apareceu na conversa é "[a esclarecer]".
- Mantenha os marcadores da anonimização; eu só os substituo dentro do CRM.

Transcrição:
{{TRANSCRICAO_LIMPA}}
```

## Revisar antes de transferir

- Cada tarefa foi realmente prometida – ou a IA transformou uma boa ideia em tarefa?
- Responsáveis e prazos estão corretos?
- Substitua os marcadores pelos registros reais – dentro do CRM, não no chat da IA.

## O caminho para a automação (avançado)

Quando o rascunho for confiável, uma automação (por exemplo com n8n, Make, Zapier ou os recursos do seu CRM) pode ligar os passos: a transcrição chega → a IA cria o rascunho no formato acima → **um humano aprova** → tarefas, lead e oportunidade são criados. O ponto de aprovação não é desconfiança da tecnologia, e sim garantia de qualidade: um registro errado no CRM custa mais tempo depois do que dez segundos de revisão agora.
