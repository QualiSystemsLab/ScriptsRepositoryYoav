import xml.etree.cElementTree as ET
cust_config_path = 'C:\Program Files (x86)\QualiSystems\TestShell\Studio\customer.config'

class config_key():
    def __init__(self, key, value):
        self.key = key
        self.value = value

class config_file():
    def __init__(self, filename):
        self.keys = []
        self.xml_filename = filename
        self.tree = ET.ElementTree(file=self.xml_filename)
        self.get_all_config_keys()

    def get_all_config_keys(self):
        all_keys = self.tree.getroot().getchildren()
        for key in all_keys:
            self.keys.append(config_key(key.get('key'), key.get('value')))

    def set_config_value(self, akey, value):
        all_keys = self.tree.getroot().getchildren()
        found_key = 0
        for key in all_keys:
            my_key = config_key(key.get('key'), key.get('value'))
            if my_key.key == akey:
                key.set('key', akey)
                key.set('value', value)
                found_key = 1
        if found_key == 0:
            my_new_element = ET.Element('add')
            my_new_element.set('key', akey)
            my_new_element.set('value', value)
            self.tree.getroot().append(my_new_element)
        self.write_the_xml()

    def write_the_xml(self):
        self.tree.write(cust_config_path)

myconfigfile = config_file(cust_config_path)
myconfigfile.set_config_value('MaxOutputCharsToDisplay9999', '100000000')



pass