import getIssuesFromGit
import createHTMLtable
import stringhandle
import sys


class bug:
    def __init__(self, id , title,  content , labels):
        self.id = id
        self.title = title
        self.content = content
        self.labels = labels

filepath = r'c:\temp\blah.html'
resultStr = ''
idx = 0
bugList = []
arguments = []
jpo = getIssuesFromGit.getIssues()
arguments = sys.argv[1:]
if arguments.__len__() == 0:
    arguments[0] = ''
for issue in jpo:
    labels = issue.get('labels')
    for label in labels:
        if 'bug' == label.get('name'):
            title = stringhandle.stringhandle(issue.get('title'))
            bodyContent = stringhandle.stringhandle(issue.get('body'))
            if 'refresh' in title.lower():
                idx = idx + 1
            labeltot = ''
            for labeler in labels:
                labeltot += labeler.get('name') + '\n'
                resultStr += ("{0} ,".format(labeler.get('name')))
            if issue.get('comments') != 0:
                commentsPath = issue.get('comments_url')
                jpoCommTemp = getIssuesFromGit.getComments(commentsPath)
                for comment in jpoCommTemp:
                    resultStr += ("Comment : {0}\n".format(comment.get('body')))
            resultStr += ("\n\n\n")
            bugList.append(bug(issue.get("number"), title, bodyContent, labeltot))
htmlstr = createHTMLtable.buildHtmlString(bugList)
q = open(filepath, 'w+')
q.write(htmlstr)
q.close()
print(htmlstr)
pass