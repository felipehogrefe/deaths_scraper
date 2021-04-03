from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import traceback
from selenium.webdriver.common.keys import Keys

months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
states = ['Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Distrito Federal', 'Espírito Santo', 'Goiás', 'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Paraná', 'Paraíba', 'Pará', 'Pernambuco', 'Piauí', 'Rio Grande do Norte', 'Rio Grande do Sul', 'Rio de Janeiro', 'Rondônia', 'Roraima', 'Santa Catarina', 'Sergipe', 'São Paulo', 'Tocantins']
years = ['2021', '2020', '2019', '2018', '2017', '2016', '2015']


def main():
    chrome_options = configure_chrome()
    chrome = webdriver.Chrome('chromedriver.exe', options=chrome_options)
    try:
        scrap_data(chrome)
    except:
        traceback.print_exc()
        chrome.close()


def scrap_data(chrome):

    url = "https://transparencia.registrocivil.org.br/registros"
    chrome.get(url)
    time.sleep(1)
    deaths_rb = chrome.find_element_by_xpath('//*[@id="__BVID__53"]/div[4]/label')
    deaths_rb.click()

    for year in years:
        with open(str(year)+'.csv', 'w') as out:
            for month in months:
                str_out = month+'\t'

                for estado_valor in extract_data(year, chrome, month).text.split('\n')[4:]:
                    str_out += estado_valor.split()[-1]+'\t'

                out.write(str_out+'\n')

    chrome.close()


def extract_data(year, chrome, month):
    define_year(year, chrome)
    define_month(chrome, month)
    click_search_btn(chrome)
    time.sleep(2)
    results_table = chrome.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div/div/div[2]/div/div[3]/div/div/div/div/div[2]/div[2]/div')
    return results_table


def click_search_btn(chrome):
    btn_search = chrome.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[5]/button')
    btn_search.click()


def define_month(chrome, month):
    month_cb = chrome.find_element_by_xpath('//*[@id="__BVID__62"]/div/div/div[2]')
    month_cb.click()
    month_input = chrome.find_element_by_xpath('//*[@id="__BVID__62"]/div/div/div[2]/input')
    month_input.send_keys(month)
    month_input.send_keys(Keys.ENTER)


def define_year(year, chrome):
    year_cb = chrome.find_element_by_xpath('//*[@id="datePickrGroup"]/div/div/div[2]')
    year_cb.click()
    year_input = chrome.find_element_by_xpath('//*[@id="datePickrGroup"]/div/div/div[2]/input')
    year_input.send_keys(year)
    year_input.send_keys(Keys.ENTER)


def configure_chrome():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--verbose')
    chrome_options.add_experimental_option("prefs", {
        "safebrowsing_for_trusted_sources_enabled": False,
        "safebrowsing.enabled": False
    })
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-software-rasterizer')
    return chrome_options


if __name__ == '__main__':
    main()


