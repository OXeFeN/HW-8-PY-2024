
#Task 1:
class Human:
    def __init__(self, full_name, date_of_birth, phone, city, country, home_address):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.phone = phone
        self.city = city
        self.country = country
        self.home_address = home_address
        
    def new_human():
        fn=input("Insert full name: ")
        db=input("Insert date of birth: ")
        p=input("Insert phone number: ")
        c=input("Insert city: ")
        cn=input("Insert country: ")
        home=input("Insert your home address: ")
        return Human(full_name=fn, date_of_birth=db, phone=p, city=c, country=cn, home_address=home)
    
    def print_human(self):
        underline = "-" * 200
        print("")
        print(f"""{"[Full name]":^16}{"[date of birth]":^15}{"[Phone number]":^17}{"[City]":^30}{"[Country]":^20}{"[Home address]":^50}""")
        print(underline)
        print(f"""|{self.full_name:25}|{self.date_of_birth:15}|{self.phone:^10}|{self.city:30}|{self.country:30}|{self.home_address:50}|""")
        print(underline)

lukas = Human.new_human()
lukas.print_human()