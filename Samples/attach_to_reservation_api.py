import requests
import json
import time
import datetime
login_data = {
    'username': 'admin',
    'password': 'admin',
    'domain': 'Global'
}

def attachFile(serverMachine, resid, file_path, user , password, domain):
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S')
    data = {
        'username' : user,
        'password' : password,
        'domain' : domain
    }
    qq = 'Basic ' + requests.put(
        url=serverMachine + ':9000/API/Auth/Login',
        data=data
    ).text[1:-1]
    head = {
        'Authorization': qq,
    }
    dat_json ={
            "reservationId": resid,
            "saveFileAs": "logs_" + st,
            "overwriteIfExists": "true",
    }

    with open(file_path, 'rb') as upload_file:
        xx = requests.post(
            url=serverMachine + ':9000/API/Package/AttachFileToReservation',
            headers=head,
            data=dat_json,
            files={'QualiPackage': upload_file}
        )
    return xx

attachFile(
    serverMachine='http://localhost',
    resid='abd1b71d-20f5-4879-bb0b-6d755b4e107f',
    file_path='https://github.com/NationOfJoe/jsonTemplates/blob/master/firewall_policies/{env_name}.xlsx?raw=true'.format(env_name='Skybox_vLab_1.1'),
    user='admin',
    password='admin',
    domain='Global'
)