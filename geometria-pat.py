from math import *
from random import *
from time import *

escolha = 0
name = str(input('Bem-vindo! Me chamo Dyosun, e você? '))
def escolha_2():
  global trofeus_2
  trofeus_2 = 0
  A = randint(0, 30)
  B = randint(30, 90)
  E = randint(90, 270)
  q1 = float(input((f'As retas transversais (verticais) "u" e "v" interceptam as retas paralelas\n(horizontais) "r", "s" e "t".\nReta u: A, B, C.\nReta v: D, E, F.\nConsiderando A = {A} ; B = {B} ; E = {E} ; D = x\nDigite o valor EXATO de "x" com as duas primeiras casas decimais (se houver)\n')))
  q1_resolucao = float(f'{(A*E)/B:.2f}')
  if q1 == q1_resolucao:
    print('-='*30)
    AD = randint(45, 210)
    AC = randint(0, 45)
    AB = randint(30, 145)
    print('Parabéns! Você acertou, então vamos para a questão 2!')
    print('-='*30)
    q2 = float(input(f'A reta transversal (horizontal, separando os dois triângulos) "s" intercepta a\nreta "D" e "E". A qual fazem parte de um triângulo retângulo com dois retângulos\nsemelhantes identificados como "Δ ABC ~ Δ AED".\nConsiderando AD = {AD} ; AE = x ; AC = {AC} ; AB = {AB}\nDigite o valor EXATO de "x" com as duas primeiras casas decimais (se houver)\n'))
    q2_resolucao = float(f'{(AD*AC)/AB:.2f}')
    if q2 == q2_resolucao:
      print('-='*30)
      G = randint(0, 30)
      I = randint(0, 15)
      K = randint(50, 75)
      L = randint(10, 40)
      H = float(f'{(K*I)/L:.2f}')
      print('Me parece que você irá para a questão 3, eba eba :)')
      q3 = float(input(f'As retas transversais (verticais) "u" e "v" interceptam as retas paralelas\n(horizontais) "r", "s" e "t".\nReta u: G, H, I\nReta v: J, K, L\nConsiderando G = {G} ; H = x ; I = {I} ; J = y ; K = {K} ; L = {L}.\nDetermine o valor EXATO de "y" com as duas primeiras casas decimais (se houver)\n'))
      q3_resolucao = float(f'{(G*K)/H:.2f}')
      if q3_resolucao == q3:
        print('-='*30)
        print(f'Muito bem, {name}! Você passou dos exercícios práticos, vamos testar o mínimo do seu conhecimento teórico.')
        print('-='*30)
        print('Assinale as afirmativas verdadeiras com "V" e as alternativas falsas com "V".\na) As retas são linhas finitas formadas por pontos e representadas por letras\nmaiúsculas.\nb) As retas paralelas não tem ponto em comum e estão sempre em uma direção\ndiferente.\nc) As retas perpendiculares possuem um ponto em comum.\nd) As retas transversais cruzam entre elas mesmas.\ne) As retas coincidentes e concorrentes são o mesmo tipo de reta, mas com nomes\ndiferentes.\n')
        print('-='*30)
        q4 = str(input('a) Todas as alternativas são falsas.\nb) VFVFV\nc) FFVVV\nd) FFVVF\nQual a alternativa correta? '))
        if q4 in 'Dd':
          print('-='*30)
          print(f'Parabéns! Em breve, adicionaremos troféus para cada vez que alguém completar um\nlevel, espere para ver.')
          sleep(10)
        else:
          print('Resposta: alternativa D')
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
