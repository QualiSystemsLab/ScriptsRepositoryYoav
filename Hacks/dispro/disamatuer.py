class record():
    def __init__(self, now , q_since, ex_id):
        self.now = now
        self.q_since = q_since
        self.ex_id = ex_id


all_records = []
with open(r"C:\temp\DisPro.txt", "r") as f:
    raw_log = f.read().split('\n2018')
mylog = filter(lambda x:x.__contains__("[Instant Job Queue Handler]"), raw_log)
mylog = filter(lambda x:x.__contains__("pending"), mylog)
mylog = ['2018{}'.format(l) for l in mylog]
for item in mylog:
    now = item.split(',')[0]
    ex_id = item.split('Execution Id')[1].split('is')[0].strip()
    q_since = item.split('queued since')[1].split('.')[0].strip()
    p = 0
    for rec in all_records:
        if ex_id == rec.ex_id:
            p = 1
            rec.now.append(now)
    if p == 0:
        all_records.append(record(now, q_since, ex_id))

for rec in all_records:
    print 'Execution {0} queued since {1} timestamp: {2}'.format(
        rec.ex_id,rec.q_since,rec.now
    )
pass