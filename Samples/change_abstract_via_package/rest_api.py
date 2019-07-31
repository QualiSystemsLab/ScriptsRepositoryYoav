import requests
import zipfile
import StringIO
import json
import time

class api_handler():
    def __init__(self):
        self.rest_session = requests.session()
        login_data = {
            'username': 'admin',
            'password': 'admin',
            'domain': 'Global'
        }
        self.base_url = 'http://localhost:9000/API'
        login_url = '/Auth/Login'
        login = self.rest_session.put(self.base_url + login_url, data=login_data).text[1:-1]
        self.rest_session.headers = {
            'Authorization': 'Basic {0}'.format(login)
        }

    def export_package(self, blueprint_name, output_file_name):
        export_url = '/Package/ExportPackage'
        input_data = {
            'TopologyNames': '{}'.format(blueprint_name)
        }

        export_file = self.rest_session.post(
            url=self.base_url + export_url,
            data=input_data,
            stream=True
        )
        zip_file = zipfile.ZipFile(StringIO.StringIO(export_file.content))
        zip_file.extractall(path=output_file_name)


    def import_package(self, file_name):
        import_url = '/Package/ImportPackage'
        input_data = {
            'Content-Type': 'application/x-zip-compressed',
            'Content-Disposition': 'form-data',
            'name': 'QualiPackage',
            'filename': '{}'.format(file_name)
        }
        response = self.rest_session.post(
            url=self.base_url + import_url,
            data=input_data
        )

        return response


