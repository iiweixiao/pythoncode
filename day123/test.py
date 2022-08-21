import requests


url = 'https://www.southwest.com/air/booking/select.html?adultPassengersCount=1&departureDate=2022-08-26&departureTimeOfDay=ALL_DAY&destinationAirportCode=BWI&fareType=USD&int=HOMEQBOMAIR&originationAirportCode=ORD&passengerType=ADULT&reset=true&returnDate=&returnTimeOfDay=ALL_DAY&tripType=oneway'
url = 'https://www.southwest.com/api/air-booking/v1/air-booking/page/air/booking/shopping'

data = {
    'adultPassengersCount': "1",
    'application': "air-booking",
    'departureDate': "2022-08-26",
    'departureTimeOfDay': "ALL_DAY",
    'destinationAirportCode': "BWI",
    'fareType': "USD",
    'int': "HOMEQBOMAIR",
    'originationAirportCode': "ORD",
    'passengerType': "ADULT",
    'reset': "true",
    'returnDate': "",
    'returnTimeOfDay': "ALL_DAY",
    'site': "southwest",
    'tripType': "oneway",
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Cookie': 'akacd_RWASP-default-phased-release=3838197008~rv=94~id=a3a3d9dfc7bb6f735447e11a0bfefe5d; at_check=true; akavpau_prd_non_vision=1660744815~id=69f5850c89e38a845620706fbf709db4; sRpK8nqm_sc=Az2VEayCAQAA4BlknkTV0rERD4gtQsTLAM7BRSYELonGtVxvyEg-gehgiqbdAXAC4oCucm46wH8AAOfvAAAAAA|1|1|4db61e445281d8f352bbb77bb70036ce70230bbe; s_ecid=MCMID%7C86841209952088934297072921412597216952; AMCVS_65D316D751E563EC0A490D4C%40AdobeOrg=1; s_cc=true; nmstat=2b636f8a-2611-6707-30ab-3f2c7c7b1ce0; _mibhv=anon-1660744218843-7911951553_4971; MP_LANG=en; _up=1.2.1062638808.1660744506; sRpK_XA_swc=%7B%22_fr%22%3A20000%2C%22c%22%3A%22OVdBVGE3bmdTM3htdFQ0Qw%3D%3DzzwAOLgdhOz1kA6E2LUo1LUiIeoo15KtMWKZwLOXdIpFWYj5W56x2edJ_0J-ZCr2nf4fr22ei_mKiQqs-vACg2Sj9i-szF7m9NIiraomm8-eeh68Ay5K7GiD0KXzdQ7vA2g%3D%22%2C%22dc%22%3A%22000%22%2C%22mf%22%3A0%2C%22fr%22%3A%22X9uhmf7EPoKX7DJ0dGQpNw%3D%3DDoQvW2_G-C3u9JVUmDVyUtZ-V6Y1cjGHoFsQb_ko4HGG1OKKtbY6savPP4qPFv5uX57Cjtj1sfmvhn0hnhUblmimsKZl8G-KfxSGD1uDpkSGIdU%3D%22%2C%22ct%22%3A%22N0xqfP9dvTHN%2FDf8tmCks8VQCfOb7B2h3XED9U4%3D%22%7D; weiygrety=GEBpqNIg; MPEL=EL; X-AK-PIM-INJECT=sync; akavpau_prd_air_booking=1660745313~id=60b9ecbca38f19267158133ecc1985e5; valid_promo=false; s_gpv_pn=BOOK%3AAIR%3ASelect%20Flight%20Page; s_sq=%5B%5BB%5D%5D; AMCV_65D316D751E563EC0A490D4C%40AdobeOrg=1176715910%7CMCIDTS%7C19222%7CMCMID%7C86841209952088934297072921412597216952%7CMCAID%7CNONE%7CMCOPTOUT-1660751915s%7CNONE%7CvVersion%7C5.4.0; mbox=session#ed4c041a8326425a8e335f34aa469f7f#1660746624|PC#ed4c041a8326425a8e335f34aa469f7f.32_0#1723989309',
    'Host': 'www.southwest.com',
    'Origin': 'https://www.southwest.com',
    'Referer': 'https://www.southwest.com/air/booking/select.html?adultPassengersCount=1&departureDate=2022-08-26&departureTimeOfDay=ALL_DAY&destinationAirportCode=BWI&fareType=USD&int=HOMEQBOMAIR&originationAirportCode=ORD&passengerType=ADULT&reset=true&returnDate=&returnTimeOfDay=ALL_DAY&tripType=oneway',
}
resp = requests.get(url=url, data=data)
print(resp)
