import outlook_main.outlook as outlook
import json
class sandbox():
    def __init__(self, id):
        self.id = id
        self.start = ''
        self.end = ''

mail = outlook.Outlook()
mail.login(
    username='yoav.e@qualisystems.com',
    password='iuyT%678'
)
folder = 'inbox/Customers/Vodafone/Enterprise - Bracknell/LS'
mail.select(folder)
ids = mail.allIds()
sandboxes = []
full_sandboxes = []
for i,mid in enumerate(ids):
    mail.getEmail(mid)
    subject = mail.mailsubject()
    message = mail.mailbody()
    try:
        id = message.split('ID')[1].split('<td>')[1].split('</td>')[0]
        sandboxes.append(sandbox(id))
        if subject.__contains__('started'):
            sbx = [sbox for sbox in sandboxes if sbox.id == id][0]
            sandboxes.remove(sbx)
            sbx.start = subject.split('at ')[1]
            sandboxes.append(sbx)
        elif subject.__contains__('ended'):
            sbx = [sbox for sbox in sandboxes if sbox.id == id][0]
            sandboxes.remove(sbx)
            sbx.end = subject.split('at ')[1]
            sandboxes.append(sbx)
    except:
        pass
    if i % 10 == 0:
        print i
for sb in sandboxes:
    if sb.start != '' and sb.end != '':
        full_sandboxes.append(sb)

json_str = json.dumps([ob.__dict__ for ob in sandboxes])
text_file = open(r"c:\temp\br_mail_report", "w")
text_file.write(json_str)
text_file.close()
pass