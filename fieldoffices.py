import utils

URL = "https://www.toontownrewritten.com/api/fieldoffices"
ZONE_ID_LOOKUP = {"3100":"Walrus Way","3200":"Sleet Street","3300":"Polar Place","4100":"Alto Avenue","4200":"Baritone Boulevard","4300":"Tenor Terrace","5100":"Elm Street","5200":"Maple Street","5300":"Oak Street","9100":"Lullaby Lane","9200":"Pajama Place"}
ENDPOINT = "(FOS)"

data = utils.error_checking_and_logging(URL, ENDPOINT)
utils.create_CSV_for_data(["Location","Difficulty", "Open?", "Annexes"])

for street in data["fieldOffices"]:
    street_name = ZONE_ID_LOOKUP[street]
    if data["fieldOffices"][street]["difficulty"] in range(1, 4):
        difficulty_rating = f"{data["fieldOffices"][street]["difficulty"]} stars"
    elif data["fieldOffices"][street]["difficulty"] == 0:
        difficulty_rating = f"No stars"
    if data["fieldOffices"][street]["open"]:
        open_status = "Yes"
    elif not data["fieldOffices"][street]["open"]:
        open_status = "No"
    if data["fieldOffices"][street]["annexes"] > 0:
        annexes_left = f"{data["fieldOffices"][street]["annexes"]} remaining"
    else:
        annexes_left = "Field Office closing"
    utils.write_data_to_CSV([street_name, difficulty_rating, open_status, annexes_left])
    