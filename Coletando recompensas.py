from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.options import Options
import contas


#chrome_options = Options()
#chrome_options.add_argument("-Headless")
#av = webdriver.Chrome(options = chrome_options)
#henrique
nav = webdriver.Chrome()
sleep(0.5)
nav.get('https://blaze.com/pt/')
nav.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div/div/div[1]/a').click()
sleep(1)
nav.find_element(By.XPATH, '//*[@id="auth-modal"]/div[2]/form/div[1]/div/input').send_keys(contas.henrique_email)
sleep(1)
nav.find_element(By.XPATH, '//*[@id="auth-modal"]/div[2]/form/div[2]/div/input').send_keys(contas.henrique_senha)
sleep(1)
nav.find_element(By.XPATH, '//*[@id="auth-modal"]/div[2]/form/div[4]/button').click()
sleep(2)
nav.get('https://blaze.com/pt/spinners/56')
abrirjanela0 = nav.maximize_window()
sleep(2)
botao_gire = nav.find_element(By.XPATH, '//*[@id="mystery-controller"]/div[3]/button').text
listando = list(botao_gire[0:1])
sleep(1)

if listando == ['G']:
    nav.find_element(By.XPATH, '//*[@id="mystery-controller"]/div[3]/button').click()
    sleep(5)
    nav.get('https://blaze.com/pt/rewards')
    sleep(1)
    botao_disponivel = nav.find_element(By.XPATH,'//*[@id="rewards"]/div/div/div[2]/div/div[3]/div/div[2]/button').text
    listando_bd = list(botao_disponivel[0:1])
    if listando_bd == ['R']:
        nav.find_element(By.XPATH, '//*[@id="rewards"]/div/div/div[2]/div/div[3]/div/div[2]/button').click()
        sleep(2)
        print('Henrique resgatou 1 recompensa!')
        nav.quit()
    else:

        nav.quit()
else:
    print('Henrique Ainda não tem Giro Disponivel!')
    nav.quit()
#matheus
#chrome_options = Options()
#chrome_options.add_argument("-Headless")
#nav = webdriver.Chrome(options = chrome_options)
nav = webdriver.Chrome()
sleep(0.5)
nav.get('https://blaze.com/pt/')
nav.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div/div/div[1]/a').click()
sleep(1)
nav.find_element(By.XPATH, '//*[@id="auth-modal"]/div[2]/form/div[1]/div/input').send_keys(contas.matheus_email)
sleep(1)
nav.find_element(By.XPATH, '//*[@id="auth-modal"]/div[2]/form/div[2]/div/input').send_keys(contas.maria_senha)
sleep(1)
nav.find_element(By.XPATH, '//*[@id="auth-modal"]/div[2]/form/div[4]/button').click()
sleep(2)
nav.get('https://blaze.com/pt/spinners/56')
abrirjanela0 = nav.maximize_window()
sleep(2)
botao_gire = nav.find_element(By.XPATH, '//*[@id="mystery-controller"]/div[3]/button').text
listando = list(botao_gire[0:1])
sleep(1)

if listando == ['G']:
    nav.find_element(By.XPATH, '//*[@id="mystery-controller"]/div[3]/button').click()
    sleep(5)
    nav.get('https://blaze.com/pt/rewards')
    sleep(1)
    botao_disponivel1 = nav.find_element(By.XPATH,'//*[@id="rewards"]/div/div/div[2]/div/div[3]/div/div[2]/button').text
    listando_bd = list(botao_disponivel1[0:1])
    if listando_bd == ['R']:
        nav.find_element(By.XPATH, '//*[@id="rewards"]/div/div/div[2]/div/div[3]/div/div[2]/button').click()
        sleep(2)
        print('Matheus resgatou 1 recompensa !')
        nav.quit()
    else:

        nav.quit()
else:
    print('Matheus Ainda não tem Giro Disponivel!')
    nav.quit()

#claudio
#chrome_options = Options()
#chrome_options.add_argument("-Headless")
#nav = webdriver.Chrome(options = chrome_options)
nav = webdriver.Chrome()
sleep(0.5)
nav.get('https://blaze.com/pt/')
nav.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div/div/div[1]/a').click()
sleep(1)
nav.find_element(By.XPATH, '//*[@id="auth-modal"]/div[2]/form/div[1]/div/input').send_keys(contas.claudio_email)
sleep(1)
nav.find_element(By.XPATH, '//*[@id="auth-modal"]/div[2]/form/div[2]/div/input').send_keys(contas.claudio_senha)
sleep(1)
nav.find_element(By.XPATH, '//*[@id="auth-modal"]/div[2]/form/div[4]/button').click()
sleep(2)
nav.get('https://blaze.com/pt/spinners/56')
abrirjanela0 = nav.maximize_window()
sleep(2)
botao_gire = nav.find_element(By.XPATH, '//*[@id="mystery-controller"]/div[3]/button').text
listando = list(botao_gire[0:1])
sleep(1)

if listando == ['G']:
    nav.find_element(By.XPATH, '//*[@id="mystery-controller"]/div[3]/button').click()
    sleep(5)
    nav.get('https://blaze.com/pt/rewards')
    sleep(1)
    botao_disponivel2 = nav.find_element(By.XPATH,'//*[@id="rewards"]/div/div/div[2]/div/div[3]/div/div[2]/button').text
    listando_bd2 = list(botao_disponivel2[0:1])
    if listando_bd2 == ['R']:
        nav.find_element(By.XPATH, '//*[@id="rewards"]/div/div/div[2]/div/div[3]/div/div[2]/button').click()
        sleep(2)
        print('Claudio tem  1 recompensa !')
        nav.quit()
    else:

        nav.quit()
else:
    print('Claudio Ainda não tem Giro Disponivel!')
    nav.quit()
