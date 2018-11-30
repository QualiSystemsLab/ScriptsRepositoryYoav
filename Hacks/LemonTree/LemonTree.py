from ete2 import Tree, TreeStyle
import data_model_cp
import inspect
import sys

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
    variables = [i for i in dir(resource) if not callable(i)]
    variables = [i for i in variables if not i.__contains__('__')]
    variables = [i for i in variables if  i[0] != '_']
    variables = [i for i in variables if  i not in  ['Resources', 'Name', 'address', 'attributes',
                                                     'add_sub_resource', 'create_autoload_details',
                                                     'cloudshell_model_name', 'create_from_context']]
    level = ','.join(variables)
    return level
classes = []
for name, obj in inspect.getmembers(data_model_cp):
    if inspect.isclass(obj):
        if obj.__name__ not in ['defaultdict', 'ResourceCommandContext', 'LegacyUtils', 'AutoLoadAttribute',
                                'AutoLoadDetails', 'AutoLoadResource']:
            classes.append(obj.__name__)

levels = []
for class_name in classes:
    levels.append(get_props('data_model_cp.{}'.format(class_name)))

tree_struct = "("

def pop_tree_struct(levels, tree_struct):
    '''
    :param list levels:
    :param tree_struct:
    :return:
    '''
    if levels.__len__() > 0:
        tree_struct += "({level}),".format(level=levels[0])
        levels.remove(levels[0])
        levels, tree_struct = pop_tree_struct(levels, tree_struct)
    else:
        return levels, tree_struct

q, tree_struct = pop_tree_struct(levels, tree_struct)
tree_struct = tree_struct[:-1]
tree_struct += ");"


from ete2 import Tree, TreeStyle
t = Tree(tree_struct)
# t = Tree( '(A:1,(B:1,(C:1,D:1):0.5):0.5);')

ts = TreeStyle()
ts.show_leaf_name = True
ts.show_branch_length = False
ts.show_branch_support = True
ts.show_scale = False
t.show(tree_style=ts)
