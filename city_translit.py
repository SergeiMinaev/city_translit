import re

CITY_RE = re.compile('[^a-zA-Z]')
DATA = {
    'a': {
       'anzherosudzhensk':'анжеро-судженск',
    },
    'b': {
       'bronnitsy':'бронницы',
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
    },
    'l': {
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
    },
    'q': {
    },
    'r': {
       'ramenskoye':'раменское',
    },
    's': {
       'stpetersburg':'санкт-петербург',
    },
    't': {
       'tayga':'тайга',
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
    return DATA[name_en[0]].get(name_en, None)
