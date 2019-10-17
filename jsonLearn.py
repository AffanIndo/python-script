import json

book = {}

book['tom'] = {
    'name': 'tom',
    'address': '1 red streed, NY',
    'phone': 6281208120812
}

book['bob'] = {
    'name': 'bob',
    'address': '1 green streed, NY',
    'phone': 6281308130813
}

s = json.dumps(book)
with open('./jsonFile.json', 'w') as f:
    f.write(s)