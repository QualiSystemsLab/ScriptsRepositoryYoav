import requests

req_session = requests.session()

user = 'admin'
password = 'admin'
login_url = 'http://localhost:88/Account/Login?ReturnUrl=%2f&username={0}&password={1}'.format(user, password)

logans = req_session.post(
    url=login_url,

)
pass



