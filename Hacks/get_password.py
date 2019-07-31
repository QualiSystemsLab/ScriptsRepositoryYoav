from cloudshell.api.cloudshell_api import CloudShellAPISession

session = CloudShellAPISession(
    username='admin',
    password='civ1C2018',
    host='172.30.180.86',
    domain='Global'
)
res_det = session.GetResourceDetails(
    resourceFullPath='Ansible-dev-server-vm'
)


pvt_key = '''-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA7Zrx6SISBrXMZpz8WM0yde/QJ+0RNeV5YAk65IH1FjqrLpOj
TP1ZrIpB5nSytUdNKav/JgfXPTOF/Ra2Av5GrOgfHUYy1fBjXa/Ieg3BsQ6J9k/T
uamWD0J9o3ljSB61dW9iV3H5bM6bYrDwUiaJuTcGOBxEabkFBHmjkDnDUU0J7G9w
AlzLpzF9w6sW75asa7JXJAvLxx206XnpPQ39liodC9tHnao+xaTuUf+NbrtZSFYf
t5VFvzgs8UuTF+QQ13ei1GA7aQpfwpcv67B9iHI7edAqb/ypSAdoZKvp7LWhuZnD
dSomLfRNp/89qnmIgs+pTr7wA9UUfJLdsTDtnQIDAQABAoIBAQDIB8qirxkn5wM2
W/EhvVY+7W57Plxf2FlPXVXkK/guB6Q3aPlwhlVpKVgDcLlGXcl7TJ5X4P/2ORsT
D3yZloHfbOdM2N1ROLgeli8bedtXeNryrw+a3UdEf4CQEFBh1eCEBgpvfbczP9iW
xEj9kA4gDE/DCyEZNDciJllpwQdKuAZf9HMFwm+IoafuXo/L8++THf3NqnMil4a0
nwcf4sCD609ij7GlxGgLMJR04l6Deb5BfZm91QUJeQY+vhYdaNI10FtIs4Y2jtwf
jwEctWSe7eHYUwiE7cORIAlwV4PqCbbQjSiOyikQaZ6cxNoQWGUV740WJIRfX1bd
WkHwRJ+BAoGBAPboVfCfp3gO8JPUP5ut5KLZx6GfinKBJrYW7YEc6nPXJlryp2K8
g0QW+se3JkCLJyimUCKRRvPCxQqiKdDe4LS00n2zOVSsq7uehNLBMdVTvw9Q/1oa
GjKk39l3DsvZpnO7wfOgderChXlxWVopUj/nroIN0VNY5uX/HdBfhkWhAoGBAPZa
6fTu4Qwk0es/i3yxT4ruezFeZpwPgK4PDM38na2jQAGs91ncG78tQheezYlGJhb+
/9gwvzcraQ/e+5PCtWa2IyDm+PYonDEMtFBLzXhAHwGJMCIPIiKai2vd8LDqw1cg
zh+Eg1ik4IH0Yfl5SC76Xb3gi1g/W+8TyVN7Xi59AoGATeCEUswYp16W9RmqInFb
vx3PwKOwqGMiEabzrJixPm5rE56buyHYiV5yJRIYh50ccc7bUbve1D3npm31oILb
/0NVbP5do95+oEPkgxEapb2vcqZKlGHNR5IHZPEPgq6YuMJM74n6B1zpep+M3kpQ
PgXWXgD7uD0/PuYTwkiO8mECgYBi9M/ncBD8BMpBmcvY8YxG/VaE1SuYYm3I/Qii
sWdQ+TNbuPO+p7iJiY9z13kuO/xO3m08lRAqBAj2tBYQG3UsZdske0Lj9hoPZdAE
NP66397UihvIgpWumq+IS6VEG3kNxYKmjF8KO2hnKxgz0rDZFf6Tp9+xOfoexa7o
FrUVLQKBgQCLjEJ1iwGEAqqB9AXNcYOyDpWekj+24/6IkrjLZeFuk416d0kGMeE/
8OJB0iITna1tJUEYbzXLB4biiNVxx8djwK9XIaNr3CjarrM1h3YWtvZmsvzIHSJo
+OPNKKHu0xOOTVKrad2XjyNZraU3VvogPxISyqBvxp1lR0yzHdjH4g==
-----END RSA PRIVATE KEY-----'''
session.SetAttributeValue(
    resourceFullPath='Ansible-dev-server-vm',
    attributeName='{}.Password'.format(res_det.ResourceModelName),
    attributeValue=pvt_key
)

password = [attr for attr in res_det.ResourceAttributes if attr.Name == '{}.Password'.format(res_det.ResourceModelName)][0].Value
dec_pass = session.DecryptPassword(password).Value
print dec_pass
pass

session.Service(
)