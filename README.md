# Jogo de Adivinhação em Python 🎯

Jogo de terminal para dois participantes adivinharem um número secreto entre 0 e 50. O projeto foi criado para praticar os fundamentos de lógica de programação em Python.

## Como funciona

1. Os dois jogadores informam seus nomes.
2. O programa sorteia quem começa.
3. Um número secreto entre 0 e 50 é gerado.
4. Os jogadores alternam seus palpites e recebem dicas de “maior” ou “menor”.
5. A partida termina quando alguém acerta o número.

## Conceitos praticados

- entrada e saída de dados;
- variáveis e f-strings;
- condicionais;
- laços de repetição;
- números aleatórios com o módulo `random`.

## Nível atual do projeto

Este é um dos meus projetos iniciais e está mantido no perfil para registrar a
evolução da minha base em Python. O código ainda tem pontos simples a melhorar,
especialmente validação de entrada, alternância correta de turnos, limite de
tentativas e separação em funções.

## Executar

Pré-requisito: Python 3 instalado.

```bash
git clone https://github.com/r-otavio-dev/Jogo-de-Adivinha-o-python.git
cd Jogo-de-Adivinha-o-python
python sorteioeadivinhacao.py
```

## Possíveis melhorias

- validar entradas que não sejam números;
- limitar a faixa dos palpites;
- contar tentativas e partidas vencidas;
- adicionar testes automatizados;
- permitir partidas contra o computador.
