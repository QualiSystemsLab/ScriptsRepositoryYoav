def buildHtmlString(items):
    htmlstring = '<table  border="1" style="width:150% ;color:#000000; text-align:center ;font-size:14px" >\n'
    htmlstring += '<tr>\n'
    htmlstring += '<td >ID</td>\n'
    htmlstring += '<td>Title</td>\n'
    htmlstring += '<td>Content</td>\n'
    htmlstring += '<td>Labels</td>\n'
    htmlstring += '</tr>\n'
    idx = 1
    for entity in items:
        htmlstring += '<tr>\n'
        htmlstring += '<td>'+ str(entity.id) + '</td>\n'
        htmlstring += '<td>'+ str(entity.title) + '</td>\n'
        htmlstring += '<td >'+ str(entity.content) + '</td>\n'
        htmlstring += '<td >'+ str(entity.labels) + '</td>\n'
        htmlstring += '</tr>\n'
    htmlstring += '</table>\n'
    return htmlstring
