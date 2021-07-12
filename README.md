# jogo-da-velha

Script simples de Jogo da Velha para dois jogadores feito em Python


  No início do código fiz o import de duas classes:

UUID - Universal Unique Identifier, classe que no futuro nos ajudará a gerar um código para cada partida do Jogo da Velha

RANDINT - classe da biblioteca "RANDOM", que futuramente nos ajudará a escolher aleatoriamente um número inteiro para determinar o jogador que iniciará a partida


  Em seguida, gerei um dicionário para criar o tabuleiro em que o Jogo da Velha acontecerá. É importante ressaltar que os dicionários em Python funcionam no esquema "chave: valor", portanto geramos nove chaves numeradas de 1-9 assumindo valores em branco, e cada lacuna do dicionário funcionará como um campo do Jogo da Velha.
Entao criei a funcao printBoard, a fim de printar o tabuleiro do Jogo da Velha atualizado toda vez que fosse necessário no decorrer do código.
  
  Enfim, criei as variáveis "turn", que representa qual jogador deverá fazer uma jogada no respectivo turno e "count" (que contará o número de jogadas que foram feitas). Junto da variável turn, utilizei a classe randint, que sorteará um dos jogadores (X ou O) para comecar jogando a partida. Em seguida, utilizando a classe UUID e a funcao UUID4 (que gera um hash aleatório) atribui a variável "id" o valor do hash que será gerado ao início de cada partida.
  
  A variável "move" é responsável por receber o input das jogadas que serao feitas, e com o uso de um simples IF torna-se possível checar se a jogada é válida ou nao! Além disso, a cada jogada válida feita por um jogador o contador recebe mais um valor.
  
  Nas linhas 53 e 96 novamente utilizamos o contador, dessa vez para determinar as condicoes de vitória ou empate. É importante ressaltar que os valores atribuídos no IF do contador nao sao escolhidos de maneira arbitrária, já que uma partida de Jogo da Velha só pode ser ganha com NO MÍNIMO 5 jogadas NO TOTAL, e se uma partida atinge o número de 9 jogadas NO TOTAL e ninguém cumpre as condicoes de vitória, temos um empate.
  
  A grande seguencia de IFs deve-se ao fato de que a partir da quinta jogada, todas as condicoes de vitória possíveis devem ser checadas pelo programa, sejam as linhas verticais, horizontais ou diagonais.
  
  Ao final do código, vemos o booleano responsável por alterar o jogador a cada rodada. Independente de qual jogador tenha sido escolhido aleatóriamente para comecar o jogo, os jogadores devem alternar de vez a cada rodada.
