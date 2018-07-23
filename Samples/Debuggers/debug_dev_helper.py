import cloudshell.helpers.scripts.cloudshell_dev_helpers as dev_help

resid = '8b137d58-b376-4204-825d-f073338a3979'
dev_help.attach_to_cloudshell_as(
    user='dom_admin',
    password='da',
    reservation_id=resid,
    domain='Global'
)
pass