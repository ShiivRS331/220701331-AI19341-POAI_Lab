# Knowledge base of direct train routes between cities
train_routes = {
    'New York': {'Boston': 'Direct', 'Washington': 'Direct', 'Chicago': 'Connecting'},
    'Boston': {'New York': 'Direct', 'Chicago': 'Connecting'},
    'Washington': {'New York': 'Direct', 'Chicago': 'Connecting'},
    'Chicago': {'New York': 'Connecting', 'Boston': 'Connecting', 'Washington': 'Connecting'},
    'Los Angeles': {'San Francisco': 'Direct', 'Seattle': 'Connecting'},
    'San Francisco': {'Los Angeles': 'Direct', 'Seattle': 'Connecting'},
    'Seattle': {'Los Angeles': 'Connecting', 'San Francisco': 'Connecting'}
}

# Function to find available train routes between two cities
def find_train_routes(start_city, destination_city):
    if start_city in train_routes:
        if destination_city in train_routes[start_city]:
            route_type = train_routes[start_city][destination_city]
            return f"The train route from {start_city} to {destination_city} is {route_type}."
        else:
            return f"No direct or connecting route from {start_city} to {destination_city}."
    else:
        return f"{start_city} is not in our train network."

# Main function to get user input and display results
def main():
    # Get customer's start city and destination city
    start_city = input("Enter your starting city: ")
    destination_city = input("Enter your destination city: ")

    # Get the available train routes
    result = find_train_routes(start_city, destination_city)

    # Output the result
    print(result)

# Ensure the script runs only when it is executed directly
if __name__ == "__main__":
    main()
