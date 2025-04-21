import requests

def make_request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass
    
    
target_input= "google.com"

with open("SubdomainLister\subdomainlist.txt","r") as file:
    for word in file:
        word=word.strip() #for cleaning
        url="http://"+ word + "." + target_input
        response = make_request(url)
        if response:
            print(f"Found subdomain ---> {url}")
            
        else:
            print(response)