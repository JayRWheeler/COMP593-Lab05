import requests

DAD_JOKES_API_URL = 'https://icanhazadadjoke.com/'
DAD_JOKES_SEARCH_URL = f'{DAD_JOKES_API_URL}/search'

def main():
    jokes_list = search_for_dad_jokes('cow')
    print(*jokes_list, sep= '\n')
    return

def search_for_dad_jokes(search_term):
    """Gets a list of dad jokes that contains a search term

    Args:
        search_term (str): Search Term

    Returns:
        Accept: 'application/json'
    """
   # Setup the header parameters
    header_params = {
        'Accept' : 'application/json'        
    }
    # Setup Query string parameters
    query_str_param = {
        'term': search_term
    }


        # Send the GET request to the Dad Jokes API
    print(f'Searching Dad Jokes API for "{search_term}" jokes...', end='')
    resp_msg = requests.get(DAD_JOKES_API_URL, headers=header_params, params=query_str_param)

    # Check whether the GET request was successful
    if resp_msg.ok:
        print('success')
        body_dict = resp_msg.json()
        jokes_list = [j['joke'] for j in body_dict['results']]
        return jokes_list 
    else:
        print('failed')
        print(f'Status code: {resp_msg.status_code} ({resp_msg.reason})')

    return

def get_random_dad_joke():
    """Gets a random Dad Joke

    Returns:
        str: Dad Joke
    """
    # Setup the header parameters
    header_params = {
        'Accept' : 'application/json'        

    }

        # Send the GET request to the Dad Jokes API
    print('Sending GET request to Dad Jokes API...', end='')
    resp_msg = requests.get(DAD_JOKES_API_URL, headers=header_params)

    # Check whether the GET request was successful
    if resp_msg.ok:
        print('success')
        joke_dict = resp_msg.json()
        return joke_dict['joke']    
    else:
        print('failed')
        print(f'Status code: {resp_msg.status_code} ({resp_msg.reason})')

    return
if __name__ == '__main__':
    main()