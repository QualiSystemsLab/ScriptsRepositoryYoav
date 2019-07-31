class data():
    def __init__(self):
        self.dataValue = 'AAA'
        self.dataKey = 'YYYY'

    def showmethevalue(self):
        q = self.dataKey
        return self.dataValue


class GetSandboxDataInfo():
    def __init__(self, xml_object, find_prefix):
        self.SandboxDataKeyValues = {'list': SandboxDataKeyValueInfo}
        """:type : list[SandboxDataKeyValueInfo]"""

class SandboxDataKeyValueInfo():
    def __init__(self, xml_object, find_prefix):
        self.Value = str
        """:type : str"""
        self.Key = str
        """:type : str"""

    def showmethevalue(self):
        q = self.dataKey
        return self.dataValue



qq = GetSandboxDataInfo()
ww = [attr.Value for attr in qq.SandboxDataKeyValues if attr.Key == 'adam']


mydata = data()
mydata.showmethevalue()
print mydata.__dict__['dataKey']





