import qualipy.api.cloudshell_api as api6
import cloudshell.api.cloudshell_api as api7
import drivercontext

ss6 = api6.CloudShellAPISession('q1.cisco.com', 'admin', 'admin', 'Global')
ss7 = api7.CloudShellAPISession('qs.cisco.com', 'admin', 'admin', 'Global')
gtd = ss6.GetTopologyDetails("RTP Topologies/Yoav RTP Migration")

ss7.CreateImmediateReservation()

connected_resources = []
items_to_remove = []
l2switches = []
for someres in gtd.Resources:
    if someres.ResourceFamilyName == 'Switch':
        l2switches.append(someres)
#     if someres.Connections:
#         connected_resources.append(someres.Connections[0].FullPath)
# connected_resources = sorted(connected_resources)
for sw in l2switches:
    # rdet = ss6.GetResourceDetails(sw.Name)
    if sw.ResourceModelName == 'Cisco NXOS Switch':
        ss7.UpdateResourceDriver(sw.Name, 'Generic Cisco NXOS Driver Version2')
    if sw.ResourceModelName == 'Cisco IOS Switch':
        ss7.UpdateResourceDriver(sw.Name, 'Generic Cisco IOS Driver Version2')
    ss7.AutoLoad(sw.Name)
    # try:
    #     ss7.CreateResource(sw.ResourceFamilyName, sw.ResourceModelName, sw.Name, sw.Address, sw.FolderFullPath, '', '')
    # except:
    #     pass
    # ss7.AddResourcesToDomain('RTP', [sw.Name])
    # for attr in rdet.ResourceAttributes:
    #     try:
    #         ss7.SetAttributeValue(resourceFullPath=sw.Name, attributeName=attr.Name, attributeValue=attr.Value)
    #     except Exception as e:
    #         print(e.message)
# num_subs = 0
# for idx, con_res in enumerate(connected_resources):
#     if idx + 1 < connected_resources.__len__():
#         f_val = connected_resources[idx].split('/')[-4]
#         s_val = connected_resources[idx + 1].split('/')[-4]
#         if f_val == s_val:
#             items_to_remove.append(connected_resources[idx])
# for item in items_to_remove:
#     connected_resources.remove(item)
pass

