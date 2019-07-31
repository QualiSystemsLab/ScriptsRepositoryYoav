from cloudshell.api.cloudshell_api import CloudShellAPISession, DeployAppInput
from cloudshell.core.logger import qs_logger

def deploy_apps_in_reservation(api, reservation_details, reservation_id, logger):
    """
    :param CloudShellAPISession api:
    :param GetReservationDescriptionResponseInfo reservation_details:
    :param str reservation_id:
    :param logging.Logger logger:
    :return:
    """
    apps = reservation_details.ReservationDescription.Apps
    if not apps or (len(apps) == 1 and not apps[0].Name):
        logger.info("No apps found in sandbox {0}".format(reservation_id))
        api.WriteMessageToReservationOutput(reservationId=reservation_id,
                                            message='No apps to deploy')
        return None

    app_names = map(lambda x: x.Name, apps)
    app_inputs = map(lambda x: DeployAppInput(x.Name, "Name", x.Name), apps)

    api.WriteMessageToReservationOutput(reservationId=reservation_id,
                                        message='Apps deployment started')
    logger.info(
        "Deploying apps for sandbox {0}. App names: {1}".format(reservation_id, ", ".join(app_names)))

    res = api.DeployAppToCloudProviderBulk(reservation_id, app_names, app_inputs)

    return res

resid = 'f87392d2-c934-48e5-8a29-98370d180d3a'
username = 'yoav.e'
password = '1234'
server = '40.91.201.107'
domain = 'Global'


logger = qs_logger.get_qs_logger(
    log_group=resid,
    log_category='SkyBox_custom_Setup',
    log_file_prefix='Skybox_Setup'
)

session = CloudShellAPISession(
    username=username,
    password=password,
    domain=domain,
    host=server
)

res_desc = session.GetReservationDetails(resid)

qq = deploy_apps_in_reservation(session, res_desc, resid, logger)
pass