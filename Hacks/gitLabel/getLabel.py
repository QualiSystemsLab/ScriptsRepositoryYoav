import requests
import jsonpickle
import sys


jpo = []
pageNumber = 1
resultStr = ''
token = 'aaa379192aaec41f492ebf789d8dc81c2dbf1eb3'
headers = {
    'access_token': token,
    'Scope': 'repo',
    'token_type': 'bearer',
}
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
if sys.argv.__len__() == 1:
    userinput = "VM Networking"
else:
    userinput = sys.argv[1]
for issue in jpo:
    labels = issue.get('labels')
    for label in labels:
        if userinput == label.get('name'):
            resultStr += ("Issue number {0}\n".format(str(issue.get("number"))))
            resultStr += ("Labels :")
            for labeler in labels:
                resultStr += ("{0} ,".format(labeler.get('name')))
            resultStr = resultStr[:-1]
            resultStr += ("\n")
            resultStr += ("Title : {0}\n".format(issue.get('title')))
            resultStr += ("{0}\n".format(issue.get('body')))
            if issue.get('comments') != 0:
                commentsPath = issue.get('comments_url')
                commResp = requests.get(commentsPath, params=headers)
                jpoCommTemp = jsonpickle.decode(commResp._content)
                for comment in jpoCommTemp:
                    resultStr += ("Comment : {0}\n".format(comment.get('body')))
            resultStr += ("\n\n\n")
print(resultStr)
pass

