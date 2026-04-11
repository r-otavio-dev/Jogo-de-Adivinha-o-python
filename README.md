📝 Sobre o Projeto
Desenvolvi este script em Python para criar uma experiência interativa de jogo entre dois usuários. O objetivo principal foi aplicar conceitos de lógica de programação, manipulação de entradas e o uso da biblioteca random para criar um sistema de competição simples, mas funcional.

🧠 Lógica de Desenvolvimento
Ao escrever o código, segui os seguintes passos:

Interatividade Inicial: Comecei capturando o nome dos jogadores para tornar a experiência personalizada através de f-strings.

Geração de Dados Aleatórios: Utilizei a função random.randint(0, 50) para garantir que o número secreto fosse imprevisível a cada nova execução. Também adicionei um sorteio estético para definir quem começa a partida.

Gerenciamento de Turnos: Implementei uma estrutura de repetição aninhada (for). O loop externo garante que o jogo não pare até que haja um vencedor, enquanto o loop interno alterna as tentativas entre o Jogador 1 e o Jogador 2.

Feedback Dinâmico: Para que o jogo não fosse baseado apenas em sorte, utilizei estruturas condicionais (if/elif/else) para fornecer dicas se o número secreto é maior ou menor que o palpite atual.

Finalização: O jogo utiliza a função exit() para encerrar o processo imediatamente assim que a condição de vitória (acerto) é satisfeita.

🛠️ Tecnologias Aplicadas
Linguagem: Python 3

Módulos: random (Geração de números e escolhas aleatórias)

Conceitos: Loops de repetição, condicionais compostas e tratamento de inputs.

Como rodar o meu código:
Tenha o Python instalado em sua máquina.

Clone este repositório.

Execute o arquivo via terminal:

Bash
python nome_do_seu_arquivo.py
