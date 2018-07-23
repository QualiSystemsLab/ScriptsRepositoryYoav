def stringhandle(st):
    if not (st):
        st = ''
    else:
        st = st.encode("utf-8")
    return st


def buildResultStr(issue, jpocommtemp):
    resultStr = ''
    resultStr += ("Issue number {0}\n".format(str(issue.get("number"))))
    resultStr += ("Labels :")
    for labeler in labels:
        labeltot += labeler.get('name') + '\n'
    resultStr += ("{0} ,".format(labeler.get('name')))
    resultStr = resultStr[:-1]
    resultStr += ("\n")
    resultStr += ("Title : {0}\n".format(stringhandle(issue.get("title"))))
    resultStr += ("{0}\n".format(stringhandle(issue.get("body"))))
    for comment in jpoCommTemp:
        resultStr += ("Comment : {0}\n".format(comment.get('body')))
    return resultStr