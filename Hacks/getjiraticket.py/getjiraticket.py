from jira import JIRA

jira = JIRA(server='https://jira.sgg.cisco.com', basic_auth=('yekshtei', 'Zoidberg19'))
cc = jira.issue('QUALI-702')
description = cc.raw['fields']['description']
print (description)
pass

