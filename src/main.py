from city import City
from country import Country

g = Country()

g.add_city('Buch')
g.add_city('Urzi')
g.add_city('Giu')
g.add_city('Pite')
g.add_city('Faga')

g.add_route('Buch', 'Urzi', [85, 9, 2])
g.add_route('Buch', 'Giu', [90, 8, 1])
g.add_route('Buch', 'Pite', [101, 8, 0])
g.add_route('Buch', 'Faga', [211, 8, 3])

for v in g:
    for w in v.get_connections():
        vid = v.get_name()
        wid = w.get_name()
        print ('( %s , %s, %s)'  % ( vid, wid, v.get_data(w)))
