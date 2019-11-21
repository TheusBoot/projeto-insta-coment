from ui import Ui_MainWindow
from selenium import webdriver
from selenium.webdriver.common.keys import*
import random
import sys
import time
from threading import Thread
from PySide2 import QtCore, QtGui, QtWidgets
   
 
class Automatiza:
    """modo Teste ON AND OF == OFF"""
 
    def __init__(self):
        #self.browser = webdriver.Chrome('C:/chromedriver.exe')
        self.browser = webdriver.Firefox()
        self.login()
        self.encontrar()
 
 
    def login(self):
        self.browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(2)
 
        campo_usuario = self.browser.find_element_by_xpath("//input[@name='username']")
        campo_usuario.clear()
        campo_usuario.send_keys(self.usuario)
        time.sleep(1)
 
        campo_senha = self.browser.find_element_by_xpath("//input[@name='password']")
        campo_senha.clear()
        campo_senha.send_keys(self.senha)
        time.sleep(1)
 
        btn_login = self.browser.find_element_by_xpath("//button[@type='submit']")
        btn_login.click()
        time.sleep(2)
 
    def encontrar(self):
        self.pegarTopPosts()
        self.execute()
        self.finalizar()
 
    def pegarTopPosts(self):
        for hashtag in self.hashtags:
            self.browser.get('https://www.instagram.com/explore/tags/' + hashtag +'/')
            time.sleep(2)
 
            links = self.browser.find_elements_by_tag_name('a')
            condicao = lambda link: '.com/p/' in link.get_attribute('href')
            links_validos = list(filter(condicao, links))
 
            for i in range(0, 9):
                link = links_validos[i].get_attribute('href')
                if link not in self.links:
                    self.links.append(link)
 
 
    def execute(self):
        for link in self.links:
            self.browser.get(link)
            time.sleep(1)
 
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
           
            self.comentario()
            time.sleep(2)
           
            self.like()
 
            self.preco += 0.02
            tempo = random.randint(18, 28)
            time.sleep(tempo)
 
    def comentario(self):
        comentario_input = lambda: self.browser.find_element_by_tag_name('textarea')
        comentario_input().click()
        comentario_input().clear()
 
        comentario = random.choice(self.comentarios)
        for coment in comentario:
            comentario_input().send_keys(coment)
            delay = random.randint(1, 7) / 30
            time.sleep(delay)
 
        comentario_input().send_keys(Keys.RETURN)
 
    def like(self):
        btn_like = lambda: self.browser.find_element_by_xpath('//span[@class="glyphsSpriteHeart__outline__24__grey_9 u-__7"]')
        btn_like().click()
 
    def finalizar(self):
        print ('Você realizou $' + str(self.preco) + ' do método hoje.')
        self.browser.close()
        sys.exit()

# Essa class é a responsável por juntar outras 3 classes nela, porém aqui não estamos
# Não estamos passando a inicilização dessas outras classes e sim só seus objetos para
# que seja trata de uma certa forma e utilizamos a boa prática. 


class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow,Automatiza):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.btn_ok.clicked.connect(self.th)

    def execute_table(self):
        self.usuario = self.user_edit.text()
        self.senha = self.senha_edit.text()
        self.hashtags = self.hashtag_edit.text()
        #self.comentarios = self.comente_edit.text()
        self.comentarios = self.comente_edit.toPlainText()
        Automatiza()
        #print(f'{self.usuario} {self.senha_edit} {self.hashtags} {self.comentarios}')
    
    def th(self):
        Thread(target=self.execute_table, daemon=True).start()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
