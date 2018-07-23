__author__ = 'yoav.e'
import qualipy.api.cloudshell_api as api


cs_server_address = 'q1.cisco.com'
admin_username = 'admin'
cs_admin_password = 'admin'
cs_domain = 'Global'


api_session = api.CloudShellAPISession(host=cs_server_address, user=admin_username, password=cs_admin_password, domain=cs_domain)

fail = 0
error = []
for n in xrange(100):
    try:
        rese = api_session.GetScheduledReservations('06/10/2010 10:00', '08/31/2016 10:00')
    except Exception, e:
        fail += 1
        error.append(e)
print str(fail)
pass
