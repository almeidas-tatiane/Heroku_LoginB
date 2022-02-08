import pytest

from . import config

def pytest_addoption(parser):
    parser.addoption('--baseurl',
                     action='store',
                     default='https://the-internet.herokuapp.com',
                     help='endereço do site alvo do teste'

    )

    parser.addoption('--host',
                     action='store',
                     default='saucelabs',
                     help='ambiente em que vou executar os testes'

    )

    parser.addoption('--browser',
                     action='store',
                     default='chrome',
                     help='navegador padrão'
                     )

    parser.addoption('--browserversion',
                     action='store',
                     default='98.0',
                     help='versão do navegador'
                     )

    parser.addoption('--plataform',
                     action='store',
                     default='Windows 10',
                     help='versão do sistema operacional'

    )

@pytest.fixture
def driver(request):
    config.baseurl = request.config.getoption('--baseurl')
    config.baseurl = request.config.getoption('--host')
    config.baseurl = request.config.getoption('--browser')
    config.baseurl = request.config.getoption('--browserversion')
    config.baseurl = request.config.getoption('--platform')

    if config.host == 'saucelabs':
        test_name = request.node.name #adicionar o nome do teste baseado no script
        capabilities = {
            'browserName': config.browser,
            'browserVersion': config.browserversion,
            'platformName': config.plataform,
            'sauce.options': {
                'name': test_name, #nome do teste conforme acima
            }

        }
        #_credentials =