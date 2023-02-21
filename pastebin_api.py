import requests

DEV_KEY = 'YceKwsTzXDesRPoJvHfPOz8RFB_aXAqQ'
PASTE_API_URL = 'https://pastebin.com/api/api_post.php'

def main():
    url = post_new_paste("this is a title", "this\nis\the body", "1H", True)
    print(f'New paste URL: {url}')

def post_new_paste(title, body_text, expiration='10M', listed=False):
    """Posts a new public pate to Pastebin

    Args:
        title (str): Paste tite
        body_text (str): Paste body text
        expiration (str, optional): Expiration date of paste (N = never, 10M = minutes, 1H, 1D, 1W, 2W, 1M, 6M, 1Y). Defaults to False.
        listed (bool, optional): Whether paste is publicly listed (True) or not (False). Defaults to False.

    Returns:
        str: URL of the new paste, if successful. None if unsuccessful.
    """
    # Setup the parameters for the request message
    paste_params = {
        'api_dev_key' : DEV_KEY,
        'api_option' : 'paste',
        'api_paste_code' : body_text,
        'api_paste_name' : title,
        'api_paste_expire_date' : expiration,
        'api_paste_private' : 0 if listed else 1
    }    
    
    # Send the POST request to the PasteBin API
    print('Sending POST request to Pastebin API...', end='')
    resp_msg = requests.post(PASTE_API_URL, data=paste_params)

    # Check whether the POST request was successful
    if resp_msg.ok:
        print('success')
        return resp_msg.text    
    else:
        print('failed')
        print(f'Status code: {resp_msg.status_code} ({resp_msg.reason})')
        print (f'Reason: {resp_msg.text}')
if __name__ == '__main__':
    main()