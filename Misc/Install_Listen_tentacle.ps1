Param(
[string]$OCTOPUS_SERVER,
[string]$API_KEY,
[string]$ENVIRONMENT_NAME,
[string]$ROLE
)

$OctopusServerThumbprint = "283D0B9DDF77D1D287D948DCAC43C021D112566F"

Start-Transcript -Path "c:\tentacle-transcript.txt"

[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
Invoke-WebRequest -Uri http://octopusdeploy.com/downloads/latest/OctopusTentacle64 -OutFile c:\OctopusTentacle_x64.msi
cd c:\
msiexec /i OctopusTentacle_x64.msi /quiet | Out-Null

& 'C:\Program Files\Octopus Deploy\Tentacle\Tentacle.exe' create-instance --instance "Tentacle" --config "C:\Octopus\Tentacle\Tentacle.config" --console
& 'C:\Program Files\Octopus Deploy\Tentacle\Tentacle.exe' new-certificate --instance "Tentacle" --console
& 'C:\Program Files\Octopus Deploy\Tentacle\Tentacle.exe' configure --instance "Tentacle" --reset-trust --console
& 'C:\Program Files\Octopus Deploy\Tentacle\Tentacle.exe' configure --instance "Tentacle" --home "C:\Octopus" --console
& 'C:\Program Files\Octopus Deploy\Tentacle\Tentacle.exe' configure --instance "Tentacle" --app "C:\Octopus\Applications" --console
& 'C:\Program Files\Octopus Deploy\Tentacle\Tentacle.exe' configure --instance "Tentacle" --port "10933" --console
& 'C:\Program Files\Octopus Deploy\Tentacle\Tentacle.exe' configure --instance "Tentacle" --trust "$OctopusServerThumbprint" --console

$a= curl -UseBasicParsing 'https://api.ipify.org'

netsh advfirewall firewall add rule "name=Octopus Deploy Tentacle" dir=in action=allow protocol=TCP localport=10933
& 'C:\Program Files\Octopus Deploy\Tentacle\Tentacle.exe' register-with --instance "Tentacle" --server "$OCTOPUS_SERVER" --apiKey="$API_KEY" --role "$ROLE" --environment "$ENVIRONMENT_NAME" --publicHostName="$a" --comms-style TentaclePassive --console
& 'C:\Program Files\Octopus Deploy\Tentacle\Tentacle.exe' service --instance "Tentacle" --install --start --console

netsh advfirewall firewall add rule "name=Web Server" dir=in action=allow protocol=TCP localport=81
$enable_winrm_script_location = "https://raw.githubusercontent.com/QualiSystemsLab/SCA_POC_Pub/master/ExtensionScriptWithFileShare.ps1"
wget $enable_winrm_script_location -outfile "winrm.ps1"
Powershell.exe -ExecutionPolicy Bypass -File winrm.ps1

import-module servermanager
Add-WindowsFeature Web-Server -IncludeAllSubFeature

Stop-Transcript
