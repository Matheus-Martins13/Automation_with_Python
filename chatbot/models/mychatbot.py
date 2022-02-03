from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from time import localtime


class MyChatBot:
    def __init__(self, name):
        self.chatbot = ChatBot(name)
        self.trainer = ListTrainer(self.chatbot)
        self.hour = int(localtime()[3])


    @property
    def greet(self):
        greet = ''

        if 00 < self.hour < 12:
            greet = 'Bom dia'
        elif 12 < self.hour < 18:
            greet = 'Boa tarde'
        else: 
            greet = 'Boa noite'
        
        return greet


    def train_bot(self, training):
        self.trainer.train(training)


    def get_response(self, message):
        return self.chatbot.get_response(str(message))
    
    
    def clear_database(self):
        self.chatbot.storage.drop()
