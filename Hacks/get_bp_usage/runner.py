from get_af_sandbox_api import Rest_api_client
import json


instance = Rest_api_client(
    username='admin',
    password='admin',
    # host='qs-il-adams'
)
sandboxes = json.loads(instance.get_all_sandboxes().content)
sorted_sandboxes = []
for sandbox in sandboxes:
    bp = sandbox.get('blueprint')
    if bp.get('id') not in sorted_sandboxes:
        sorted_sandboxes.append(bp.get('id'))
    # bp_data = sorted_sandboxes.get(bp.get('name')) or []
    # bp_data.append({
    #     'id': sandbox.get('id')
    # })
    # sorted_sandboxes.update({
    #     bp.get('name') : bp_data
    # })
for bpa in sorted_sandboxes:
    qq = instance.get_sandboxes_from_blueprint(
        sandboxes, bpa
    )
pass
