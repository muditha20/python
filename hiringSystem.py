from os import remove
vehiclesCategory = ["car", "van", "threeWheelers", "lorry", "trucks"] # all vehicle categories 

car = ["passanger-3-AC c","passanger-3-NonAC c", "passanger-6-AC c", "passanger-6-NonAC c", ]
van = ["passanger-6-AC v","passanger-6-NonAC v", "passanger-8-AC v", "passanger-8-NonAC v", ]
threeWheelers = ["passanger-3 t" ]
lorry = ["2500kg-lorry l", "3500kg-lorry l" ]
trucks = ["7ft-trucks tr", "12ft-trucks tr" ]

available_vehicles = [car, van, threeWheelers, lorry, trucks] 
hireJobs = [] #list to add hiring vehicles


def vehiclesCategoryList():  #function for print all vehicles Categories
    for i, no in enumerate(vehiclesCategory):
        print(i,"-",no)

def carList(): #function for print all cars in car list  
    print("----Car list---")
    for i, no in enumerate(car):
        print(i,"-",no)

def vanList(): #function for print all vans in van list  
    print("---Van list---")
    for i, no in enumerate(van):
        print(i,"-",no)
 
def lorryList(): #function for print all lorries in lorry list  
    print("----Car lorry---")
    for i, no in enumerate(lorry):
        print(i,"-",no)

def truckList(): #function for print all trucks in truck list  
    print("----Truck list---")
    for i, no in enumerate(trucks):
        print(i,"-",no)

def threewheelList(): #function for print 3wheelers cars in threewheelers list  
    print("----Three wheelers list---")
    for i, no in enumerate(threeWheelers):
        print(i,"-",no)

def hireJobsView(): #function for print all active hires
    print("----Hired jobs list---")
    for i, no in enumerate(hireJobs):
        print(i,"-",no)

vehicleListFunctions = [carList, vanList, threewheelList, lorryList, truckList] # print all available vehicles in each category


#=============================== Add vehicle =========================
def addVehicle():
    vehiclesCategoryList()
    inSelect = int(input("To add vehicle select category and press enter : "))
    selectedAddList = available_vehicles[inSelect]
    newVehicle = input("Enter new vehicle name : ")
    selectedAddList.append(newVehicle)
    print("New vehicle sucessfully added")

#=============================== remove vehicle ======================
def removeVehicle():
    vehiclesCategoryList()
    inSelect = int(input("To view vehicle list and press enter : "))

    vehicleListFunctions[inSelect]()

    removeItem = int(input("Enter id to remove : "))
    selectedRemList = available_vehicles[inSelect]
    selectedRemList.remove(selectedRemList[removeItem])
    vehicleListFunctions[inSelect]()
    print("Selected " + str(vehiclesCategory[inSelect]) + " vehicle has succefully removed...")



#=============================== Assign jobs to vehicles ==============
def assignJobs():
    vehiclesCategoryList()

    inSelect = int(input("To view vehicle list press vehicle no and enter : "))
    vehicleListFunctions[inSelect]()
    addItem = int(input("Enter vehicle id to add a job : "))
    selectAddList = available_vehicles[inSelect]
    hireJobs.append(selectAddList[addItem])
    print(selectAddList[addItem]+ " added to hired list")
    selectAddList.remove(selectAddList[addItem]) #remove form vehicle list currently available in hire list
    print(hireJobs)


#=============================== Complete jobs of the vehicles ===========
def completeHire():
    hireJobsView()
    completeJobVehicleId = int(input("Enter id to complete hire: "))

    for i in hireJobs:
        if i[-1] == 'c':
            car.append(i)

        elif i[-1] == 'v':
            van.append(i)
        
        elif i[-1] == 't':
            threeWheelers.append(i)
        
        elif i[-1] == 'l':
            lorry.append(i)
        
        elif i[-1] == 'tr':
            trucks.append(i)

    print(hireJobs[completeJobVehicleId]+ " vehicle completed hire")
    hireJobs.remove(hireJobs[completeJobVehicleId])


#while loop for run operations and update vehicle details
while True:
    print("==============================")
    print("==> Select a option <==")
    print("Enter 0 to Add new vehicles")
    print("Enter 1 to view vehicles category list")
    print("Enter 2 to remove vehicles")
    print("Enter 3 to assign jobs")
    print("Enter 4 to view current jobs")
    print("Enter 5 to complete hires")
    print("Enter 6 to exit")
    print("==============================")

    inVal = input("Enter a number to select option : ")

    if inVal == "0": #add new vehicles
        addVehicle()
    
    elif inVal == "1": #view avilable vehicles
        vehiclesCategoryList()
        inSelect = input("Vehicle list : ")
        vehicleListFunctions[int(inSelect)]()


    elif inVal == "2": #remove vehicles
        removeVehicle()
        pass

    elif inVal == "3": #add jobs
        assignJobs()
        pass

    elif inVal == "4": #view active hires 
        print("Hired vehicles = "+ str(hireJobs))
        pass

    elif inVal == "5":  #complete hires
        if len(hireJobs) ==0:
            print("No hired vehicles")
        else:
            completeHire()
        pass
    elif inVal == "6": #exit from system
        print("System is closed... \n ")
        break
    
    else:
        print("Enter correct value in the menu!")



