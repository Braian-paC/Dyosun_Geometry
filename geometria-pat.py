from math import *
from random import *
from time import *

escolha = 0
print('=-'*30)
print('Criado por Braian B. Gonçalves e Augusto Teixeira.')
print('Leia as instruções abaixo:\n1) Use sempre o ponto (.) ao invés da vírgula (,) na hora de colocar casas decimais, ex: 3.6 ; 209.63\n2) Os números sempre serão arredondados, então se você errar por 1 número que seja, o resultado será automáticamente\nconsiderado INCORRETO pelo programa. Ex: 69.8951 = 69.90 ; 69.8949 = 69.89\nCaso eu tenha esquecido de alguma instrução, ou você tenha achado algum bug, me avise e tentarei consertar. Também vale\nressaltar que o programa será desenvolvido com o tempo, afim de aprimorar meus conhecimentos.')
print('=-'*30)
name = str(input('Bem-vindo! Me chamo Dyosun, e você? '))
def escolha_2():
  A, B, E = randint(0, 30), randint(30, 90), randint(90, 270)
  q1 = float(input((f'As retas transversais (verticais) "u" e "v" interceptam as retas paralelas\n(horizontais) "r", "s" e "t".\nReta u: A, B, C.\nReta v: D, E, F.\nConsiderando A = {A} ; B = {B} ; E = {E} ; D = x ; E = {randint(0, 50)} ; F = {randint(10, 120)}\nDigite o valor EXATO de "x" com as duas primeiras casas decimais (se houver)\n')))
  q1_resolucao = float(f'{(A*E)/B:.2f}')
  if q1 == q1_resolucao:
    print('-='*30)
    AD, AC, AB = randint(45, 210), randint(0, 45), randint(30, 145)
    print('Parabéns! Você acertou, então vamos para a questão 2!')
    print('-='*30)
    q2 = float(input(f'A reta transversal (horizontal, separando os dois triângulos) "s" intercepta a\nreta "D" e "E". A qual fazem parte de um triângulo retângulo com dois retângulos\nsemelhantes identificados como "Δ ABC ~ Δ AED".\nConsiderando AD = {AD} ; AE = x ; AC = {AC} ; AB = {AB}\nDigite o valor EXATO de "x" com as duas primeiras casas decimais (se houver)\n'))
    q2_resolucao = float(f'{(AD*AC)/AB:.2f}')
    if q2 == q2_resolucao:
      print('-='*30)
      G, I, K, L, H = randint(0, 30), randint(0, 15), randint(50, 75), randint(10, 40), float(f'{(K*I)/L:.2f}')
      print('Me parece que você irá para a questão 3, eba eba :)')
      q3 = float(input(f'As retas transversais (verticais) "u" e "v" interceptam as retas paralelas\n(horizontais) "r", "s" e "t".\nReta u: G, H, I\nReta v: J, K, L\nConsiderando G = {G} ; H = x ; I = {I} ; J = y ; K = {K} ; L = {L}.\nDetermine o valor EXATO de "y" com as duas primeiras casas decimais (se houver)\n'))
      q3_resolucao = float(f'{(G*K)/H:.2f}')
      if q3_resolucao == q3:
        print('-='*30)
        print(f'Muito bem! Estamos chegando no final do desafio.')
        print('-='*30)
        AB, BC_1, BC_2, CB, BA = randint(0, 15), randint(0, 200), randint(0, 100), randint(0, 50), randint(75, 125)
        q4 = float(input(f'Temos as retas paralelas verticais "a", "b" e "c". Interligadas por duas paralelas horizontais "d" e "e".\nNa reta "d", estão os valores da esquerda para a direita: ab -> {AB} ; bc -> {BC_1}x-{BC_2}\nNa reta "e", estão os valores da direita para a esquerda: cb -> {CB}x ; ba -> {BA}\nDetermine o valor EXATO de "x" com as duas primeiras casas decimais (se houver)\n'))
        q4_resolucao = float(f'{(BA*BC_2)/((AB*CB)-(BA*BC_1)):.2f}')
        if q4 == q4_resolucao:
          print(f'Você completou os exercícios do Teorema de Tales, {name}! Vamos para o próximo? ')
          sleep(5)
        else:
          print(f'Resposta: {q4_resolucao}')
          print(f'\nVocê errou, {name}. Em 5 segundos você irá voltar para o menu principal.')
          sleep(5)
      else:
        print(f'Resposta: {q3_resolucao}')
        print(f'\nVocê errou, {name}. Em 5 segundos você irá voltar para o menu principal.')
        sleep(5)
    else:
      print(f'Resposta: {q2_resolucao}')
      print(f'\nVocê errou, {name}. Em 5 segundos você irá voltar para o menu principal.')
      sleep(5)
  else:
    print(f'Resposta: {q1_resolucao}')
    print(f'\nVocê errou, {name}. Em 5 segundos você irá voltar para o menu principal.')
    sleep(5)

while escolha != 5:
  print('-='*45)
  escolha = int(input(f'[1] - Elementos de um Triângulo (MANUTENÇÃO)\n[2] - Teorema de Tales\n[3] - Teorema de Pitágoras (MANUTENÇÃO)\n[4] - Congruência de triângulos (MANUTENÇÃO)\n[5] - ABANDONAR O JOGO\nQual o nível desejado por você, {name}? '))
  print('-='*45)
  if escolha == 5:
    print('Dyosun lhe aguarda ansiosamente!')
    break
  elif escolha == 2:
    escolha_2()
  elif escolha == 1 or escolha == 3 or escolha == 4:
    print('Número inválido, leia com atenção e digite novamente.')
