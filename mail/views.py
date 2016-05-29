import requests
from django.shortcuts import render
from bs4 import BeautifulSoup

def login_page(request):
    '''Render to login Page'''
    return render(request, 'mail/login.html')

def get_google_login(request):

    if request.method == "GET":
        gcode = request.GET['code']
        client_id = '977890289014-oug5ohgk1q6qod8gp1hbllm4c4qo2cjh.apps.googleusercontent.com'  #Google cient_id
        redirect_uri = 'http://localhost:8000/mail/get_google_login/'
        grant_type = 'authorization_code'
        client_secret = 'YH39lQckLYY9zMOotVe_I7bW'
        result = requests.post("https://accounts.google.com/o/oauth2/token",    #Post method token request g+
                          data={                                                #Parameters
                              'code': gcode,
                              'client_id': client_id,
                              'client_secret': client_secret,
                              'redirect_uri': redirect_uri,
                              'grant_type':grant_type})
        dct = result.json()
        access_token = dct['access_token']
        headers = {'Authorization': 'Bearer %s' % access_token}
        response = requests.get("https://www.google.com/m8/feeds/contacts/default/full", headers = headers)      #get contact request
        soup = BeautifulSoup(response.text)                         #Parse xml response
        dic = soup.find_all('entry')
        data = []
        for i in dic:
            data.append(i.find('title').text)
        return render(request, 'mail/contacts.html', {'data': data})
