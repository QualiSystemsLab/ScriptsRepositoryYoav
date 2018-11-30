my_path = r'C:\ProgramData\QualiSystems\venv\decorator_test_1_4D96040DAC02F346B5AD4CF4AE41900B\lib\site-packages\retrying_qslogger'
for i, item in enumerate(my_path.split('\\')):
    if item == 'venv':
        entity_name = my_path.split('\\')[i+1]
print entity_name