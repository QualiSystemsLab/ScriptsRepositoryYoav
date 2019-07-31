import requests
import datetime

def attachFile(serverMachine, resid, file_path, user , password, domain, filename='genericfile'):

    # st = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S')
    data = {
        'username' : user,
        'password' : password,
        'domain' : domain
    }
    qq = 'Basic ' + requests.put(
        url='http://' + serverMachine + ':9000/API/Auth/Login',
        data=data
    ).text[1:-1]
    head = {
        'Authorization': qq,
    }
    dat_json ={
            "reservationId": resid,
            "saveFileAs": "{}.rdp".format(filename),
            "overwriteIfExists": "true",
    }

    with open(file_path, 'rb') as upload_file:
        xx = requests.post(
            url='http://' + serverMachine + ':9000/API/Package/AttachFileToReservation',
            headers=head,
            data=dat_json,
            files={'QualiPackage': upload_file}
        )
    return xx