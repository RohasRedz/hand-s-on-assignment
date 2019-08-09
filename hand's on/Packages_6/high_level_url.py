import re

regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

url_list = input("Enter a list of URL: ")

for url in url_list:
    if re.match(regex, url) is not None:
        print("Valid URL")
        start_idx = url.index("wwww") or url.index("//")
        print(url[start_idx:])
    else:
        print("Invalid URL")