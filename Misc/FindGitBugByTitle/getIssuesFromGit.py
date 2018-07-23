import requests
import jsonpickle

token = 'aaa379192aaec41f492ebf789d8dc81c2dbf1eb3'
headers = {
    'access_token': token,
    'Scope': 'repo',
    'token_type': 'bearer',
    }


def getIssues():
    jpo = []
    pageNumber = 1
    resultStr = ''
    while (pageNumber != -1):
        path = 'https://api.github.com/repos/QualiSystems/vCenterShell/issues?page=' + str(pageNumber)
        resp = requests.get(path, params=headers)
        jpoTemp = jsonpickle.decode(resp._content)
        if jpoTemp:
            for item in jpoTemp:
                jpo.append(item)
            pageNumber = pageNumber + 1
        else:
            pageNumber = -1
    return jpo


def getComments(commentsPath):
    commResp = requests.get(commentsPath, params=headers)
    jpoCommTemp = jsonpickle.decode(commResp._content)
    return jpoCommTemp
