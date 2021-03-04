print("Welcome to Pypet!", "\n" +
      "We'll try to feed Pyworm""\n")

input('Press Enter...')

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
def feed(worm):
    if worm['hungry'] == False:
        worm['hungry'] = True
        worm['weight'] = worm['weight'] + 1.5
        worm['photo'] = worm['photo'] + '~~'
    else:
        print('Pyworm is not hungry!''\n')

feed(worm)
print('Her weight is', worm['weight'],
      'and she looks like this:''\n' + worm['photo'])
