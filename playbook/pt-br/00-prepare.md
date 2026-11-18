# 00 · Preparação: consentimento, anonimização, contexto

Antes que uma única palavra vá para uma IA, vêm três coisas. Juntas levam dez minutos e protegem você, a pessoa com quem você conversou e o resultado.

## 1. Consentimento antes da gravação

Na Alemanha, gravar secretamente palavras ditas em ambiente não público é crime (§ 201 StGB). No Brasil e em muitos outros países também há regras, e o conteúdo de uma conversa quase sempre é dado pessoal (LGPD, GDPR e leis semelhantes). Por isso:

- **Pergunte antes, não depois.** De preferência já no convite da reunião e, de novo, em voz alta no início da conversa.
- **Diga a finalidade.** "Gostaria de gravar para não perder nada e depois te enviar um resumo e um diagrama do processo."
- **Não é não.** Então você faz anotações e as usa como "transcrição". O método funciona mesmo assim, só que de forma mais grosseira.
- **Verifique a ferramenta.** Onde a ferramenta de gravação armazena os dados? Existe um contrato de tratamento de dados? Essa é uma pergunta para o seu encarregado de proteção de dados, não para este playbook.

Modelo para o convite:

```text
Uma observação rápida sobre a nossa reunião: gostaria de gravar e transcrever a nossa conversa para
poder me concentrar totalmente em você sem perder nada. Depois você recebe de mim um resumo e uma imagem
do seu processo atual para confirmar. Vou usar a gravação apenas para isso e apagá-la quando terminarmos.
Se preferir que eu não grave, é só avisar – aí eu anoto do jeito clássico.
```

> Não é aconselhamento jurídico. Verifique você mesmo as regras do seu país, da sua empresa e da sua ferramenta.

## 2. Anonimizar antes que a IA veja

Substitua nomes, empresas, lugares, telefones, e-mails, preços e tudo o que identifique uma pessoa por papéis e marcadores. A IA não precisa de nomes reais para a análise. Você pode guardar a correspondência só para si.

```text
Você é um assistente cuidadoso de proteção de dados.

Tarefa: anonimize a transcrição abaixo antes que ela seja processada.
- Substitua nomes de pessoas por papéis entre colchetes, por exemplo [Diretor], [Gerente de vendas], [Eu].
- Substitua nomes de empresas por [Empresa A], [Cliente B], [Fornecedor C] etc. O mesmo nome recebe sempre o mesmo marcador.
- Substitua lugares, telefones, e-mails, sites, números de cliente e de pedido por [Local], [Telefone], [E-mail] etc.
- Substitua valores concretos de dinheiro por [Valor].
- NÃO altere mais nada: sem encurtar, sem reformular, sem corrigir.
- No final, gere uma tabela "original → marcador" que eu guardo localmente e NÃO compartilho.

Transcrição:
{{TRANSCRICAO}}
```

> Importante: se você entregar até mesmo este passo a uma IA na nuvem, ela já viu os dados originais. Para conversas sensíveis, anonimize à mão (localizar e substituir) ou com um modelo rodando localmente.

## 3. O bloco de contexto

Todo prompt deste playbook começa com o mesmo bloco de contexto. Preencha-o uma vez e copie-o sempre junto. Assim a IA sabe em cada passo do que se trata.

```text
CONTEXTO
- Quem sou eu: {{seu papel, por exemplo "consultor de automação de processos", "gerente de vendas", "administrador Salesforce"}}
- Com quem foi a conversa: {{papel da outra pessoa, setor, porte – sem nomes}}
- Tipo de conversa: {{primeira reunião / reunião estratégica / treinamento / reunião interna}}
- Objetivo da outra pessoa: {{em uma frase, do jeito que ela disse}}
- Meu objetivo: {{por exemplo "entender o problema e propor três caminhos de solução"}}
- Idioma e tom dos resultados: {{por exemplo português, informal, palavras simples, sem jargão sem explicação}}
```

## Forma de trabalhar

- **Uma conversa = um chat** (ou um projeto na sua IA). Assim os resultados anteriores ficam no contexto e você não precisa colá-los toda vez.
- **Revise cada passo** antes de iniciar o próximo. A IA continua construindo sobre os próprios erros se você não a interromper.
- **Salve os resultados** – um arquivo Markdown por passo. No fim você tem um registro rastreável.

Próximo: [Fase 1 · Situação atual](01-phase-1-current-state.md)
