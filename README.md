# Send_Mail_Alert_To_Twilio
For windows we server 2022:

This is for windows server:
>> Install python
Follow this commands in powershell:

Set-ExecutionPolicy AllSigned

Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

choco install python --pre

py get-pip.py

py -m pip install --upgrade pip

After installing setup the ENV variables in windows.

>> Install required modules

pip install twilio
pip install schedule
pip install win32com.client


>> If windows server don't have outlook then please download it.
Link: https://www.filehorse.com/download-microsoft-office-64/

>> If you don't have twilio account then create a account from the below link:
Link: https://www.twilio.com/en-us
