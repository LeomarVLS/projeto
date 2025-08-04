"""Calculadora de IMC"""

Nome = input("Digite o seu nome: ")
altura = float(input("Digite o sua altura: "))
peso = float(input("Digite o sua peso: "))
idade = int(input("Digite o sua idade: "))
imc = peso / (altura ** 2)
observacao = imc
adulto_ou_crianca = idade

if idade <= 17:
    adulto_ou_crianca = 'Criança'
    print("Criança\n")
else:
    adulto_ou_crianca = 'Adulto'
    print("Adulto\n")

print(Nome, 'tem', f"{altura:.2f}", 'de altura', '\nPesa', peso, 'Quilos e seu IMC é', imc, '\n')

if adulto_ou_crianca == 'Adulto':
    if  observacao <= 18.5:
        print("Abaixo do normal", "\nProcure um médico. Algumas pessoas têm um baixo peso por características do seu organismo e tudo bem. Outras podem estar enfrentando problemas, como a desnutrição. É preciso saber qual é o caso.")
    elif observacao <= 24.9:
        print("Normal\n", "\nQue bom que você está com o peso normal! E o melhor jeito de continuar assim é mantendo um estilo de vida ativo e uma alimentação equilibrada.")
    elif observacao <= 29.9:
        print("Sobrepeso\n", "\nEle é, na verdade, uma pré-obesidade e muitas pessoas nessa faixa já apresentam doenças associadas, como diabetes e hipertensão. Importante rever hábitos e buscar ajuda antes de, por uma série de fatores, entrar na faixa da obesidade pra valer.")
    elif observacao <= 34.9:
        print("Obesidade grau I\n", "\nSinal de alerta! Chegou na hora de se cuidar, mesmo que seus exames sejam normais. Vamos dar início a mudanças hoje! Cuide de sua alimentação. Você precisa iniciar um acompanhamento com nutricionista e/ou endocrinologista.")
    elif observacao <= 39.9:
        print("Obesidade grau II\n", "\nMesmo que seus exames aparentem estar normais, é hora de se cuidar, iniciando mudanças no estilo de vida com o acompanhamento próximo de profissionais de saúde.")
    else:
        print("Obesidade grau III\n", "\nAqui o sinal é vermelho, com forte probabilidade de já existirem doenças muito graves associadas. O tratamento deve ser ainda mais urgente.")

if adulto_ou_crianca == 'Criança':
    if observacao <= 13.3:
        print("Abaixo do normal", "\nUma criança abaixo do peso precisa sempre de uma boa avaliação do pediatra, o qual deve em primeiro lugar excluir a suspeita de uma desnutrição. Mas lembre-se que existem famílias com essa característica: uma magreza constitucional que, no caso, é normal. Só o médico saberá dizer.")
    elif observacao <= 16.9:
        print("Peso normal\n", "\nLegal! Estar com peso dentro da faixa da normalidade é ponto positivo para o desenvolvimento infantil. Que essa criança continue assim, apredendo a saborear desde cedo refeições ricas em vegetais e sem o consumo rotineiro de alimentos lotados de açúcar, gordura e sal. Ah, também é importante brincar, correr, fazer muita atividade física.")
    elif observacao <= 18.1:
        print("Sobrepeso\n", "\nÉ a fase inicial do excesso de peso, quando ainda é mais fácil para a criança, na medida em que ela cresce,estabelecer hábitos saudáveis e manter um estado nutricional mais adequado.. Para isso, como sempre, é preciso mudar a rotina de toda a família, com a ajuda do pediatra e de um nutricionista capaz de melhorar os hábitos alimentares da casa.")
    else:
        print("Obesidade\n", '\nInfelizmente, muitas vezes os pais nem acreditam nesse resultado, pois são tantos meninos e meninas acima do peso que todos estão se acostumando com esse padrão. Sem contar que, no passado, uma criança “forte" era tida como “müito saudável". Engano. O problema é sério e o certo é procurar orientação profissional para ajustar os hábitos de toda a família. Afinal, os adultos da casa são os maiores exemplos.')