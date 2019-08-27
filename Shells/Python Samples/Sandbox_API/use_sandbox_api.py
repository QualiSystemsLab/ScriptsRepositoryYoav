from Sandbox_api_class import sandbox_api

rest_handler = sandbox_api(
    server='localhost',
    username='admin',
    password='admin',
    domain='global'
)

blueprint_initial_id = '510f8806-a333-4967-85fc-05bdb94ae062'
# running script

my_blueprint = [bp for bp in rest_handler.get_blueprints() if bp['name'] == 'Python Sample'][0]
blueprint_id = my_blueprint['id']
sandbox_id = rest_handler.reserve(blueprint_id)
rest_handler.run_blueprint_command(sandbox_id, 'power_off_all_apps')
rest_handler.end_sandbox(sandbox_id)
pass
