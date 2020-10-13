from django.shortcuts import render
import requests


import json
import requests
import sys
import urllib3
from requests.auth import HTTPBasicAuth
from prettytable import PrettyTable



def button(request):
    return render(request,'home.html')
def output(request):

    """
    # disable warnings from SSL/TLS certificates
    requests.packages.urllib3.disable_warnings()

    # use the IP address or hostname of your Cat9300
    HOST = '10.4.1.52'

    # use your user credentials to access the Cat9300
    USER = 'kaval'
    PASS = 'KSs200684'


     # url string to issue GET request
    url = "https://{h}/restconf/data/ietf-interfaces:interfaces".format(h=HOST)

    # RESTCONF media types for REST API headers
    headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}
    # this statement performs a GET on the specified url
    response = requests.get(url, auth=(USER, PASS),
                            headers=headers, verify=False)

    # print the json that is returned
    print(response.text)
    data=response.text
    return render(request,'home.html',{'data':data})
    """


    data=requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
    print(data.text)
    data=data.text
    return render(request,'home.html',{'data':data})

