import requests
import json
import os
import zipfile


class getallshellfoundrytemplates():
    def __init__(self, input_data):
        self.config_data = input_data
        self.rest_session = requests.session()
        self.rest_session.params = {
            'access_token': self.config_data.get('configuration').get('token'),
            'Scope': 'repo',
            'token_type': 'bearer',
        }
        self.base_path = 'https://api.github.com/users/Qualisystems/repos'

    def download_file(self, url, local_prefix):
        local_filename = local_prefix + '\\' + url.split('/')[-3] + '.zip'
        r = self.rest_session.get(url, stream=True)
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        return local_filename

    def execute(self):
        # original call
        resp = self.rest_session.get(self.base_path)
        repos = json.loads(resp.text)
        # pagination
        while resp.links.get('next'):
            next_page_url = resp.links.get('next').get('url')
            resp = self.rest_session.get(next_page_url)
            new_repos = json.loads(resp.text)
            for repo in new_repos:
                repos.append(repo)
        template_repos = [repo for repo in repos if (repo.get('name').__contains__('tosca') and repo.get('name').__contains__('shellfoundry') or repo.get('name').__contains__('shell-L1-template') )]
        for temp in template_repos:
            zip_url = temp.get('url') + '/zipball/main'
            self.verify_dir(self.config_data.get('configuration').get('local_folder'))
            self.download_file(
                url=zip_url,
                local_prefix=self.config_data.get('configuration').get('local_folder')
            )
            print temp.get('name')
        all_zip_files = self.get_folder_content(self.config_data.get('configuration').get('local_folder'))
        for zipfile in all_zip_files:
            self.extract(path_to_zip_file='{0}/{1}'.format(self.config_data.get('configuration').get('local_folder'), zipfile),
                         directory_to_extract_to='{0}/{1}'.format(self.config_data.get('configuration').get('local_folder'), 'Extracted'))

    def verify_dir(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    def extract(self, path_to_zip_file, directory_to_extract_to):
        zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
        zip_ref.extractall(directory_to_extract_to)
        zip_ref.close()

    def get_folder_content(self, path):
        return os.listdir(path)