#karol
#chrome_options = Options()
#chrome_options.add_argument("-Headless")
#nav = webdriver.Chrome(options = chrome_options)
nav = webdriver.Chrome()
sleep(0.5)
nav.get('https://blaze.com/pt/')
nav.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div/div/div[1]/a').click()
sleep(1)
nav.find_element(By.XPATH, '//*[@id="auth-modal"]/div[2]/form/div[1]/div/input').send_keys(contas.karol_email)
sleep(1)
nav.find_element(By.XPATH, '//*[@id="auth-modal"]/div[2]/form/div[2]/div/input').send_keys(contas.karol_senha)
sleep(1)
nav.find_element(By.XPATH, '//*[@id="auth-modal"]/div[2]/form/div[4]/button').click()
sleep(2)
nav.get('https://blaze.com/pt/spinners/56')
abrirjanela0 = nav.maximize_window()
sleep(2)
botao_gire = nav.find_element(By.XPATH, '//*[@id="mystery-controller"]/div[3]/button').text
listando = list(botao_gire[0:1])
sleep(1)

if listando == ['G']:
    nav.find_element(By.XPATH, '//*[@id="mystery-controller"]/div[3]/button').click()
    sleep(5)
    nav.get('https://blaze.com/pt/rewards')
    sleep(1)
    botao_disponivel3 = nav.find_element(By.XPATH,'//*[@id="rewards"]/div/div/div[2]/div/div[3]/div/div[2]/button').text
    listando_bd = list(botao_disponivel3[0:1])
    if listando_bd == ['R']:
        nav.find_element(By.XPATH, '//*[@id="rewards"]/div/div/div[2]/div/div[3]/div/div[2]/button').click()
        sleep(2)
        print('Karol tem 1 recompensa!')
        nav.quit()
    else:

        nav.quit()
else:
    print('Karol Ainda não tem o Giro Disponivel!')
    nav.quit()
#Maria
#chrome_options = Options()
#chrome_options.add_argument("-Headless")
#nav = webdriver.Chrome(options = chrome_options)
nav = webdriver.Chrome()
sleep(0.5)
nav.get('https://blaze.com/pt/')
nav.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div/div/div[1]/a').click()
sleep(1)
nav.find_element(By.XPATH, '//*[@id="auth-modal"]/div[2]/form/div[1]/div/input').send_keys(contas.maria_email)
sleep(1)
nav.find_element(By.XPATH, '//*[@id="auth-modal"]/div[2]/form/div[2]/div/input').send_keys(contas.maria_senha)
sleep(1)
nav.find_element(By.XPATH, '//*[@id="auth-modal"]/div[2]/form/div[4]/button').click()
sleep(2)
nav.get('https://blaze.com/pt/spinners/56')
abrirjanela0 = nav.maximize_window()
sleep(2)
botao_gire = nav.find_element(By.XPATH, '//*[@id="mystery-controller"]/div[3]/button').text
listando = list(botao_gire[0:1])
sleep(1)

if listando == ['G']:
    nav.find_element(By.XPATH, '//*[@id="mystery-controller"]/div[3]/button').click()
    sleep(5)
    nav.get('https://blaze.com/pt/rewards')
    sleep(1)
    botao_disponivel4 = nav.find_element(By.XPATH,'//*[@id="rewards"]/div/div/div[2]/div/div[3]/div/div[2]/button').text
    listando_bd = list(botao_disponivel4[0:1])
    if listando_bd == ['R']:
        sleep(2)
        nav.find_element(By.XPATH, '//*[@id="rewards"]/div/div/div[2]/div/div[3]/div/div[2]/button').click()
        sleep(2)
        print('Maria resgatou 1 recompensa!')
        nav.quit()
    else:

        nav.quit()
else:
    print('Maria Ainda não tem Giro Disponivel!')
    nav.quit()
#caio
#chrome_options = Options()
#chrome_options.add_argument("-Headless")
#nav = webdriver.Chrome(options = chrome_options)
nav = webdriver.Chrome()
sleep(0.5)
nav.get('https://blaze.com/pt/')
nav.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div/div/div[1]/a').click()
sleep(1)
nav.find_element(By.XPATH, '//*[@id="auth-modal"]/div[2]/form/div[1]/div/input').send_keys(contas.caio_email)
sleep(1)
nav.find_element(By.XPATH, '//*[@id="auth-modal"]/div[2]/form/div[2]/div/input').send_keys(contas.caio_senha)
sleep(1)
nav.find_element(By.XPATH, '//*[@id="auth-modal"]/div[2]/form/div[4]/button').click()
sleep(2)
nav.get('https://blaze.com/pt/spinners/57')
abrirjanela0 = nav.maximize_window()
sleep(2)
botao_gire = nav.find_element(By.XPATH, '//*[@id="mystery-controller"]/div[3]/button').text
listando = list(botao_gire[0:1])
sleep(1)

if listando == ['G']:
    nav.find_element(By.XPATH, '//*[@id="mystery-controller"]/div[3]/button').click()
    sleep(5)
    nav.get('https://blaze.com/pt/rewards')
    sleep(1)
    botao_disponivel5 = nav.find_element(By.XPATH,'//*[@id="rewards"]/div/div/div[2]/div/div[3]/div/div[2]/button').text
    listando_bd6 = list(botao_disponivel5[0:1])
    if listando_bd6 == ['R']:
        sleep(2)
        nav.find_element(By.XPATH, '//*[@id="rewards"]/div/div/div[2]/div/div[3]/div/div[2]/button').click()
        sleep(2)
        print('Caio tem 1 recompensa Disponivel!')
        nav.quit()
    else:

        nav.quit()
else:
    print('Caio Ainda não tem Giro Disponivel!')
    nav.quit()
