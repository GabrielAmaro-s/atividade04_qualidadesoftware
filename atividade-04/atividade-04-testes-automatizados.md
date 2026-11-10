# Atividade 4: Testes Automatizados do LocalEats

**Unidade curricular:** Qualidade de Software  
**Projeto:** LocalEats  
**Modalidade:** Individual  
**Responsável:** Gabriel Amaro  
**Sistema testado:** https://local-eats-unisenac.vercel.app/

## 1. Objetivo

Criar testes automatizados para validar uma regra de negócio de pedidos e uma funcionalidade da interface do LocalEats. Foram usados Python, pytest e Playwright.

## 2. Parte 1: Testes unitários

**Regra escolhida:** verificar o valor mínimo de um pedido.

A função `pedido_atingiu_valor_minimo(valor_pedido)` fica em `src/regras_localeats.py` e segue estas condições:

- Pedidos de R$ 30,00 ou mais retornam `True`.
- Pedidos abaixo de R$ 30,00 retornam `False`.
- Valores negativos geram `ValueError`.

Foram criados três testes independentes:

1. `test_pedido_de_trinta_reais_atinge_o_minimo`: verifica o valor exato de R$ 30,00.
2. `test_pedido_abaixo_do_minimo_e_rejeitado`: verifica o valor de R$ 29,99.
3. `test_pedido_negativo_gera_erro`: verifica a exceção para o valor de R$ -1,00.

Os três testes utilizam assertions do pytest, incluindo `pytest.raises` para a exceção.

## 3. Registro simplificado do TDD de Gabriel Amaro

**Regra escolhida:** valor mínimo do pedido.

**Primeiro teste escrito:** `test_pedido_de_trinta_reais_atinge_o_minimo`, com um pedido de R$ 30,00.

**Por que o teste falhou inicialmente:** na primeira execução, o arquivo `src/regras_localeats.py` ainda não existia. O pytest apresentou `ModuleNotFoundError` durante a coleta dos testes. O registro está em `evidencias/primeira-execucao-tdd.txt`.

**Implementação mínima realizada:** criei a função `pedido_atingiu_valor_minimo` e implementei a comparação com o mínimo de R$ 30,00.

**Segundo teste escrito:** `test_pedido_abaixo_do_minimo_e_rejeitado`, com R$ 29,99, para garantir que um pedido abaixo do mínimo seja rejeitado.

**Melhoria realizada:** adicionei a validação de valores negativos e o terceiro teste, `test_pedido_negativo_gera_erro`. Assim, a função passou a tratar também uma entrada inválida.

**Resultado:** os três testes unitários passaram. A saída está em `evidencias/testes_unitarios-aprovados.txt`.

## 4. Parte 2: Teste funcional com Playwright

**Fluxo escolhido:** abrir o formulário de cadastro do LocalEats pela página inicial.

O teste `test_abrir_formulario_de_cadastro`, em `tests/test_localeats.py`, realiza o seguinte fluxo:

1. Acessa a página inicial do LocalEats pelo navegador Chromium.
2. Clica no botão de criação de conta, localizado pelo seletor `#showRegisterBtn`.
3. Verifica que o formulário `#registerForm` ficou visível.
4. Verifica que o campo de nome `#regName` está visível.
5. Verifica que o botão **Registrar** está visível.

São **três assertions**, todas usando `expect`, para verificar elementos observáveis na interface. O teste não utiliza `time.sleep`.

Os seletores foram escolhidos com base em referências públicas de testes da interface do LocalEats. Como o site não pôde ser aberto neste ambiente, ainda é necessário confirmar a execução integral no computador do integrante.

## 5. Identificação das responsabilidades

| ID | Integrante | Tipo | Comportamento verificado | Arquivo e função |
| --- | --- | --- | --- | --- |
| TU01 | Gabriel Amaro | Unitário | Pedido de R$ 30,00 atende ao mínimo | `tests/test_regras_localeats.py::test_pedido_de_trinta_reais_atinge_o_minimo` |
| TU02 | Gabriel Amaro | Unitário | Pedido de R$ 29,99 fica abaixo do mínimo | `tests/test_regras_localeats.py::test_pedido_abaixo_do_minimo_e_rejeitado` |
| TU03 | Gabriel Amaro | Unitário | Valor negativo gera `ValueError` | `tests/test_regras_localeats.py::test_pedido_negativo_gera_erro` |
| TF01 | Gabriel Amaro | Funcional | Abertura do formulário de cadastro | `tests/test_localeats.py::test_abrir_formulario_de_cadastro` |

## 6. Explicação individual de um teste

Escolhi explicar o teste `test_pedido_negativo_gera_erro`. Ele verifica o que acontece quando alguém informa um valor negativo para um pedido. Como esse valor não faz sentido para a regra, a função deve lançar um `ValueError` em vez de devolver `True` ou `False`. Usei `pytest.raises` para confirmar esse comportamento. Esse caso é importante porque impede que dados inválidos sejam aceitos sem tratamento.

## 7. Execução e resultados

Foi executado `python -m pytest -v`, com os seguintes resultados neste ambiente:

| Teste | Resultado |
| --- | --- |
| TU01 | Aprovado |
| TU02 | Aprovado |
| TU03 | Aprovado |
| TF01 | Não concluído: acesso externo bloqueado (`ERR_BLOCKED_BY_ADMINISTRATOR`) |

**Resumo real da execução:** 3 testes aprovados e 1 reprovado por bloqueio do navegador ao tentar abrir a URL. A falha aconteceu antes de qualquer interação com o site, portanto não permite concluir que existe defeito na aplicação ou no fluxo automatizado.

O relatório completo está no arquivo `relatorio-pytest.txt`. Antes da entrega, o teste funcional precisa ser executado em um computador que consiga acessar o LocalEats e o relatório deve ser atualizado com a execução real.

## 8. Como executar no PowerShell

Abra um terminal na pasta `atividades/atividade-04` e execute:

```powershell
python -m pip install -r requirements.txt
python -m playwright install chromium
python -m pytest -v | Tee-Object -FilePath relatorio-pytest.txt
```

Se o teste funcional falhar em um computador com internet, confira se a interface ainda apresenta os mesmos elementos e ajuste os locators conforme necessário. Depois, rode novamente o pytest e atualize o relatório.

## 9. Uso de inteligência artificial

**Ferramenta utilizada:** ChatGPT (GPT-6).

**Como a ferramenta foi utilizada:** apoio na organização dos arquivos, implementação da regra em Python, criação dos testes e elaboração deste registro.

**Uma sugestão que precisou ser alterada ou rejeitada:** foi descartado o uso de espera fixa na automação da interface. O teste utiliza as esperas automáticas dos locators e das assertions do Playwright.

**Como o código sugerido foi verificado:** foram executados os testes unitários, confirmando as três aprovações. Também foi feita uma tentativa de executar o teste funcional com Chromium. A navegação foi impedida pelo bloqueio de acesso externo deste ambiente, então a validação funcional permanece pendente no computador do integrante.

## 10. Estrutura dos arquivos

```text
atividade-04/
├── atividade-04-testes-automatizados.md
├── relatorio-pytest.txt
├── requirements.txt
├── pytest.ini
├── src/
│   ├── __init__.py
│   └── regras_localeats.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_regras_localeats.py
│   └── test_localeats.py
└── evidencias/
    ├── primeira-execucao-tdd.txt
    └── testes_unitarios-aprovados.txt
```
