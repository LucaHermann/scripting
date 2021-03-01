import requests

cookies = {
    '__stripe_mid': '0f483b43-a43f-4ec0-9f13-1da840fd90291a0508',
    'cookieLawSeen': 'true',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:87.0) Gecko/20100101 Firefox/87.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0',
    'If-None-Match': 'W/"d7f6-LPeLItTxk4t2YdOsB2pWyzZcvHI-gzip"',
}

response = requests.get(
    'https://www.emerita.legal/abogado/a', headers=headers, cookies=cookies)

print(response.content)
