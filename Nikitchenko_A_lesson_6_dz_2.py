import requests
from collections import Counter


# Вытаскивает из строки (<remote_addr>, <request_type>, <requested_resource>)
def conv_str(element):
    element = element.replace('"', '').split()
    return element[0], element[5], element[6]


# Запись больших файлов
def download_file(s_url, file):
    r = requests.get(s_url, stream=True)
    with open(file, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)


if __name__ == '__main__':
    url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
    log = requests.get(url)
    local_file = url.split('/')[-1]
    list_tuples = []

    download_file(url, local_file)

    # извлекаем данные в список кортежей
    with open(local_file, 'r') as f:
        for line in f:
            list_tuples.append(conv_str(line))

    # поиск  клиента, отправившего больше всех запросов
    spammer = Counter(list_tuples).most_common(1)
    print(f'IP адрес спамера - {spammer[0][0][0]}\nКоличество отправленных им запросов - {spammer[0][1]}')
