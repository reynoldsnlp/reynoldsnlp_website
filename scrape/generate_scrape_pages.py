"""Generate html pages for toy scraping project."""

from random import sample

letters = 'abcdefghijklmnopqrstuvwxyz'
combos = [a + b for a in letters for b in letters]

for c in combos:
    with open(c + '.html', 'w') as h_file:
        h_file.write('<!DOCTYPE html>\n')
        h_file.write('<html>\n<body>\nHere are the links: <br />\n')
        counter = 1
        for lnk in sample(combos, 10):
            if lnk != c:  # don't put page's link to itself
                h_file.write('<a href="https://reynoldsnlp.com/scrape/' + lnk +
                             '.html">Link {}</a> <br />\n'.format(counter))
                counter += 1
        h_file.write('</body>\n</html>\n')
