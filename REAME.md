# Pass availability monitor

This tool helps you automatically monitor the availability of trail passes on the [BC parks website](https://reserve.bcparks.ca/dayuse/).

To get hike on any trails listed on the website, you need to get passes which become available 2 days before at 7:00 AM PST. Once the passes are sold out and you were not able to secure them, you need to check the website regulary. This tool automates that monitoring process and sends a notification to your e-mail when the intended passes become available.  

## Installation + Setup

Everything runs locally. Credentials are encrypted and stored locally. Only website check needs internet access.

**Desktop notifications**  
No set-up required. Works on macOS.

**E-mail notifications**  
To be launched soon

## Usage

**Overview**  
Once you open the file, a command line tool opens and asks for a bunch of relevant inputs from you and once you hit "Start execution", the monitoring begins and lasts for 3 hours by default. If you want to stop execution, press 'Ctrl+C'.  

**Detailed steps**  
The application will ask for the following inputs from you:  

- Execution Mode: Just press enter (this is for developers)
- Trail name: E.g., Cheakamus, Diamond head, Joffre etc. It is case insensitive however it should be spelled correct
- Target date: Format YYYY-MM-DD (2024-07-26)
