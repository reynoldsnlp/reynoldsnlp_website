from pathlib import Path
import re

from bs4 import BeautifulSoup

soup = BeautifulSoup(Path('LDC_orig.html').read_text(), 'html5lib')

while soup.script:
    print('deleting', soup.script)
    soup.script.extract()
soup.header.extract()
soup.footer.extract()
soup.aside.extract()
soup.find('div', class_='breadcrumb').extract()
for th in soup.find_all('th'):
    if th.get_text() in {'Requested By', 'Invoice Date', 'Invoice'}:
        th.extract()
for cell in soup.find_all('td'):
    text = cell.get_text()
    if (re.match(r'\d{4}-\d{2}-\d{2}$', text) or
        re.match('Robert Reynolds|Deryle Lonsdale|John Jardine|Don Colton|David Eddington|Eric Ringger|Seth McCombie|Benjamin Jafek|Andrew Carr', text) or
        [True for a in cell.find_all('a') if '/orders/' in a.get('href')]):
        cell.extract()
print(soup.prettify().replace('Corpora Invoiced', 'LDC corpora already invoiced by BYU'))

Path('BYUxLDC.html').write_text(soup.prettify())
