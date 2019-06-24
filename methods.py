import requests


import data_base_work as db


# url = 'https://stackoverflow.com/questions/tagged/python'
# url_1 = 'http://flask.pocoo.org/docs/1.0/quickstart/'
# url_2 = 'fghfghfgh://jhvjh.com/kjnkj'
# url_3 = 'https://docs.python.org/3/library/stdtypes.html'
# url_4 = 'https://docs.python.org/3/library/'
# url_5 = 'https://docs.python.org/3/'
# sp = 'short-link'


def check_requests(full_url_address):
    """
    does the site exist?
    :param full_url_address: from *html form
    :return: True/False
    """
    try:
        requests.get(full_url_address)
        return True
    except requests.exceptions.RequestException as e:
        print(e)
        print('URL does not exist. Insert existing URL')
        return False


def check_protocol(full_url_address):
    """
    Defines the protocol
    :param full_url_address: str
    :return: https/http/False
    """
    exists_url_address = check_requests(full_url_address)
    http = full_url_address[0:7:1]
    https = full_url_address[0:8:1]
    if exists_url_address is True and https == 'https://':
        return https
    if exists_url_address is True and http == 'http://':
        return http
    else:
        return False


def cut_full_url(full_url_address):
    """
    Returns protocol + domain_name
    :param full_url_address: str
    :return: top_address = protocol + domain_name
    """
    protocol = check_protocol(full_url_address)
    if protocol == 'https://':
        domain_length = full_url_address.find('/', 8, len(full_url_address))
        domain_length = domain_length + 1
        domain_name = full_url_address[8:domain_length:1]
        top_address = protocol + domain_name
        return top_address
    if protocol == 'http://':
        domain_length = full_url_address.find('/', 7, len(full_url_address))
        domain_length = domain_length + 1
        domain_name = full_url_address[7:domain_length:1]
        top_address = protocol + domain_name
        return top_address


def check_full_url_address_in_database_user(full_url_address, user):
    """
    :param full_url_address: str
    :return: True/False
    """
    query_str = f'''SELECT URL_full FROM URL
                    WHERE URL_full = '{full_url_address}' AND Users_Id = {user};
                    '''
    query = db.query_db(query_str)
    if query:
        return True
    else:
        return False


def check_short_url_address_in_database_user(short_url_address, user):
    """
    :param short_url_address: str
    :return: True/False
    """
    query_str = f'''SELECT URL_short FROM URL
                    WHERE URL_short = '{short_url_address}' AND Users_Id = {user};
                    '''
    query = db.query_db(query_str)
    if query:
        for string in query:
            for line in string:
                return line
    else:
        return False


def abbreviation_auto_user(full_url_address, user):
    """
    reduces to a domain with automatic naming and writes to database
    :param full_url_address: str
    :return: True/False
    """
    top_address = cut_full_url(full_url_address)
    short_part_letter = 'short-ad-'
    short_part_number = 0
    short_url_address = top_address + short_part_letter + str(short_part_number)
    if check_full_url_address_in_database_user(full_url_address) is False:
        while check_short_url_address_in_database(short_url_address) is not False:
            short_part_number += 1
            short_url_address = top_address + short_part_letter + str(short_part_number)
            check_short_url_address_in_database(short_url_address)

        query_str = f'''INSERT INTO URL (URL_full, URL_short, Users_Id)
                        VALUES ('{full_url_address}', '{short_url_address}', {user});
                        '''
        db.query_save_db(query_str)
        return True
    else:
        return False


def abbreviation_input_user(full_url_address, short_part, user):
    """
    Enter the abbreviation
    :param full_url_address: str
    :return: True/False
    """
    top_address = cut_full_url(full_url_address)
    short_url_address = top_address + short_part
    if check_full_url_address_in_database_user(full_url_address) is False:
        while check_short_url_address_in_database(short_url_address) is not False:
            message = print('Enter new address')
            return message
        query_str = f'''INSERT INTO URL (URL_full, URL_short, Users_Id)
                        VALUES ('{full_url_address}', '{short_url_address}', {user});
                        '''
        db.query_save_db(query_str)
        return True
    else:
        return False


# БЕЗ ЮЗЕРОВ


def check_full_url_address_in_database(full_url_address):
    """
    :param full_url_address: str
    :return: True/False
    """
    query_str = f'''SELECT URL_full FROM URL
                    WHERE URL_full = '{full_url_address}';
                    '''
    query = db.query_db(query_str)
    if query:
        return True
    else:
        return False


def check_short_url_address_in_database(short_url_address):
    """
    :param short_url_address: str
    :return: True/False
    """
    query_str = f'''SELECT URL_short FROM URL
                    WHERE URL_short = '{short_url_address}';
                    '''
    query = db.query_db(query_str)
    if query:
        for string in query:
            for line in string:
                return line
    else:
        return False


def abbreviation_auto(full_url_address):
    """
    reduces to a domain with automatic naming and writes to database
    :param full_url_address: str
    :return: True/False
    """
    top_address = cut_full_url(full_url_address)
    short_part_letter = 'short-ad-'
    short_part_number = 0
    short_url_address = top_address + short_part_letter + str(short_part_number)
    if check_full_url_address_in_database_user(full_url_address) is False:
        while check_short_url_address_in_database(short_url_address) is not False:
            short_part_number += 1
            short_url_address = top_address + short_part_letter + str(short_part_number)
            check_short_url_address_in_database(short_url_address)

        query_str = f'''INSERT INTO URL (URL_full, URL_short, Users_Id)
                        VALUES ('{full_url_address}', '{short_url_address}', '2');
                        '''
        db.query_save_db(query_str)
        return True
    else:
        return False


def abbreviation_input(full_url_address, short_part):
    """
    Enter the abbreviation
    :param full_url_address: str
    :return: True/False
    """
    top_address = cut_full_url(full_url_address)
    short_url_address = top_address + short_part
    if check_full_url_address_in_database(full_url_address) is False:
        while check_short_url_address_in_database(short_url_address) is not False:
            message = print('Enter new address')
            return message
        query_str = f'''INSERT INTO URL (URL_full, URL_short, Users_Id)
                        VALUES ('{full_url_address}', '{short_url_address}', '2');
                        '''
        db.query_save_db(query_str)
        return True
    else:
        return False




#
# tt = abbreviation_input(url, sp)
# print(tt)
#
#
#
# i = abbreviation_auto(url_4)
# print(i)
#
# y = check_requests(url)
# print(y)
#
# # t = make_url_short_automatically(url)
# # print(t)
#
# a = url[0:8:1]
# print(a)
#
# address_length = url.find('/', 8, len(url))
# print(address_length)
#
# r = check_full_url_address_in_database(url_1)
# print(r)
#
# # y = abbreviation(url)
# # print(y)
#
# q = check_short_url_address_in_database('https://stackoverflow.com/aaa2')
# print(q)
#
#
# yy = cut_full_url(url)
# print(yy)