# Farm Beats Hack

![hackathon design](/images/hackathon.jpg)


## Install Farm Beats

https://docs.microsoft.com/en-us/azure/industry/agriculture/install-azure-farmbeats#install

## Partner Integration

### Enable device integration with FarmBeats

This step creates a client that has access to your Azure FarmBeats instance as the device partner. Generating your Farm Beats partner will provide your with the following:

- Tenant ID
- Client ID
- Client secret
- EventHub connection string

#### Azure Cloud Shell Access

Grant Azure Cloud Shell Access to Farm Beats API deployment (https://<datahub>.azurewebsites.net)

1. Download the [zip file](https://aka.ms/farmbeatspartnerscriptv2), and extract it to your local drive. There will be one file inside the zip file.

2. Sign in to [Azure Portal](https://portal.azure.com/) and go to Azure Active Directory -> App Registrations

3. Click on the App Registration that was created as part of your FarmBeats deployment. It will have the same name as your FarmBeats Datahub.

4. Click on “Expose an API” -> Click “Add a client application” and enter 04b07795-8ddb-461a-bbee-02f9e1bf7b46 and check "Authorize Scope". This will give access to the Azure CLI (Cloud Shell) to perform the below steps.

#### Generate Partner


1. Open Cloud Shell. This option is available on the toolbar in the upper-right corner of the Azure portal.

![cloud shell bar](/images/navigation-bar-1.png)

2. Make sure the environment is set to PowerShell. By default, it's set to Bash.

![cloud shell bar](/images/power-shell-new-1.png)

3. Upload the file from step 1 in your Cloud Shell instance.

![cloud shell bar](/images/power-shell-two-1.png)

4. Go to the directory where the file was uploaded. By default, files get uploaded to the home directory under the username.
Run the following script. The script asks for the Tenant ID which can be obtained from Azure Active Directory -> Overview page.

```bash
./generatePartnerCredentials.ps1
```

5. Follow the onscreen instructions to capture the values for API Endpoint, Tenant ID, Client ID, Client Secret, and EventHub Connection String.


_Please review the steps on the [Farm Beats Documentation](https://docs.microsoft.com/en-us/azure/industry/agriculture/get-sensor-data-from-sensor-partner#enable-device-integration-with-farmbeats) for additional guiidance._
 

### Create Device and Sensor Models for Partner Integration

Run the following scrip; Fill in:
- Farm Beats Data Hub
- Farm Beats Client ID
- Farm Beats Tenent ID
- Farm Beats Client Secret

```bash

python curl -L https://raw.githubusercontent.com/Jscholtes128/Azure-FarmBeatsLabModule/master/Set-Up/sensorregistration.py | python --endpoint https://<Farm Beats Data Hub>.azurewebsites.net --client_id <Farm Beats Client ID> --tenent_id <Farm Beats Tenent ID> --client_secret <Farm Beats Client Secret>

```

__Capture the Json as this will be used in the device twin__


## Create Azure IoT Resources

## Create Azure IoT Resources

Run the bash scrip from the Azure Cloud Shell

```bash
curl -L https://raw.githubusercontent.com/Jscholtes128/Azure-FarmBeatsLabModule/master/Set-Up/resource_set_up.sh | bash

```

Run the provided bash script on your Raspberry Pi device to install IoT Edge Runtime and configure 

### Create Azure IoT Route 

