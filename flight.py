import csv #import CSV module for File handling
from datetime import datetime, timedelta # Functions to handle the date and time from the time module

class FlightManager:
    def __init__(self) -> None:
        #Class variables/ attributes
        self.flights = [] #List for Storing all the flight data 
        self.headers = [ #List of the headers for the flight data
             'FlightNumber',
             'FlightOrigin',
             'AircraftNumber', 
             'AirlineName',
             'AirlineCode',
             'PlaneModel',
             'DistanceFromAirport',
             'FlightSpeed',
             'TimeTabledArrival',
             'EstimatedArrivalTime'
        ]
        self.loadFlightsData() #Variable to load flight data from the CSV file 
        self.update_estimated_time_of_arrival() #Variable that updates the CSV file with the estimated arrival times 

         
    #Function to load flight from CSV file into the flight list
    def loadFlightsData(self) -> None:
        try :
            with open("FlightData.csv", 'r') as file: #Open the CSV in read mode
                csvreader = csv.reader(file) #CSV reader object
                next(csvreader) #This skips the CSV header 
                for row in csvreader:   #Iteration of each row in the CSV to print the contents of each row 
                    singleFlights = {}  #This creates a dictionary for each flight. it creates a better way to access the data in the CSV file
                    for index, header in enumerate(self.headers):  
                        singleFlights[header] = row[index]
                        if index == len(self.headers)-1:
                            self.flights.append(singleFlights) #Append flight data into list 
                        
        except FileNotFoundError:
                print("File could not be found")
    
    #Function to calculate estimated time of arrival given the distance and speed
    def calculate_time_of_arrival(self, distance, speed) -> int:
            estimated_time= distance / speed
            return estimated_time
    
    #Function to ad hours to a given time 

    def getTime(self, current_time, hours_to_add):
        try:
            # This converts the time string to a datetime object
            timeObj = datetime.strptime(current_time, "%H:%M") #strptime converts the time in hours into a time object

            # Add the specified number of hours to the time
            updatedTime = timeObj + timedelta(hours=hours_to_add) #timedelta performs the calculatio of the hours variable 

            # Convert time "HH:MM" format
            newTime = updatedTime.strftime("%H:%M") # strftime formats the value of the updated time in an hour minute format 
            
            return newTime #Returns the value of new time 
        except ValueError:
            return "Incorrect time format."
        


    #Function to update the estimated arrivval times result into the self. flights list 
    def update_estimated_time_of_arrival(self):
        for index, flight in enumerate(self.flights):   #For loop to iterate through each flight 
            
            distance = int(flight['DistanceFromAirport'])  # Accessing distance for each flight
            speed = int(flight['FlightSpeed'])  # Accessing the speed of each flight 

            estimated_time= self.calculate_time_of_arrival(distance, speed)
            time_value = round(estimated_time, 2) #Rounds up the estimated arrival time to 2 SF
            new_time = self.getTime(self.flights[index]['TimeTabledArrival'], time_value)

            # Add  estimated arrivlal time to self.flights
            self.flights[index]['EstimatedArrivalTime'] = new_time
    

    # This function gets all the flight information
    def getAllFlightsInfo(self) -> list:
         return self.flights #Return all flights 
    
    #This function diplays flight information when the user enters the flight number of a particular flight
    def getIndividualFlightInfo(self, flightNumber) -> dict:
        individualFlight = {} #Create an Empty dictionary
        for flight in self.flights:
             if str(flight['FlightNumber']).lower() == str(flightNumber).lower(): #Check if the flight number matches the number the user has input
                  individualFlight = flight
                  return individualFlight
             
    

             
         
         


