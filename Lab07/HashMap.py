class HashMap:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(size)]


    def _hash_function(self, key):
        return hash(key) % self.size


    def put(self, key, value):
        """Insert a (key, value) pair in the HashMap."""
        index = self._hash_function(key)
        bucket = self.hash_table[index]

        for k, v in bucket:
            if k == key:
                v = value  # Update the value if the key already exists
                return
            
        # Insert the new key-value pair into the bucket
        bucket.append((key, value))


    def get(self, key) -> int:
        """Retrieve the value corresponding to a key in the HashMap."""
        index = self._hash_function(key)
        bucket = self.hash_table[index]
        
        # Iterate over the bucket and return the value if the key is found
        for k, v in bucket:
            if k == key:
                return v
            
        # Return None if the key is not found
        return None  # Key not found


    def remove(self, key, value):
        """Remove the value corresponding to a key in the HashMap."""
        index = self._hash_function(key)
        bucket = self.hash_table[index]

        # Iterate over the bucket and remove the key-value pair if it exists
        for i, (k, v) in enumerate(bucket):
            if k == key and v == value:
                bucket.pop(i)
                return


    def display(self):
        """Display the updated HashMap."""
        for index, bucket in enumerate(self.hash_table):
            print(f"Bucket {index}:")
            for item in bucket:
                print(f"  {item[0]}: {item[1]}")
                
    def max_passengers_in_flight(self, flight_number) -> (str, int):
        max_passengers = 0
        max_trip_id = None
        # Get the bucket for the given flight number
        bucket = self.hash_table[self._hash_function(flight_number)]
        # Iterate over the bucket and find the trip with the maximum number of passengers
        for key, value in bucket:
            if key == flight_number and value.passengers > max_passengers:
                max_passengers = value.passengers
                max_trip_id = value.trip_id
        return max_trip_id, max_passengers
    

class FlightNode:
    def __init__(self, flight_number, trip_id, passengers):
        self.flight_number = flight_number
        self.trip_id = trip_id
        self.passengers = passengers



# Display the hash map
my_hash_map = HashMap(7)
0, 1, 4, 9, 16, 25, 36, 49, 64, 81
my_hash_map.put("aaa", 0)
my_hash_map.put("bbb", 1)
my_hash_map.put("ccc", 4)
my_hash_map.put("ddd", 9)
my_hash_map.put("eee", 16)
my_hash_map.put("fff", 25)
my_hash_map.put("ggg", 36)
my_hash_map.put("hhh", 49)
my_hash_map.put("ccc", 64)
my_hash_map.put("ccc", 81)
my_hash_map.display()  

# Retrieve values
print("Retrieve values:")
print("aaa:", my_hash_map.get("aaa"))  
print("bbb:", my_hash_map.get("bbb"))
print("ccc:", my_hash_map.get("ccc"))

# Remove a key-value pair
my_hash_map.remove("bbb", 1)  

# Display the updated hash map
my_hash_map.display() 

#Max Passengers on Trip
my_map = HashMap(11)
# Add flight nodes (flight_number, trip_id, passengers)
my_map.put(16, FlightNode(16, "Trip 1", 300))
my_map.put(16, FlightNode(16, "Trip 2", 700))
my_map.put(29, FlightNode(29, "Trip 1", 800))
my_map.put(29, FlightNode(29, "Trip 2", 250))
my_map.put(36, FlightNode(29, "Trip 3", 500))
my_map.put(36, FlightNode(36, "Trip 1", 500))
my_map.put(36, FlightNode(36, "Trip 2", 340))
my_map.put(36, FlightNode(36, "Trip 3", 900))
my_map.put(36, FlightNode(36, "Trip 4", 400))
my_map.put(49, FlightNode(49, "Trip 1", 250))
my_map.put(49, FlightNode(49, "Trip 2", 550))

max_passengers = my_map.max_passengers_in_flight(49)
if max_passengers is not None:
    print("Largest number of people in flight at once :", max_passengers)
else:
    print("Flight not found in the map")


