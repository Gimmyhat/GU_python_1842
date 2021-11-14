import re
import requests


# получение информации вида:
# (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>)
def conv_str(raw):
    remote_addr = re.search(r'^(\d{,3}\.?){4}|(\w{,4}:?){8}', raw)  # находит ipv4 или ipv6
    request_datetime = re.search(r'(?<=\[)(.)*(?=\])', raw)  # '17/May/2015:08:05:32 +0000'
    request_type = re.search(r'(?<=\]\s\")(.)+(?=\s/)', raw)  # 'GET'
    requested_resource = re.search(r'(?<=\s)/[A-Za-z0-9-_/]+', raw)  # '/downloads/product_1'
    response_code = re.search(r'(?<=\" )\d{3}', raw)  # '304'
    response_size = re.search(r'(?<=\"\s\d{3}\s)\d+', raw)  # '0'
    return (remote_addr[0], request_datetime[0], request_type[0], requested_resource[0], response_code[0],
            response_size[0])


if __name__ == '__main__':
    link = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
    log = requests.get(link)
    list_tuples = []

    with open('nginx_logs.txt', 'w') as f:
        f.write(log.text)

    with open('nginx_logs.txt', 'r') as f:
        for line in f:
            list_tuples.append(conv_str(line))

    # вывод первых 4 значений списка
    for i in range(4):
        print(list_tuples[i])
