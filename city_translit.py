import re

CITY_RE = re.compile('[^a-zA-Z- ]')
DATA = {
    'a': {
       'anzherosudzhensk':'анжеро-судженск',
    },
    'b': {
       'bronnitsy':'бронницы',
       'biysk':'бийск',
    },
    'c': {
    },
    'd': {
    },
    'e': {
    },
    'f': {
    },
    'g': {
    },
    'h': {
    },
    'i': {
       'ivanteyevka':'ивантеевка',
       'irkutsk':'иркутск',
       'ivanovo':'иваново',
    },
    'j': {
    },
    'k': {
       'kirov':'киров',
       'krasnoarmeysk':'красноармейск',
       'korolyov':'королев',
       'kashira':'кашира',
       'kozhevnikovo':'кожевниково',
       'klin':'клин',
       'klimovsk':'климовск',
       'krasnodar':'краснодар'.
    },
    'l': {
        'leninsk_kuznetsky':'ленинск-кузнецкий',
    },
    'm': {
       'moscow':'москва',
       'mezhdurechensk':'междуреченск',
    },
    'n': {
       'novoaltaysk':'новоалтайск',
    },
    'o': {
       'oktyabrsky':'октябрьский',
    },
    'p': {
       'podolsk':'подольск',
       'plavsk':'плавск',
       'prokopyevsk':'прокопьевск',
    },
    'q': {
    },
    'r': {
       'ramenskoye':'раменское',
    },
    's': {
       'st_petersburg':'санкт-петербург',
       'staraya yurga':'старая юрга',
    },
    't': {
       'tayga':'тайга',
       'tula':'тула',
    },
    'v': {
       'volgograd':'волгоград',
    },
    'u': {
    },
    'w': {
    },
    'x': {
    },
    'y': {
       'yaroslavl':'ярославль',
    },
    'z': {
       'zhukovskiy':'жуковский',
    },
}

def get_city_ru(name_en: str) -> str:
    name_en = CITY_RE.sub('', name_en.lower())
    name_en = name_en.replace('-', '_').replace(' ','_')
    return DATA[name_en[0]].get(name_en, None)
