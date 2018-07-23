import pymssql
import json

# local DB debug
SQL_Server = 'localhost'
SQL_Username = 'Qualisystems\yoav.e'
SQL_Password = 'iuyT%678'
SQL_Database = 'emailer'
SQL_TableName = 'emails'

filepath = r"C:\temp\br_mail_report"
json_file = open(filepath, 'r')
json_obj = json.load(json_file)
json_file.close()
pass

conn = pymssql.connect(server=SQL_Server,
                       user=SQL_Username,
                       password=SQL_Password,
                       database=SQL_Database)
cursor = conn.cursor()

cursor.execute('DELETE FROM {}'.format(SQL_TableName))
for entry in json_obj:
    if entry.get('start') != '' and entry.get('end') != '':
        start = entry.get('start').split(' (UTC)')[0].strip().replace('\r\n', ' ')
        end = entry.get('end').split(' (UTC)')[0].strip().replace('\r\n', ' ')
        query = "INSERT INTO " + SQL_TableName + " (id, [start], [end]) VALUES ('{0}', '{1}', '{2}')" \
            .format(entry.get('id'),
                    start,
                    end
                    )
        try:
            cursor.execute(query)
        except Exception as e:
            print(e)
            continue
conn.commit()
conn.close()