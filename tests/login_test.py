import os
import pytest
from selenium import webdriver

from pages.login_page import LoginPage


# um padrão para o PyTest executar no inicio e no final dos testes
@pytest.fixture  # padrao para começar
def login(request):
    # anteriormente apontavamos o Chrome Driver diretamente
    # _chromedriver = 'vendor/chromedriver.exe'
    _chromedriver = os.path.join(os.getcwd(), 'vendor', 'chromedriver.exe')  # vantajoso quando rodamos em ambiente na nuvem como SauceLabs
    print('CWD = ' + _chromedriver)

    # caso o Chrome Driver nao esteja na pasta indicada do projeto
    # vamos usar a configuração geeral do servidor / serviço

    # se encontrar o arquivo localmente
    if os.path.isfile(_chromedriver):
        driver_ = webdriver.Chrome(_chromedriver)

    # se não encontrou localmente
    else:
        # usando o Chrome Driver do servidor / serviço, usando variaveis de ambiente do servidor
        driver_ = webdriver.Chrome()

    # instanciar a LoginPage e por consequencia a BasePage e herdar tudo delas
    loginPage = LoginPage(driver_)

    # função de finalização do teste está contida na função de inicialização (login)
    def quit():
        driver_.quit()  # desligou o Selenium -> Para execução local

    # chamar o quit (a finalização)  -> Para execução remota, coloca na fila para executar a função
    request.addfinalizer(quit)
    return loginPage


# terminou a função de Login

# começam os testes
# não esqueça de alinhar na margem
# <----------------

def testar_login_com_sucesso(login):
    # faça o login com este usuario e senha
    login.com_('tomsmith', 'SuperSecretPassword!')
    # validar o resultado = mensagem de sucesso presente
    assert login.success_message_present()


def testar_login_com_usuario_invalido(login):
    login.com_('juca', 'SuperSecretPassword!')
    assert login.failure_message_present()
    # assert login.success_message_present() == False


def testar_login_com_senha_invalida(login):
    login.com_('tomsmith', 'xpto1234!')
    assert login.failure_message_present()
