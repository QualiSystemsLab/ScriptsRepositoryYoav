import cloudshell.api.cloudshell_api as api7

# Destination details
d_username = 'admin'
d_password = 'admin'
d_server = 'qs.cisco.com'
d_domain = 'Global'

d_session = api7.CloudShellAPISession(d_server, d_username, d_password, d_domain)

reservations = d_session.GetScheduledReservations('01/01/1970 00:00', '07/21/2016 00:00')
a_reservations = []
Resource_list = []
Resource_list_names = []
todelete = []
tdr_fullpaths = []


for r in reservations.Reservations:
    if r.Status == 'Started':
        a_reservations.append(r)
for a_r in a_reservations:
    res_det = d_session.GetReservationDetails(a_r.Id)
    for t in res_det.ReservationDescription.Resources:
        if t.ResourceFamilyName == "SSP CI Regression VMs" or t.ResourceFamilyName == "Virtual Machine Instance":
            Resource_list.append(t)
b_resources = d_session.FindResources(resourceFamily="SSP CI Regression VMs")
c_resources = d_session.FindResources(resourceFamily="Virtual Machine Instance")
d_resources = b_resources.Resources + c_resources.Resources
for res in Resource_list:
    Resource_list_names.append(res.Name)
for d_r in d_resources:
    if d_r.Name not in Resource_list_names:
        todelete.append(d_r)
aux_reservation = d_session.CreateImmediateReservation("Maintenence res", owner="yekshtei", durationInMinutes=150)
# d_session.AddTopologyToReservation\
#     (reservationId=aux_reservation.Reservation.Id, topologyFullPath="Bangalore Topologies1\Maintenance_Topology")
for tdr in todelete:
    tdr_fullpaths.append(tdr.FullPath)
d_session.AddResourcesToReservation(reservationId=aux_reservation.Reservation.Id, resourcesFullPath=tdr_fullpaths)
for res_tdr in tdr_fullpaths:
    try:
        d_session.ExecuteResourceConnectedCommand(reservationId=aux_reservation.Reservation.Id,
                                              resourceFullPath=res_tdr,
                                              commandName='destroy_vm',
                                              commandTag='app_management'
                                              )
    except Exception as e:
        print(e.message)
pass