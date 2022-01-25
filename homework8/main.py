import argparse
import json
import os
from collections import defaultdict
import re


def get_top3_ip_address(ip_address_dict):
    top3_ip_address = dict(sorted(ip_address_dict.items(), key=lambda x: x[1], reverse=True)[:3])
    return top3_ip_address


def get_top3_long_requests(long_requests):
    long_requests.sort(key=lambda long_requests: long_requests['request_time'], reverse=True)
    top3_long_requests = long_requests[:3]
    return top3_long_requests


def get_all_requests(dictionary):
    all_requests = dictionary['GET'] + dictionary['POST'] + dictionary['PUT'] + dictionary['DELETE'] + dictionary[
        'HEAD'] + dictionary['CONNECT'] + dictionary['OPTIONS'] + dictionary['TRACE']
    return all_requests


def check_log_file(file):
    dictionary = {'GET': 0,
                  'POST': 0,
                  'PUT': 0,
                  'DELETE': 0,
                  'HEAD': 0,
                  'CONNECT': 0,
                  'OPTIONS': 0,
                  'TRACE': 0,
                  'PATCH': 0,
                  'top_3_ip_address': None,
                  'top_3_long_requests': None,
                  'all_requests': 0}
    ip_address_dict = defaultdict(int)
    long_requests = []
    with open(file) as file:
        for line in file:
            ip_address = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
            method = re.search(r'] "(GET|POST|PUT|DELETE|HEAD|CONNECT|OPTIONS|TRACE|PATCH)', line)
            request_time = re.search(r'(?<!\.)\d+\n', line)
            url = re.search(r' (\/.*) HTTP', line)
            request_datetime = re.search(r'\[(.*)] ', line)
            if method is not None:
                dictionary[method.group(1)] += 1
            if ip_address:
                ip_address_dict[ip_address.group()] += 1
                dictionary['all_requests'] +=1
            if request_time is not None:
                if url is not None:
                    url = url.group(1)
                elif url is None:
                    url = None
                if method is not None:
                    method = method.group(1)
                elif method is None:
                    method = None
                data = {'ip_address': ip_address.group(),
                        'method': method,
                        'url': url,
                        'datetime': request_datetime.group(1),
                        'request_time': int(request_time.group()[:-1])
                        }
                long_requests.append(data)
        # dictionary['all_requests'] = get_all_requests(dictionary)
        top3_ip_address = get_top3_ip_address(ip_address_dict)
        dictionary['top_3_ip_address'] = top3_ip_address
        top3_long_requests = get_top3_long_requests(long_requests)
        dictionary['top_3_long_requests'] = top3_long_requests
        print('Results for file: ' + file.name)
        print(json.dumps(dictionary, indent=4))
        return dictionary


def write_result(result, file_name):
    with open(file_name, 'w') as file:
        json.dump(result, file, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--f", dest='file', action='store', help="path to log file")
    args = parser.parse_args()

    if '.log' in args.file:
        result = check_log_file(args.file)
        write_result(result, args.file + '_result.json')
    else:
        path = args.file
        files = os.listdir(path)
        logs_files = [file for file in files if file.endswith('.log')]
        for file in logs_files:
            result = check_log_file(path + file)
            write_result(result, file + '_result.json')
