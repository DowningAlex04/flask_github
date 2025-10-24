# TODO make requests to github API
import requests
import logging
def get_github_user(username):
    #404 not found
    #other errors
    #success 

    #return a tuple (data,error)
    # if work (data, none), if not (none, error)
    try:
        response = requests.get(f'https://api.github.com/users/{username}')
        if response.status_code == 404:
            return None, f'Username {username} not found'
        response.raise_for_status()
        response_json = response.json()
        user_info = extract_user_info(response_json)
        return user_info, None
    except Exception as e:
        logging.exeption(e)
        return None, 'Error'

def extract_user_info(json_response):
    return {
        'login': json_response.get('login'),
        'name': json_response.get('name'),
        'avatar_url': json_response.get('avatar_url'),
        'home_page': json_response.get('html_url'),
        'repos': json_response.get('public_repos')
    }