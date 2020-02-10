# Farm Beats Raspberry Pi Lab Hackathon

![hackathon design](/images/hackathon.jpg)

## Prerequisites

- Azure subscription. If you don't have one, create a [free account](https://azure.microsoft.com/en-us/free/) before you begin.
- Farm Beats [Student Lab Kit](https://github.com/farmbeatslabs/studentkit/blob/master/Indoor-m1/Indoor_M1_Hardware_List.md) (_todo: hardware build options_)
- Flash SD with [Raspbian Buster](https://www.raspberrypi.org/downloads/raspbian/) for Raspberry Pi

## Step 1 - Install Farm Beats (40 minutes)

https://docs.microsoft.com/en-us/azure/industry/agriculture/install-azure-farmbeats#install

## Step 2 - Device Integrator (x Minutes)

### 2.1 - Enable device integration with FarmBeats

This step creates a client that has access to your Azure FarmBeats instance as the device partner. Generating your Farm Beats partner will provide your with the following:

- Tenant ID
- Client ID
- Client secret
- EventHub connection string

#### 2.1.1 Azure Cloud Shell Access

Grant Azure Cloud Shell Access to Farm Beats API deployment (https://<datahub>.azurewebsites.net)

1. Download the [zip file](https://aka.ms/farmbeatspartnerscriptv2), and extract it to your local drive. There will be one file inside the zip file.

2. Sign in to [Azure Portal](https://portal.azure.com/) and go to Azure Active Directory -> App Registrations

3. Click on the App Registration that was created as part of your FarmBeats deployment. It will have the same name as your FarmBeats Datahub.

4. Click on “Expose an API” -> Click “Add a client application” and enter 04b07795-8ddb-461a-bbee-02f9e1bf7b46 and check "Authorize Scope". This will give access to the Azure CLI (Cloud Shell) to perform the below steps.

#### 2.1.2 Generate Partner

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
 
### 2.2 - Create Device and Sensor Models for Partner Integration 

Run the following scrip; Fill in:
- Farm Beats Data Hub
- Farm Beats Client ID
- Farm Beats Tenent ID
- Farm Beats Client Secret

```bash

ENDPOINT=[Farm Beats Data Hub Web URL]
CLIENT_ID=[Farm Beats Client ID]
CLIENT_SECRET=[Farm Beats Client Secret]
TENANT_ID=[Tenent ID]

curl -L https://raw.githubusercontent.com/Jscholtes128/Azure-FarmBeatsLabModule/master/Set-Up/registerdevice.sh | bash -s $ENDPOINT $CLIENT_ID $CLIENT_SECRET $TENANT_ID

```

__Copy__ the generated JSON as we will use in Step 3.2 Add Module Twins

```json
      Interval": 60,
     "DeviceID": "[generated]",
     "PressureSensorID": "[generated]",
     "TempSensorID": "[generated]",
```

## Step 3 - Azure IoT Resource and Device (x Minutes)

### 3.1 - Create Azure Resources

Run the bash scrip from the Azure Cloud Shell to create:

- Azure IoT Hub
- Azure IoT Hub Edge Device
- Azure IoT Hub Edge Device Farm Beats Module
- Azure Blob Store with IoT Edge Runtime install script for Raspberry Pi (Tiny Url will be provided to SAS URL)

```bash
curl -L https://raw.githubusercontent.com/Jscholtes128/Azure-FarmBeatsLabModule/master/Set-Up/resource_set_up.sh | bash

```

The generated URL (https://j.mp/2#####) will be used in Step 4 to install and configure Azure IoT Runtime on Raspberry Pi.

### 3.3 - Install Azure IoT Runtime

#### 3.3.1 - Configure Raspberry Pi Inputs

#### 3.3.2 - Install with Tiny URL

### 3.4 - Update Device Twins to Module

### 3.5 - Create Azure IoT Route

## Step 4 - Farm Beats UI

### 4.1 Create Farm and Add Sensor (x Minutes)

 1. Create a [Farm](https://docs.microsoft.com/en-us/azure/industry/agriculture/manage-farms-in-azure-farmbeats) with Azure Farm Beats.

 2. Add your device to your Farm.

      (Add Images)

 3. Generate [maps](https://docs.microsoft.com/en-us/azure/industry/agriculture/generate-maps-in-azure-farmbeats) in Azure Farm Beats.
 