import bs4
filename = "C:\Users\yoav.e\Desktop\Royal Thai Navy\Topologies\Royal Thai Navy.xml"

file = open(filename, "r")
file_content = file.read()
file.close()
bsoup = bs4.BeautifulSoup(file_content, "xml")
all_connectors = bsoup.find_all('Connector')
for con in all_connectors:
    con.attrs_aa = con('Attributes')
    print con.attrs_aa
    # if con.contents:
    #
    #     con.con_attrs = [tag for tag in con.contents[1].contents if tag != '\n']
    #     for attr in con.con_attrs:
    #         print attr.get('Name')
    #         print attr.get('Value')
    # else:
    #     con.contents=''


pass
