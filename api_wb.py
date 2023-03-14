import re

import requests as requests

CLEAN = re.compile('<.*?>')


def clean_html(raw_html):
    clean_text = re.sub(CLEAN, '', raw_html)
    return clean_text


async def get_keys_from_api(art, telegram_id):
    data = {
        'arts':
            art,
        'subj':
            1,
        'pop_min':
            10
    }

    url = 'https://marpla.ru/wb/settings_get_qs_by_arts.php'
    r = requests.post(url=url, data=data)

    info = clean_html(r.text)

    final_info = ''.join([x for x in info if not x.isdigit()])

    file = open(f'key_data_{telegram_id}.txt', 'w', encoding='utf-8')
    file.write(final_info)
    file.close()

