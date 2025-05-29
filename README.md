# ToonTown Rewritten API Scripts

This repository contains scripts used to call the ToonTown Rewritten (TTR) REST API. Currently, invasions.py is built to call the 'invasions' endpoint and display the current 'districts' being invaded, which cog (i.e. Enemy) is invading, and the progress on the invasion (e.g. time left). Mega-Invasions are accounted for should they occur. Populations.py allows users to call the 'population' endpoint to see the current district populations throughout TTR. Users can perform sorting on the list as well to see only higher/lower district populations or all district populations.

Plans are in place to expand the scripts to include using other endpoints available such as 'field-offices', 'doodles', and 'silly-meter'.

Assuming you have Python 3 installed, you just need to run the below commands in a Command Prompt window (Terminal on MAC) to install the needed resources to run these scripts:

* pip install requests
* pip install pandas

Below are links for external API Endpoints and Python library documentation used in scripts:

* TTR Invasions API endpoint - https://github.com/ToontownRewritten/api-doc/blob/master/invasions.md
* TTR Population API endpoint - https://github.com/ToontownRewritten/api-doc/blob/master/population.md
* Pandas - https://pandas.pydata.org/docs/
* Dateutil - https://dateutil.readthedocs.io/en/stable/
* Requests - https://requests.readthedocs.io/en/latest/
