def createHTMLtablehtml_Table(headlines, data, title=''):
    html_Table = '<p>{0}</p>'.format(title)
    html_Table += '<table border="1">'
    html_Table += '<tr>'
    for headline in headlines:
        html_Table += '<td style=color:black;text-align:center;>{item}</td>'.format(item=headline)
    html_Table += '</tr>'
    for item in data:
        html_Table += '<tr>'
        for record in item:
            html_Table += '<td style=color:black;text-align:center;>{0}</td>'.format(str(record))
        html_Table += '</tr>'
    html_Table += '</tr></table>'
    return html_Table

