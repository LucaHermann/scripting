import requests

cookies = {
    '__stripe_mid': '0f483b43-a43f-4ec0-9f13-1da840fd90291a0508',
    'cookieLawSeen': 'true',
    '__stripe_sid': '38e4a151-9c00-4fca-91f0-51b1bd33667e601599',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:87.0) Gecko/20100101 Firefox/87.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Referer': 'https://www.emerita.legal/abogado/a',
    'If-Modified-Since': 'Fri, 19 Feb 2021 15:35:10 GMT',
    'If-None-Match': '"393-5bbb232941ffb-gzip"',
    'Cache-Control': 'max-age=0',
    'TE': 'Trailers',
}

response = requests.get(
    'https://www.emerita.legal/65-es2015.b4f35766bf8a5b1a8d4d.js', headers=headers, cookies=cookies)
