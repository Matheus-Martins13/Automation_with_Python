"""
Requisitos para que este programa funcione como o esperado: 

1. Instalar a biblioteca Selenium;

2. Ter, no diretório de instalação do Python (ou no ambiente virtual)
o webdriver desejado. Aqui deixei a possibilidade de utilizar tanto 
com o Firefox quanto com o Chrome.

    - Para o Chrome, utilize o chromedriver;
    - Para o Firefox, utilize o geckodriver.
"""


from selenium import webdriver
from time import sleep


class BotInstagram:


    def __init__(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()


    def go_to_link(self, link):
        self.driver.get(link)

    
    def login(self, email, password):
        email_textarea = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        password_textarea = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        sleep(1)
        
        # E-mail
        email_textarea.click()
        sleep(0.5)
        email_textarea = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        sleep(0.5)
        email_textarea.clear()
        sleep(0.5)
        email_textarea.send_keys(email)
        sleep(1)

        # Senha
        password_textarea.click()
        sleep(0.5)
        password_textarea = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        sleep(0.5)
        password_textarea.clear()
        sleep(0.5)
        password_textarea.send_keys(password)
        sleep(0.5)

        # Entrar 
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()


    def get_link_of_pictures(self):
        links = self.driver.find_elements_by_tag_name('a')

        all_links = []
        
        for link in links:
            href = link.get_attribute("href")

            if (href.startswith("https://www.instagram.com/p/")):
                all_links.append(href)

        return all_links


    def give_like(self):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div/div[2]/div/div[2]/section[1]/span[1]/button').click()


    def comment(self, text):
        textarea = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div/div[2]/div/div[2]/section[3]/div/form/textarea')
        sleep(1)
        textarea.click()
        sleep(1)
        textarea = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div/div[2]/div/div[2]/section[3]/div/form/textarea')
        sleep(1)
        textarea.clear()
        sleep(1)
        textarea.send_keys(text)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div/div[2]/div/div[2]/section[3]/div/form/button[2]').click()
