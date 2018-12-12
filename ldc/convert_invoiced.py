from pathlib import Path
import re

from bs4 import BeautifulSoup


def sorter(tr):
    """Sort table rows by LDC catalog ID (add `19` to the 90s)."""
    return re.sub('^LDC9', 'LDC199', tr.td.a.get_text().strip())


soup = BeautifulSoup(Path('LDC_orig.html').read_text(), 'html5lib')

# remove extraneous stuff
while soup.script:
    print('deleting', soup.script)
    soup.script.extract()
soup.header.extract()
soup.footer.extract()
soup.aside.extract()
soup.find('div', class_='breadcrumb').extract()

# strip internal info from table
for th in soup.find_all('th'):
    if th.get_text() in {'Requested By', 'Invoice Date', 'Invoice'}:
        th.extract()
for cell in soup.find_all('td'):
    text = cell.get_text()
    if (re.match(r'\d{4}-\d{2}-\d{2}$', text) or
        re.match('Robert Reynolds|Deryle Lonsdale|John Jardine|Don Colton|David Eddington|Eric Ringger|Seth McCombie|Benjamin Jafek|Andrew Carr', text) or
        [True for a in cell.find_all('a') if '/orders/' in a.get('href')]):
        cell.extract()

# sort the table by catalog ID
new_table = soup.new_tag('table')
new_table.append(soup.table.thead)
new_table.append(soup.new_tag('tbody'))
for tr in sorted(soup.find_all('tr'), key=sorter):
    new_table.tbody.append(tr)
soup.table.replace_with(new_table)

# Change h1 header
new_h1 = soup.new_tag('h1')
new_h1.string = 'LDC corpora already invoiced by BYU'
soup.h1.replace_with(new_h1)

print(soup.prettify())

Path('BYUxLDC.html').write_text(soup.prettify())
