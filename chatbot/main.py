from models import mychatbot
from time import sleep

bot = mychatbot.MyChatBot(name='BotMartins')

training = [
    '1',
    'Você escolheu fazer login',
    '2',
    'Você escolheu cadastrar conta',
    '3',
    'Você escolheu pedir informações',
]

bot.train_bot(training)


def main_menu():
    print(100 * '\n')
    print(f'{bot.greet}! Digite o número da opção que deseja: ')
    print('1 - Fazer login')
    print('2 - Cadastrar conta')
    print('3 - Pedir informações')
    message = int(input('>> '))
    validate(message)


def validate(message):
    if message not in range(1, 4):
        print('Opção inexistente. Tente novamente!')
        sleep(3)
        main_menu()

    print(bot.get_response(message))


main_menu()
bot.clear_database()
