 #### Descrição do código do Jogo

 **1. Implemente a classe Carta. Esta deve ter os atributos naipe e valor.**
Naipes: Paus, Ouros, Copas, Espadas. 
Valores: Ás, 2, 3, 4, 5, 6, 7, 8, 9, 10, Valete, Rainha, Rei. 
##
 **2. Implemente o método __str__ na classe Carta para converter uma Carta numa string com o formato "Valor de Naipe" (ex.: "Valete de Ouros").** 
##
 **3. Implemente os métodos __lt__ e __gt__ na classe Carta para definir os operadores de comparação < e >. Considere a seguinte ordem:** 
Ás < 2 < 3 < ... < 10 < Valete < Rainha < Rei 
♧ < ♢ < ♡ < ♤ 
##
 **4. Implemente a classe Baralho. Esta deve ter o atributo cartas que corresponde a uma lista com todas as cartas disponíveis. Considere importar o módulo random e tenha em mente que no baralho, para além das cartas disponíveis, também podem haver cartas removidas.**
##
 **5. Implemente o método baralhar na classe Baralho que desordena as cartas do baralho.**
##
**6. Implemente o método ordenar na classe Baralho que ordena as cartas do baralho.**
##
**7. Implemente o método retirar na classe Baralho que remova uma carta do baralho.**
##
 **8. Implemente o método restaurar na classe Baralho que reponha todas as cartas retiradas do baralho.**
##
 **9. Implemente o método __str__ na classe Baralho que imprime a lista completa de cartas do baralho.**
##
 **10. Blackjack é um jogo de cartas em que o objetivo é ter mais pontos que o  adversário, mas sem ultrapassar os 21 pontos (caso em que se perde). Escreva uma função (não um método) chamada blackjack() que siga as seguintes regras:**

-  O dealer deve retirar duas cartas para ele próprio (exibindo apenas 
uma) e outras duas cartas para o Jogador. 
-  O jogador pode opcionalmente pedir mais cartas enquanto não igualar 
ou ultrapassar os 21 pontos (se ultrapassar 21 pontos, perde). 
-  O dealer, enquanto não tiver uma pontuação superior ao Jogador (e a 
pontuação for diferente de 21), deve retirar mais cartas. 
- Se o dealer ultrapassar os 21 pontos, perde; se ficar com mais pontos 
que o jogador, ganha; se ambos ficarem igualados com 21 pontos, é 
empate. 
As regras de pontuação são as seguintes: 
- Cartas de 2 a 10 valem o seu valor nominal. 
- Reis, rainhas e valetes valem 10. 
- Ases valem 11 se o total da mão não ultrapassar 21, caso contrário 
valem 1.
