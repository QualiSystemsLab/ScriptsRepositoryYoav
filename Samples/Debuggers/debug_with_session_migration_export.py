import cloudshell.api.cloudshell_api as api
import xlwt
import os
import json

reservation_details = json.loads(os.environ["RESERVATIONCONTEXT"])
# resource_context = json.loads(os.environ['RESOURCECONTEXT'])
connectivity_details = json.loads(os.environ["QUALICONNECTIVITYCONTEXT"])
session = api.CloudShellAPISession(host=connectivity_details['serverAddress'],
                                   token_id=connectivity_details['adminAuthToken'],
                                   domain=reservation_details['domain'])
# excel_path = r'c:\temp\migration_excel.xls'
# my_model = 'Generic App Model'
excel_path = os.environ['Excel_path']
my_model = os.environ['Model']

book = xlwt.Workbook()
sheet = book.add_sheet('Resources', cell_overwrite_ok=True)

all_resources_of_model = session.FindResources(resourceModel=my_model)
for i, resource in enumerate(all_resources_of_model.Resources):
    col = 0
    sheet.write(0, col, 'ResourceName')
    sheet.write(0, col + 1, 'Address')
    row = i+1
    resource_details = session.GetResourceDetails(resource.Name)
    sheet.write(row, col, resource_details.Name)
    sheet.write(row, col + 1, resource_details.Address)
    for n, attr in enumerate(resource_details.ResourceAttributes):
        col = 2 + n
        sheet.write(0, col, '{0} [{1}]'.format(attr.Name, attr.Type))
        sheet.write(row, col, attr.Value)
book.save(excel_path)