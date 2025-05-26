# ToonTown Rewritten API Scripts

This repository contains scripts used to call the ToonTown Rewritten (TTR) REST API. Currently, functionality is being built to call the 'invasions' endpoint and display the current 'districts' being invaded, which cog (i.e. Enemy) is invading, and the progress on the invasion (i.e. time left). 

Plans are in place to expand the scripts to include using other endpoints available such as 'district populations', 'field-offices', 'doodles', and 'silly-meter'.

Assuming you have Python 3 installed, you just need to run the below commands in a Command Prompt window (Terminal on MAC) to install the needed resources to run these scripts:

pip install requests
pip install pandas

Below are links for external API Endpoints and Python library documentation used in scripts:

TTR Invasions API - https://github.com/ToontownRewritten/api-doc/blob/master/invasions.md
Pandas - https://pandas.pydata.org/docs/
