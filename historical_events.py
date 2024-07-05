import requests


def get_historical_events(month, day):
    """
    Fetches historical events for a given month and day from the History API.

    Args:
        month (str): The month as a string (e.g., "7" for July).
        day (str): The day as a string (e.g., "1" for 1st).

    Returns:
        list: A list of dictionaries containing historical events if the request is successful.
              Each dictionary contains:
                  - 'year' (int): The year of the event.
                  - 'text' (str): A description of the event.
                  - 'links' (list): A list of links related to the event.
        None: If the request is unsuccessful.
    """
    url = f"https://history.muffinlabs.com/date/{month}/{day}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        historical_events = data['data']['Events']
        return historical_events
    else:
        return None


if __name__ == "__main__":
    month = input("Enter the month (e.g., 7 for July): ")
    day = input("Enter the day (e.g., 1 for 1st): ")
    events = get_historical_events(month, day)
    print(f"Historical Events on {month}/{day}\n")
    if events:
        for event in events:
            print(f"Year: {event['year']}")
            print(f"Description: {event['text']}")
            print(f"Link: {event['links'][0]['link']}\n")
    else:
        print(f"Error fetching data. Please try again.")
