from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    # erro: próprio autor que achou
    # defeito: outra pessoa encontrou, sem executar o software
    # falha: outra pessoa encontrou, ao executar o software

    # lista de seletores de elementos da página (locator)
    _username_input = {'by': By.ID, 'value': 'username'}
    _password_input = {'by': By.ID, 'value': 'password'}
    _submit_button = {'by': By.CSS_SELECTOR, 'value': 'button.radius'}
    _failure_message = {'by': By.CSS_SELECTOR, 'value': 'div.flash.error'}
    _success_message = {'by': By.CSS_SELECTOR, 'value': 'div.flash.success'}
    _login_form = {'by': By.ID, 'value': 'login'}

    # Ações possiveis na página

    # Método de inicialização
    def __init__(self, driver):
        # inicializa o Selenium
        self.driver = driver
        # abre a página que será testada
        self._visitar('http://the-internet.herokuapp.com/login')
        # verificar se o elemento formulario de login esta visivel
        assert self._esta_visivel(self._login_form, 5)

    # metodo que ira realizar o login COM usuario e senha fornecidos
    def com_(self, username, password):
        # forma convencional
        # self.driver.find_element(By.ID, 'username').send_keys('tomsmith')

        # forma em Page Objects
        self._digitar(self._username_input, username)
        self._digitar(self._password_input, password)
        self._clicar(self._submit_button)

    # funçao para validar se é exibida mensagem de sucesso
    def success_message_present(self):
        return self._esta_visivel(self._success_message, 5)

    # funçao para validar se é exibida a mensagem de falha
    def failure_message_present(self):
        return self._esta_visivel(self._failure_message, 5)
