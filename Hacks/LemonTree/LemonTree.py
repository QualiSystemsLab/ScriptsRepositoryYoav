import tree_builder
import data_model_fw
import inspect
import sys
import yaml

class Resource():
    def __init__(self):
        self.Name = None
        self.Attributes = []
        self.Parent = []

    def __eq__(self, other):
        if isinstance(other, Resource):
            if self.Name == other.Name:
                return True
            else:
                return False
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, Resource):
            if self.Name != other.Name:
                return True
            else:
                return False
        else:
            return True





class LazyCallable(object):
    def __init__(self, name):
        self.n, self.f = name, None

    def caller(self, *a, **k):
        if self.f is None:
            modn, funcn = self.n.rsplit('.', 1)
            if modn not in sys.modules:
                __import__(modn)
            self.f = getattr(sys.modules[modn], funcn)
        return self.f(*a, **k)


def get_props(fn):
    LC = LazyCallable(fn)
    resource = LC.caller(name='a')
    level = Resource()
    variables = [i for i in dir(resource) if not callable(i)]
    temp_parent = resource.cloudshell_model_name.split('.')
    if temp_parent.__len__() > 1:
        level.Parent = [temp_parent[temp_parent.__len__() - 2]]
    variables = [i for i in variables if not i.__contains__('__')]
    variables = [i for i in variables if i[0] != '_']
    variables = [i for i in variables if i not in ['Resources', 'Name', 'address', 'attributes',
                                                   'add_sub_resource', 'create_autoload_details',
                                                   'cloudshell_model_name', 'create_from_context']]

    level.Name = fn.split('.')[-1]
    level.Attributes = variables
    return level

def deal_with_standard(levels):
    with open("C:\Program Files (x86)\QualiSystems\CloudShell\Server\ToscaStandard\cloudshell_firewall_standard_3_0_1.yaml", 'r') as stream:
        try:
            standard_yaml = (yaml.load(stream))
        except yaml.YAMLError as exc:
            print(exc)

    node_types = standard_yaml.get('node_types')
    for node,value in node_types.iteritems():
        if value.get('requirements'):
            reqs = value.get('requirements')
            for req in reqs:
                req_nodes = req.keys()
                for req_node in req_nodes:
                    actual_node = req.get(req_node)
                    child = actual_node.get('node').split('.')[-1]
                    parent = node.split('.')[-1]
                    for level in levels:
                        if level.Name == child:
                            level.Parent.append(parent)
        if value.get('derived_from') == 'cloudshell.nodes.Shell':
            root_node = node.split('.')[-1]
    return levels, root_node


classes = []
for name, obj in inspect.getmembers(data_model_fw):
    if inspect.isclass(obj):
        if obj.__name__ not in ['defaultdict', 'ResourceCommandContext', 'LegacyUtils', 'AutoLoadAttribute',
                                'AutoLoadDetails', 'AutoLoadResource']:
            classes.append(obj.__name__)


levels = []
for class_name in classes:
    levels.append(get_props('data_model_fw.{}'.format(class_name)))

levels, root_name_standard = deal_with_standard(levels)
root_name_dm = [level for level in levels if level.Parent == []][0].Name
# xq = LazyCallable('data_model_fw.{}'.format(root_name_dm))
for level in levels:
    if root_name_dm in level.Parent:
        level.Parent.remove(root_name_dm)
    if root_name_standard in level.Parent:
        level.Parent.remove(root_name_standard)
        if root_name_dm not in level.Parent:
            level.Parent.append(root_name_dm)
levels.sort(key=lambda x: x.Parent, reverse=False)
main = tree_builder.MainWindow(levels)
main.in_loop()

