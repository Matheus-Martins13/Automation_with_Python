from bot_instagram import BotInstagram
from time import sleep


def main():

    email = input('Digite o seu e-mail de login do instagram: ')
    password = input('Digite a senha de login do instagram: ')
    link_account = input('Digite o link da conta do instagram que deseja entrar: ')
    text = input('Digite o comentário que deseja fazer nas fotos: ')

    bot = BotInstagram()
    bot.go_to_link('https://www.instagram.com/')
    sleep(4)

    bot.login(email, password)
    sleep(3)

    bot.go_to_link(link_account)
    sleep(2)

    pictures_links = bot.get_link_of_pictures()

    for picture_link in pictures_links:
        bot.go_to_link(picture_link)
        sleep(2)
        bot.give_like()
        sleep(2)
        bot.comment(text)
        sleep(1)


if __name__== '__main__':
    main()
