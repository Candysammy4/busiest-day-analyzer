import requests

API_KEY = "DEMO_KEY"


def get_photo_count(date):
    """
    Returns the number of photos for a specific date.
    """

    url = f"https://api.nasa.gov/EPIC/api/natural/date/{date}"

    response = requests.get(url, params={"api_key": API_KEY})

    if response.status_code != 200:
        print(f"Error retrieving {date}")
        return 0

    photos = response.json()

    return len(photos)


def build_year_dictionary(month, day, start_year, end_year):
    """
    Builds a dictionary where:
    key = year
    value = number of photos
    """

    year_counts = {}

    for year in range(start_year, end_year + 1):

        date = f"{year}-{month:02d}-{day:02d}"

        count = get_photo_count(date)

        year_counts[year] = count

    return year_counts


def find_busiest_year(year_counts):
    """
    Returns the year with the most photos.
    """

    busiest = max(year_counts, key=year_counts.get)

    return busiest


def find_quietest_year(year_counts):
    """
    Returns the year with the fewest photos.
    """

    quietest = min(year_counts, key=year_counts.get)

    return quietest


def display_results(year_counts):

    print("\nPhoto Counts By Year")

    for year in year_counts:
        print(f"{year}: {year_counts[year]} photos")

    busiest = find_busiest_year(year_counts)
    quietest = find_quietest_year(year_counts)

    print("\nBusiest Year")
    print(f"{busiest}: {year_counts[busiest]} photos")

    print("\nQuietest Year")
    print(f"{quietest}: {year_counts[quietest]} photos")


def main():

    print("NASA EPIC Busiest Day Analyzer")

    month = int(input("Enter month (1-12): "))
    day = int(input("Enter day (1-31): "))

    start_year = int(input("Enter starting year: "))
    end_year = int(input("Enter ending year: "))

    year_counts = build_year_dictionary(
        month,
        day,
        start_year,
        end_year
    )

    display_results(year_counts)


main()
