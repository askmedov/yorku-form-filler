from selenium import webdriver
import time

f = open("fill_data.txt", "r")
data = f.read()
data = dict([x.split(': ') for x in data.split('\n')])

houses = {
    'Bethune': 1,
    'Calumet': 2,
    'Founders': 3,
    'Pond': 4,
    'Stong': 5,
    'Tatham': 6,
    'Vanier': 7,
    'Winters': 8,
    'Assiniboine': 9,
    'Passy': 10,
    'Atkinson': 11,
    'Quad': 12,
}

print(data)

cdl = data['webdriver']
w = webdriver.Chrome(cdl)
w.get("https://forms.office.com/Pages/ResponsePage.aspx?id=GBNTNBFw1E-H8KQ4FsSb0Aii_h-sJShOmtngDnHIJ49UNEFPQUJHTzIySDE0N0I1S0s2NjE2MkRRUyQlQCN0PWcu")
time.sleep(2)

name_field = w.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[3]/div[2]/div[2]/div[1]/div/div[2]/div/div/input')
name_answer = data['name']
name_field.send_keys( name_answer )

email_field = w.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div/div[2]/div/div/input')
email_answer = data['email']
email_field.send_keys( email_answer )

phone_field = w.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[3]/div[2]/div[2]/div[3]/div/div[2]/div/div/input')
phone_answer = data['phone']
phone_field.send_keys( phone_answer )

chosen_house = data['house']
path = '//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[3]/div[2]/div[2]/div[4]/div/div[2]/div/div[' + \
        str(houses[chosen_house]) + ']/div/label/input'
house_radio = w.find_element_by_xpath(path)
house_radio.click()

flat_field = w.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[3]/div[2]/div[2]/div[5]/div/div[2]/div/div/input')
flat_answer = data['apartment']
flat_field.send_keys( flat_answer )

submit_button = w.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[3]/div[3]/div[1]/button/div')
submit_button.click()

covid_radio = w.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/div/label/input')
covid_radio.click()

covid_radio = w.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div/label/input')
covid_radio.click()

covid_radio = w.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div[3]/div/div[2]/div/div[2]/div/label/input')
covid_radio.click()

covid_radio = w.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[2]/div/label/input')
covid_radio.click()

covid_radio = w.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div[5]/div/div[2]/div/div[2]/div/label/input')
covid_radio.click()

submit_button = w.find_element_by_xpath('//*[@id="form-container"]/div/div/div/div/div[1]/div[2]/div[3]/div[1]/button[2]/div')
submit_button.click()

time.sleep(5)

w.quit()
