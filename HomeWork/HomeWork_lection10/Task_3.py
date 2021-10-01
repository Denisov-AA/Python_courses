import urllib.request

req = urllib.request.Request('http://ya.ru')
response = urllib.request.urlopen(req)
web_page = response.read()


def url_check(web_page):
    start = 0
    while web_page:
        url_start = str(web_page).find("://", start)
        url_end = str(web_page).find('"', url_start)
        start = url_end
        finded_url = str(web_page)[url_start:url_end]
        try:
            web_url = urllib.request.Request("http"+finded_url, method='HEAD')
            if urllib.request.urlopen(url=web_url).getcode() == 200:
                print(f"http{finded_url} - good")
        except ValueError:
            break
        except Exception as text:
            print(f"http{finded_url} - {text}")
            pass


url_check(web_page=web_page)
