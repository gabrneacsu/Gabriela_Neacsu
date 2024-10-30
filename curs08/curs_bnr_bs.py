from bs4 import BeautifulSoup
import requests
import pandas as pd

r = requests.get('https://www.bnr.ro/Cursul-de-schimb-524.aspx', verify=True)
link = BeautifulSoup(r.text, 'html.parser') # am luat contentul de tip text si am zis sa mi-l paseze html
# print(link)
table = link.find_all('table', attrs={"class": "cursTable"})[0]
# print(table)
header = []
dataset = [] #lista mare de valori pe care o umplem cand iesim din for
for tr_index in table.find_all('tr'):
    td_list = []
    if tr_index.find_all('th'):
        # print(tr_index)
        for index_header, th_index in enumerate(tr_index.find_all('th')):
            # print(th_index.get_text()) # cu get_text() imi ia doar informatia, nu imi mai ia si tot codul html (ce e aici sunt capetele de tabel)
            # header.append(th_index.get_text()) # xa0 reprezinta spatiul, in partea de interfata nu vedem, dar vedem cum interpreteaza python
            if index_header < 6:
                header.append(th_index.get_text().replace('\xa0', ' '))
    variabila = ''
    for index, td_value in enumerate(tr_index.find_all('td')):
        print(index, td_value)
        if index == 0:
            variabila = td_value.get_text()
        elif index == 1:
            variabila = f"{variabila} - {td_value.get_text()}"
            td_list.append(variabila)
            # td_list.append(td_value.get_text())
        elif index != 7:
            td_list.append(float(td_value.get_text().replace(',', '.')))
    if len(td_list) > 0:
        dataset.append(td_list)

print(header)
print(dataset)
df = pd.DataFrame(dataset, columns=header)
df.to_csv('CursBnr.csv', header=header)






