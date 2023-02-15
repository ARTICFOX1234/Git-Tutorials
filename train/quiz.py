# from train_data import data

class Train:

    def __init__(self,seat1,seat2,train_info):
        # self.name = name
        # self.fare = fare
        self.info_list = train_info
        self.seat1 = seat1
        self.seat2 = seat2
        self.index_no1 = 0
        self.index_no2 = 1
        


    def bookTicket(self):
        self.train_name1 = self.info_list[self.index_no1]
        self.train_name2 = self.info_list[self.index_no2]
        
        return f"Which train you want to choose? {self.train_name1.name} or {self.train_name2.name}: "

        # user_input = input(f"Which train you want to choose? {self.train_name1.name} or {self.train_name2.name}: ").lower()

        # self.train_name(user_input)
                                                                       
    def train_name(self,user_input):
        # print(f"The name of the train is {self.name}")
        # self.train_name1 = self.info_list[self.index_no1]
        # self.train_name2 = self.info_list[self.index_no2]
        # print(self.train_name1.name)
        # end = False
        # while not end:
        
        if user_input.lower()=="black diamond":
            # print(f"The name of the train is {self.train_name1.name}")
            if self.seat1>0:
                   self.seat1-=1
                   return (f"Ther are {self.seat1+1} seats available")
                #    print(f"Your ticket has been booked! Your seat number is {self.seat1+1}")
                #    return True

        if user_input.lower()=="poorva express":
            # print(f"The name of the train is {self.train_name2.name}")
            if self.seat2>0:
                   self.seat2-=1 
                   return (f"There are {self.seat2} seats available")
                #    print(f"Your ticket has been booked! Your seat number is {self.seat2+1}")
                #    return True

        # self.get_status(user_input, train_name1.name, train_name2.name)
        # self.bookTicket(user_input)
        # self.get_status(user_input, train_name1.name, train_name2.name)
            # self.bookTicket(user_input,train_name1.seats, train_name2.seats)
        # restart=input("Type 'yes' if you want to book a ticket again. Otherwise type 'no'.\n")

        # if restart=="no":
        #     end=True
        #     print("Thank you")

    def booking_continue(self):
        return (self.seat1 or self.seat2) > 0
            
        

        


              
 