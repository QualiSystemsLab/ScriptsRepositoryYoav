import drivercontext
import pymssql
import cloudshell.api.cloudshell_api as api


class poolitem:
    def __init__(self, ID , poolId, value, ReservationId, ownerId, IsoLevel):
        self.ID = ID
        self.poolId = poolId
        self.value = value
        self.ReservationId = ReservationId
        self.ownerId = ownerId
        self.IsoLevel = IsoLevel

class sqlinfodata:
    def __init__(self, server, user, password, database):
        self.server = server
        self.user = user
        self.password = password
        self.database = database

class GetVlanPoolTable:
    def __init__(self):
        pass

    # Initialize the driver session, this function is called every time a new instance of the driver is created
    # This is a good place to load and cache the driver configuration, initiate sessions etc.
    def initialize(self, context):
        """
        :type context: drivercontext.InitCommandContext
        """
        pass

    def _getpoolstatus(self, cursor, db):
        itemList = []
        query = r'SELECT * FROM [' + db + '].[dbo].[VLanItems]'
        cursor.execute(query)
        row = cursor.fetchone()
        msgboxtxt = '\n'
        while row:
            msgboxtxt += "ID = {0}  poolId = {1}  value = {2}  ReservationId = {3}  ownerId = {4}  IsoLevel = {5}\n" \
                .format(row[0], row[1], row[2], row[3], row[4], row[5])
            itemList.append(poolitem(row[0], row[1], row[2], row[3], row[4], row[5]))
            row = cursor.fetchone()
        return itemList

    # Destroy the driver session, this function is called every time a driver instance is destroyed
    # This is a good place to close any open sessions, finish writing to log files
    def _cleanup(self):
        pass

    # A command with multiple parameters
    def showPoolInfo(self, context):
        server = context.resource.address
        user = context.resource.attributes.get('User')
        db = context.resource.attributes.get('database')
        encryptedPassword = context.resource.attributes.get('Password')
        csssesion = api.CloudShellAPISession('localhost', 'admin', 'admin', 'Global')
        password = csssesion.DecryptPassword(encryptedPassword).Value
        sqlinfo = sqlinfodata(server, user, password, db)
        conn = pymssql.connect(sqlinfo.server, sqlinfo.user, sqlinfo.password)
        cursor = conn.cursor()
        inst = GetVlanPoolTable()
        items = inst._getpoolstatus(cursor, sqlinfo.database)
        result = inst._buildHtmlString(items)
        csssesion.UpdateReservationDescription(context.reservation.reservation_id ,result)

        return result

    def _buildHtmlString(self, items):
        htmlstring = '<table  border="1" style="width:150% ;color:#000000; text-align:center ;font-size:10px" >\n'
        htmlstring += '<tr>\n'
        htmlstring += '<td >ID</td>\n'
        htmlstring += '<td>pool\nID</td>\n'
        htmlstring += '<td>VLAN</td>\n'
        htmlstring += '<td>Reservation ID</td>\n'
        htmlstring += '<td>owner</td>\n'
        htmlstring += '<td>Iso</td>\n'
        htmlstring += '</tr>\n'
        idx = 1
        for entity in items:
            htmlstring += '<tr>\n'
            htmlstring += '<td >'+ str(idx) + '</td>\n'
            htmlstring += '<td>'+ str(entity.poolId) + '</td>\n'
            htmlstring += '<td>'+ str(entity.value) + '</td>\n'
            htmlstring += '<td >'+ str(entity.ReservationId) + '</td>\n'
            htmlstring += '<td >'+ str(entity.ownerId) + '</td>\n'
            htmlstring += '<td >'+ str(entity.IsoLevel) + '</td>\n'
            htmlstring += '</tr>\n'
            idx = idx + 1
        htmlstring += '</table>\n'
        return htmlstring

    # An advanced command that that supports cancellation
    # Adding the cancellation_token param will result in a "stop" button that will be available to the end user
    # in the web interface.
    def _example_cancellation(self, context, cancellation_token):
        """
        :type context: drivercontext.ResourceCommandContext
        :type cancellation_token: drivercontext.CancellationContext
        """
        return 'cancellation token: ' + cancellation_token.is_cancelled;
