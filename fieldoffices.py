import utils
import pandas

URL = "https://www.toontownrewritten.com/api/fieldoffices"
ZONE_ID_LOOKUP = {"3100":"Walrus Way","3200":"Sleet Street","3300":"Polar Place","4100":"Alto Avenue","4200":"Baritone Boulevard","4300":"Tenor Terrace","5100":"Elm Street","5200":"Maple Street","5300":"Oak Street","9100":"Lullaby Lane","9200":"Pajama Place"}
ID_TO_NEIGHBORHOOD = {"3100":"The Brrrgh","3200":"The Brrrgh","3300":"The Brrrgh","4100":"Minne's Melodyland","4200":"Minne's Melodyland","4300":"Minne's Melodyland","5100":"Daisy Gardens","5200":"Daisy Gardens","5300":"Daisy Gardens","9100":"Donald's Dreamland","9200":"Donald's Dreamland"}
ENDPOINT = "(FOS)"


def chart_title():
    print(f"Field Office Locations & Status:\n")


def logic_loop(data):
    for street in data["fieldOffices"]:
        street_name = ZONE_ID_LOOKUP[street]
        neighborhood = ID_TO_NEIGHBORHOOD[street]
        if data["fieldOffices"][street]["difficulty"] in range(1, 4):
            # Explict double space
            difficulty_rating = f"{data["fieldOffices"][street]["difficulty"]}  stars"
        elif data["fieldOffices"][street]["difficulty"] == 0:
            difficulty_rating = "No stars"
        if data["fieldOffices"][street]["open"]:
            open_status = "Yes"
        elif not data["fieldOffices"][street]["open"]:
            open_status = "No"
        if data["fieldOffices"][street]["annexes"] > 0:
            annexes_left = f"{data["fieldOffices"][street]["annexes"]} remaining"
            if data["fieldOffices"][street]["annexes"] in range(1, 10):
                # Explict double space
                annexes_left = f"{data["fieldOffices"][street]["annexes"]}  remaining"
        else:
            annexes_left = "Field Office closing"
        utils.write_data_to_CSV([neighborhood, street_name, difficulty_rating, open_status, annexes_left])


def main():
    data = utils.error_checking_and_logging(URL, ENDPOINT)
    utils.create_CSV_for_data(["Neighborhood", "Location", "Difficulty", "Open?", "Annexes"])
    chart_title()
    logic_loop(data)
    result = pandas.read_csv("AdjustedData.csv")
    print(result)


main()
