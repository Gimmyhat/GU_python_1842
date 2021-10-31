import requests


# Вытаскивает из строки (<remote_addr>, <request_type>, <requested_resource>)
def conv_str(element):
    element = element.replace('"', '').split()
    return element[0], element[5], element[6]


if __name__ == '__main__':
    link = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
    log = requests.get(link)
    list_tuples = []

    with open('nginx_logs.txt', 'w') as f:
        f.write(log.text)

    with open('nginx_logs.txt', 'r') as f:
        for line in f:
            list_tuples.append(conv_str(line))

    print(list_tuples[:3])  # вывод первых трех значений списка

