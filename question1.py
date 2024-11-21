# Simplified Knowledge Base: List of restaurants with their location and cuisines
restaurants = [
    {"name": "Pizza Place", "location": "New York", "cuisines": ["Italian"]},
    {"name": "Sushi World", "location": "Los Angeles", "cuisines": ["Japanese"]},
    {"name": "Taco Hut", "location": "New York", "cuisines": ["Mexican"]},
]

# Function to find available food delivery options based on location and cuisine preferences
def find_delivery_options(location, preferred_cuisine):
    available_options = []
    
    # Loop through the restaurants to check for matching location and cuisine
    for restaurant in restaurants:
        if restaurant["location"] == location and preferred_cuisine in restaurant["cuisines"]:
            available_options.append(restaurant["name"])
    
    return available_options

# Sample usage of the function
def main():
    # Customer's location and cuisine preferences
    customer_location = input("Enter your location (e.g., New York, Los Angeles): ")
    preferred_cuisine = input("Enter your preferred cuisine (e.g., Italian, Japanese, Mexican): ")

    # Get the available delivery options
    options = find_delivery_options(customer_location, preferred_cuisine)

    # Output the result
    if options:
        print("Available delivery options:")
        for option in options:
            print(option)
    else:
        print(f"No delivery options available for {preferred_cuisine} in {customer_location}.")

if __name__ == "__main__":
    main()
