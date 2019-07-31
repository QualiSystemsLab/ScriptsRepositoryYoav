import cloudshell.api.cloudshell_api as api
import cloudshell.helpers.scripts.cloudshell_scripts_helpers as SH
import cloudshell.helpers.scripts.cloudshell_dev_helpers as DH

username = 'admin'
password = 'admin'
server = 'localhost'
domain = 'Global'

session = api.CloudShellAPISession(
    username=username,
    password=password,
    domain=domain,
    host=server
)

resid = 'a1b04dc4-f037-402e-839c-6d4298d97b1d'

res_det = session.GetReservationDetails(resid)
resources = res_det.ReservationDescription.Resources
for resource in resources:
    session.ExecuteCommand(
        reservationId=resid,
        targetName=resource.Name,
        targetType='resource',
        commandName='refresh',
        commandInputs=[api.InputNameValue(Name='myinput', Value='myvalue')]
    )



pass