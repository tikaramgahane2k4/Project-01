# Aadhar Link 

print("WelCome To The Aadhar Link Center")
print("For linking mobile number fill details !")

class aadhar_details:
    def __init__(self, name, date_of_birth, aadhar_number, addresh):
        self.name = name
        self.DOB = date_of_birth
        self.aadhar = aadhar_number
        self.addresh = addresh
      
    def link_number(self):
        print("___________________________________________________________")
        print("AADHAR CARD")
        print("___________________________________________________________")
        print("Name:", self.name)
        print("Date of Birth:", self.DOB) 
        print("Aadhar Number:", self.aadhar)
        print("Address:", self.addresh)
        print("___________________________________________________________")
        print("Aadhar is not link with number")
        print("Link your Aadhar with number")

        link = input("Enter Your Mobile Number: ")
        if len(link) == 10 and link.isdigit():
            print("___________________________________________________________")
            print("Aadhar is linked with your mobile number")
            print("___________________________________________________________")
            print("Name:", self.name)
            print("Date of Birth:", self.DOB) 
            print("Aadhar Number:", self.aadhar)
            print("Mobile Number:",link)
            print("Address:", self.addresh)
            print("___________________________________________________________")
            print("Get your Aadhar Online or Virtually after 15-days")
        else:
            print("Enter correct number")

data = aadhar_details(input("Enter Your Name : "), input("Enter Your Date of Birth(ex: 01-01-2000) : "), 456777708453, str(input("Your Addresh : ")))

data.link_number()


    
    