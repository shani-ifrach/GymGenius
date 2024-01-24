import requests


def get_nutirtion_info(nutirtion_desc):
    api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(nutirtion_desc)
    response = requests.get(api_url, headers={'X-Api-Key': 'Oc1imAZyLoyG4rQTWt7ycg==zwN3UgcMjrMF0jLi'})
    if response.status_code == requests.codes.ok:
        return response.text
    else:
        return "Error: Please try to check your spelling."
