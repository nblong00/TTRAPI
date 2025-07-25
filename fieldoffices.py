import utils
import pandas
import time

URL = "https://www.toontownrewritten.com/api/fieldoffices"
ZONE_ID_LOOKUP = {"3100":"Walrus Way","3200":"Sleet Street","3300":"Polar Place","4100":"Alto Avenue","4200":"Baritone Boulevard","4300":"Tenor Terrace","5100":"Elm Street","5200":"Maple Street","5300":"Oak Street","9100":"Lullaby Lane","9200":"Pajama Place"}
ID_TO_NEIGHBORHOOD = {"3100":"The Brrrgh","3200":"The Brrrgh","3300":"The Brrrgh","4100":"Minne's Melodyland","4200":"Minne's Melodyland","4300":"Minne's Melodyland","5100":"Daisy Gardens","5200":"Daisy Gardens","5300":"Daisy Gardens","9100":"Donald's Dreamland","9200":"Donald's Dreamland"}
ENDPOINT = "(FOS)"


def welcome():
    print("\n-Welcome to the ToonTown Rewritten (TTR) Field Office Tracker-")
    print(f"It is currently {utils.dt()}\n")
    time.sleep(0.5)


def main_logic_loop(data):
    print("Field Office Scan Results:\n")
    for street in data['fieldOffices']:
        difficulty_rating = data['fieldOffices'][street]['difficulty'] + 1
        street_name = ZONE_ID_LOOKUP[street]
        neighborhood = ID_TO_NEIGHBORHOOD[street]
        if data['fieldOffices'][street]['difficulty'] in range(1, 4):
            # Explict double space
            difficulty_rating = f"{difficulty_rating}  stars"
        elif data['fieldOffices'][street]['difficulty'] == 0:
            # Explict double space & space at end of string
            difficulty_rating = "1  star "
        if data['fieldOffices'][street]['open']:
            open_status = "Yes"
        elif not data['fieldOffices'][street]['open']:
            open_status = "No"
        if data['fieldOffices'][street]['annexes'] > 0:
            annexes_left = f"{data['fieldOffices'][street]['annexes']} remaining"
            if data['fieldOffices'][street]['annexes'] in range(1, 10):
                # Explict double space
                annexes_left = f"{data['fieldOffices'][street]['annexes']}  remaining"
        else:
            annexes_left = "Field Office closing"
        utils.write_data_to_csv([street_name,
                                 neighborhood,
                                 difficulty_rating,
                                 open_status,
                                 annexes_left])


def pullin_API_data_again():
    print("\nRefresh Field Office Scanner data? (yes/no)")
    for attempt in range(5):
        if attempt == 4:
            print("Too many invalid entries. Program closing...")
            return True
        user_input = input("> ")
        if user_input.lower() in ["no", "n"]:
            print("\nExiting Field Office Scanner...")
            time.sleep(1)
            return True
        elif user_input.lower() not in ["no", "n", "yes", "y", "ye"] and attempt <= 2:
            print("Invalid entry. Would you like to run the Field Office Scanner again? (yes/no)")
            continue
        elif user_input.lower() in ["yes", "y", "ye"] and attempt <= 3:
            print("\nRunning Field Office Scanner in ToonTown Rewritten...\n")
            time.sleep(1)
            return False


def main():
    end_game = False
    welcome()
    while not end_game:
        data = utils.error_checking_and_logging(URL, ENDPOINT)
        utils.error_checking_and_logging(URL, ENDPOINT)
        utils.create_csv_for_data(["Location",
                                "Neighborhood",
                                "Difficulty",
                                "Open?",
                                "Annexes"])
        main_logic_loop(data)
        result = pandas.read_csv("AdjustedData.csv")
        print(result)
        end_game = pullin_API_data_again()
        utils.delete_csv_from_system()
