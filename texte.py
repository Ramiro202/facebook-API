import requests

cookies = {
    'datr': 'CfqPZR0hrtwDN1n1rCNgcPz5',
    'sb': 'CfqPZcs0vUVAhlSWK83LKYRJ',
    'wd': '1279x902',
    'fr': '0BvAVYDpaWMBcyFtP.AWWL36XkRnPGZVAN4XL3Ixy4EJM.Blj_oh.mq.AAA.0.0.BlkAvj.AWVxlQqg29Y',
    'sfau': 'AYh6yKVSieE1t3Rb34cNuwbCRdkElKp7pgQbiMYCO2ig1jwQnxPxtEOrIU0N0lM_R_-3SCXXiidNKb_00OppRM0bMa78a-lOFERQSk_1Aom8Q1VF7Vw0tuZ9cBjt2jtWWxhXVMf2EfxgQ5yqm3uSGeDHh9rZb1jRdP8Lpj6C0j3_fmHfFgbOUHEzjClfoLD-FiC3XrTAORbMh_ibsGdpf5eoTJH6OQZmh5c0meHgnJX0oOxxiC7NQQRkWAT1QIREGOxlGRKsiG-2TYGJ7d6uBvHdQ3h4i0YkbSfAYng59EVXxA',
    'sfiu': 'AYg8yMD_8RKoqMAOXUMz7M1GlXQz5pcjdYS9fRwuEry0YmrzqmakOBhaFRhUU1SKkKj5o1wPTTrzZ0ZG4h6Uhe4Bw9Relzswswj75jaQpOkzzFVdUztBtPTIAH718buVer5hHlScNq7O42f5AsvDt_q1uFWLzCDTiUHBQd6Kiq0T31atg6zD1sSPlZQffZ2zp4m3EqC5d7Hr29ZYwCnklnpQ8JeChBhkFCK8ePUQ_yb0_wTjL1-qiVytUTlfpaz6G9k7Uo-yzIkNkKWxI97enYMxHz7vSj9bmWTHs4QQpMZ_nQ',
}

headers = {
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'datr=CfqPZR0hrtwDN1n1rCNgcPz5; sb=CfqPZcs0vUVAhlSWK83LKYRJ; wd=1279x902; fr=0BvAVYDpaWMBcyFtP.AWWL36XkRnPGZVAN4XL3Ixy4EJM.Blj_oh.mq.AAA.0.0.BlkAvj.AWVxlQqg29Y; sfau=AYh6yKVSieE1t3Rb34cNuwbCRdkElKp7pgQbiMYCO2ig1jwQnxPxtEOrIU0N0lM_R_-3SCXXiidNKb_00OppRM0bMa78a-lOFERQSk_1Aom8Q1VF7Vw0tuZ9cBjt2jtWWxhXVMf2EfxgQ5yqm3uSGeDHh9rZb1jRdP8Lpj6C0j3_fmHfFgbOUHEzjClfoLD-FiC3XrTAORbMh_ibsGdpf5eoTJH6OQZmh5c0meHgnJX0oOxxiC7NQQRkWAT1QIREGOxlGRKsiG-2TYGJ7d6uBvHdQ3h4i0YkbSfAYng59EVXxA; sfiu=AYg8yMD_8RKoqMAOXUMz7M1GlXQz5pcjdYS9fRwuEry0YmrzqmakOBhaFRhUU1SKkKj5o1wPTTrzZ0ZG4h6Uhe4Bw9Relzswswj75jaQpOkzzFVdUztBtPTIAH718buVer5hHlScNq7O42f5AsvDt_q1uFWLzCDTiUHBQd6Kiq0T31atg6zD1sSPlZQffZ2zp4m3EqC5d7Hr29ZYwCnklnpQ8JeChBhkFCK8ePUQ_yb0_wTjL1-qiVytUTlfpaz6G9k7Uo-yzIkNkKWxI97enYMxHz7vSj9bmWTHs4QQpMZ_nQ',
    'dpr': '1',
    'origin': 'https://mbasic.facebook.com',
    'referer': 'https://mbasic.facebook.com/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.109", "Google Chrome";v="120.0.6099.109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '"6.5.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'viewport-width': '1279',
}

params = {
    'refsrc': 'deprecated',
    'lwv': '100',
    'refid': '8',
}

data = {
    'lsd': 'AVpw_bH5CCo',
    'jazoest': '2945',
    'm_ts': '1703978425',
    'li': 'uaWQZaj6xZnVkDNIJut7dxBx',
    'try_number': '0',
    'unrecognized_tries': '0',
    'email': '955500564',
    'pass': 'NetUnitel',
    'login': 'Entrar',
    'bi_xrwh': '0',
}

response = requests.post(
    'https://mbasic.facebook.com/login/device-based/regular/login/',
    params=params,
    headers=headers,
    data=data,
)
with open("index.html", "wt") as file:
    file.write(response.text)