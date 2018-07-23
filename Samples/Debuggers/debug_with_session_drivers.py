import cloudshell.api.cloudshell_api as api
from github import Github

# First create a Github instance:
g = Github("yoavEkshtein", "Zoidberg19")

# Then play with your Github objects:
all_repos = g.get_user().get_repos()
for repo in all_repos:
    print repo.name

username = 'admin'
password = 'admin'
server = 'localhost'
domain = 'Global'


session = api.CloudShellAPISession(
    username=username,
    password=password,
    domain=domain,
    host=server
)

pass