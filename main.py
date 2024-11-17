import csv
from flight import FlightManager #Importing the flight manger class from flight.py 


flightData = FlightManager() #Flight manager object 

# Access options of the menu list 
def accessOption(choice):
    print("\n")
    if(choice == "1"):
        displayAllFlights() #Function is called to display all fligths 
    elif(choice=="2"):
        displayIndividualFlights() #Function is called to display information about a specific flight
    elif(choice=="3"):
        exitProgram() #The function is called and the program is exited 
    else:
        print("Invalid input. Enter 1,2 or 3")

# This function gets all the flights details from the Flights class 
def displayAllFlights():
    allFlghts = flightData.getAllFlightsInfo() #Variable to retrieve all flights 
    for flight in allFlghts:
        for header in flightData.headers:
            print(header +"  -  "+ flight[header]) #print all the flight details
        print("\n")

# This function get all the individual flights details from the flights class 
def displayIndividualFlights():
    flight_number=input("Enter your Flight number: ")
    flight_details = flightData.getIndividualFlightInfo(flight_number) #Retrieve details of the specific flight the user has input 

    # If the flight exist, then it is displayed 
    if flight_details is not None:
        print("\nYour flight details are : \n")
        for header in flightData.headers: #Marches through headers 
            print(header +"  -  "+ flight_details[header])
    else:
        print("Invalid flight number")

   

# This function is to exit the program 
def exitProgram():
    print("\nThank you for using Ufo's software :)")
    createCSV() #Function creates a CSV file and saves the updated flight details (Estimated arrival time)
    exit()

#Write the Data into a CSV file
def createCSV():
    try:
        with open('updated.csv', 'w', encoding='UTF8', newline='') as f: #Open the CSV file for writing 
        
        
            writer = csv.DictWriter(f, fieldnames=flightData.headers)
            writer.writeheader()
            writer.writerows(flightData.flights) #Update the CSV 
    except:
        print("Error while writing to file")

# The main function 
if __name__ == '__main__':
    while True:    #While loop continues until the program is exited 
        print("~Menu~")
        print ("1. - Display all flights ")
        print ("2. - Display individual flights")
        print ("3. - Exit program")

        choice = input("Enter a choice from the above options: ")
        accessOption(choice)  #Function handles the user choice by calling thr accessOption function

        print("\n\n")


#Ask user if they want to view all flights or view individual flights

# If user picks all, then display all the flights info 

# If user picks individual, Ask them for the flight number
    
# Then Display flight info

# The cycle continies until the user decides to stop 
