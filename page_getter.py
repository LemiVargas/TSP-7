import requests

def get_info(title: str) -> dict:
    """
    Takes the given Wikipedia title and returns a dictionary of useful data

    Args:
        title: str - Wikipedia title to retrieve data from
    
    Returns:
        dict - Dictionary with useful data

    """
    summary = requests.get(f'https://en.wikipedia.org/api/rest_v1/page/summary/{title}')
    info = {}
    info['summary'] = summary.json()['extract']
    media = requests.get(f'https://en.wikipedia.org/api/rest_v1/page/media-list/{title}')
    info['media-list'] = []
    for photo in media.json()['items']:
        if photo['type'] == 'image':
            info['media-list'].append(photo['srcset'][0]['src'])
    print(info['media-list'])

get_info('Apple')