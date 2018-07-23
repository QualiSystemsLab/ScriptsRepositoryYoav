import cloudshell.api.cloudshell_api as api
import requests
import json
username = 'admin'
password = 'admin'
server = 'localhost'
domain = 'Global'

session = api.CloudShellAPISession(
    username=username,
    password=password,
    host=server,
    domain=domain
)
session.SetCustomShellAttribute(
    modelName='Cisco IOS Switch 2G',
    attributeName='Lab Location',
    defaultValue='Dojima 18F',
    restrictedValues=['Dojima 18F', 'Dojima 15F']
)
