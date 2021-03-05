print('My pet is a worm')

name = 'Pyworm'
age = 7
weight = 10.5
hungry = True
photo = '~~~~~~~'

worm = {
     'name': 'Pyworm',
     'age': 7,
     'weight': 10.5,
     'hungry': True,
     'photo': '~~~~~~~',
}

print("It's called " + worm["name"] + "!" + "\n" +
      "And now I'll feed her""\n")
def feed(worm):
    worm['hungry'] = True
    worm['weight'] += 1.5
    worm['photo'] += '~~'

print('Her actual weight is', worm['weight'],
      '\n''She looks like this:''\n' + worm['photo'],'\n')

feed(worm)

input('Press Enter...''\n')

print('My worm ate the food and its final weight is', worm['weight'],
      '\n''Now she looks like this:''\n' + worm['photo'])
