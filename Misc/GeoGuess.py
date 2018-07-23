metadatafile = "C:\Users\yoav.e\Downloads\GeoPhotoService (6).GetMetadata"
f = open(metadatafile)
mdf = f.read()
f.close
lat = mdf.split('(')[1].split(')')[0].split('],[')[15].split(',')[2]
longt = mdf.split('(')[1].split(')')[0].split('],[')[15].split(',')[3]
coord = '{0} {1}'.format(lat, longt)
print coord
