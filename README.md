# Busiest Day Analyzer

My program uses NASA's EPIC data to compare the number of Earth photos taken on the same month and day across multiple years. It determines which year had the most photos of the busiest year and which had the fewest photos of the quietest year.

## How it works
- get_photo_count(date): Requests EPIC data for a specific date and returns the number of photos taken on that day.
- build_year_dictionary(month, day, start_year, end_year): Creates a dictionary that stores the photo count for the same month and day across multiple years.
- find_busiest_year(year_counts): Uses the dictionary to determine which year had the highest number of photos.

## How to run
1. Install requests: pip install requests
2. Run: python <your_file_name>.py
3. Uses "DEMO_KEY" by default. Swap in your own key
   from api.nasa.gov for higher rate limits.

## Built with
Python, requests and the NASA EPIC API
