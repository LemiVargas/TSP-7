import requests


def get_summary(title: str) -> str:
    """
    Takes the given Wikipedia title and returns a short summary

    Args:
        title: str - Wikipedia title to retrieve data from
    
    Returns:
        str - Summary pulled from the Wikipedia page

    """
    raw = requests.get(f'https://en.wikipedia.org/api/rest_v1/page/summary/{title}')
    return raw.json()['extract']


def get_photos(title: str) -> list:
    """
    Takes the given Wikipedia title and returns a list of associated photos

    Args:
        title: str - Wikipedia title to retrieve data from
    
    Returns:
        list - List of all photos on the given Wikipedia page

    """
    raw = requests.get(f'https://en.wikipedia.org/api/rest_v1/page/media-list/{title}')
    photos = []
    for medium in raw.json()['items']:
        if medium['type'] == 'image':
            photos.append(medium['srcset'][0]['src'])
    return photos


def get_links(title: str) -> list:
    """
    Takes the given Wikipedia title and returns a list of outgoing wiki links

    Args:
        title: str - Wikipedia title to retrieve data from
    
    Returns:
        list - List of all Wikipedia articles linked by the given page

    """
    raw = requests.get(f'https://en.wikipedia.org/api/rest_v1/page/html/{title}').text
    links = []
    # Only finds explicitly wikipedia links
    i = raw.find('<a rel="mw:WikiLink"')
    while i > 0:
        # Gets the href link
        i = raw.find('/', i)
        end = raw.find('"', i)
        links.append(f'https://en.wikipedia.org/wiki{raw[i:end]}')
        # Go to next WikiLink
        i = raw.find('<a rel="mw:WikiLink"', i + 1)
    return links


def get_info(title: str) -> dict:
    """
    Takes the given Wikipedia title and returns a dictionary of useful data

    Args:
        title: str - Wikipedia title to retrieve data from
    
    Returns:
        dict - Dictionary with useful data

    """
    info = {}
    info['summary'] = get_summary(title)
    info['photos'] = get_photos(title)
    info['links'] = get_links(title)
    return info