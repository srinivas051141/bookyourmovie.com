class BookYourMovie:
    def __init__(self):
        
        print('\033[91mWelcome to Bookyourmovie.com, Where the movies come to you!!\033[00m');
        print('Enter the number of rows:');
        self.r=input();
        print('Enter the number of columns:');
        
        self.c=input();
        
        if (self.r).isnumeric() and (self.c).isnumeric() and int(self.r)>0 and int(self.c)>0:
            
            self.s=[0]*int(self.r);
            self.t =[' ']+[str(i+1) for i in range(int(self.c))];
            for i in range(int(self.r)):
                self.s[i]=[str(i+1)]+['\033[91mS\033[m']*int(self.c);
        
        #calculating totalincome and making currentincome zero    
            if int(self.r)*int(self.c)<=60:
                self.totalincome=10*int(self.r)*int(self.c);
            if int(self.r)*int(self.c)>=60:
                if int(self.r)%2==0:
                    self.totalincome=9*int(self.r)*int(self.c);
                else:
                    f= (int(self.r)//2)
                    self.totalincome = (8*f*int(self.c))+(10*(int(self.r)-f)*int(self.c));
        
            self.currentincome=0;
        
            self.userinfo = {};
        
            self.options();
        else:
            print('Rows and columns should be positive integers.');
            self.__init__();
        
            
        
    def options(self):
        print("\n");
        print('\033[1m');
        print('Select from the below options');
        print('1.Show the seats');
        print('2.Buy a Ticket');
        print('3.Statistics');
        print('4.Show booked Tickets User Info.');
        print('0.Exit');
        print('Type corresponding number for corresponding option.')
        print('***********************');
        print('\033[0m')
        
        x = input();
        if x=='1':
            self.showtickets();
        elif x=='2':
            self.buyticket();
        elif x=='3':
            self.statistics();
        elif x=='4':
            self.show_booked_ticket_n_userinfo();
        elif x=='0':
            self.exit();
        else:
            print('\033[91mChoose from the appropriate options. \033[00m ');
            self.options();
    
    def showtickets(self):
        print("\n");
        print ('Cinema:');
        print(' '.join(self.t));
        for i in self.s:
            print(' '.join(i));
        print('\n');
        print('  \033[91mS\033[m - Vacant          B - Booked\n');
        
        self.options();
        
    def buyticket(self):
        print("\n");
        x1= input('Row Number :');
        x2 = input('Column Number : ');
        if x1.isnumeric() and x2.isnumeric() and int(x1)<=int(self.r) and int(x2)<=int(self.c) and int(x1)>0 and int(x2)>0 and self.s[int(x1)-1][int(x2)]!='B':
            
        
            
            
            price=0;
        
            if int(self.r)*int(self.c)<=60:
                price = 10;
            if int(self.r)*int(self.c)>=60:
                if int(x1)> int(self.r)/2:
                    price = 8;
                if int(x1)<=int(self.r)/2:
                    price =10;
        
            print("\n");        
            print('Price for that seat is $ '+str(price)+'.');
            print("\n");
            print('would you like to book?');
            print('Type \033[91m"yes"\033[m for booking \n\033[91m"no"\033[m for options.');
        
        
            yorn=input();
            if yorn =='yes':
                self.currentincome+=price;
                self.userinfo[x1+x2]={};
                print("\n");
                self.userinfo[x1+x2]['Name']=input('Name - ');
            
                self.userinfo[x1+x2]['Gender']=input('Gender - ');
                if self.userinfo[x1+x2]['Gender']=='m'or self.userinfo[x1+x2]['Gender']=='f' or self.userinfo[x1+x2]['Gender']=='M' or self.userinfo[x1+x2]['Gender']=='F' or self.userinfo[x1+x2]['Gender'] =='other' :
                    pass;
                else:
                    print('\033[91mType the correct Gender\033[00m');
                    self.userinfo[x1+x2]['Gender']= input('Gender - ');
            
                self.userinfo[x1+x2]['Age']= input('Age - ');
                if self.userinfo[x1+x2]['Age'].isnumeric() and int(self.userinfo[x1+x2]['Age'])>=0 and int(self.userinfo[x1+x2]['Age'])<=100 :
                    pass;
                else:
                    print('\033[91mType the correct age\033[00m');
                    self.userinfo[x1+x2]['Age']= input('Age - ');
                self.userinfo[x1+x2]['TicketPrice']= price;
            
                self.userinfo[x1+x2]['Phone no']= input('Phoneno - ');
                if self.userinfo[x1+x2]['Phone no'].isnumeric() and len(self.userinfo[x1+x2]['Phone no'])==10:
                    pass;
                else:
                    print('\033[91mNumber is invalid\033[00m');
                    self.userinfo[x1+x2]['Phone no']= input('Phoneno - ');
                
                print('\033[91mBooked Successfully!!\033[m');
                self.s[int(x1)-1][int(x2)]='B';
            elif yorn =='no':
                print("\n");
                print('Thank you!');
            else :
                print('\033[91mYour input is invalid!\033[00m');
        else:
            print('\n\033[91mYour input should be valid Postive numbers and the ticket should be vacant\033[00m');
            
        
        self.options();
        
    
    def statistics(self):
        
        print("\n");
        print('\033[1m'+'Number of purchased tickets : '+str(len(self.userinfo)));
        print('Percentage : ',str((self.currentincome*100)/self.totalincome)+'%');
        print('Current Income : ','$'+str(self.currentincome));
        print('Total Income : ','$'+str(self.totalincome));
        print('************************************');
        print('\033[0m');
        
        self.options();
        
    def show_booked_ticket_n_userinfo(self):
        print("\n");
        
    
        i= input('Row Number : ');
        j= input('Column Number :');
            
            
        if i.isnumeric() and j.isnumeric() and int(i)<=int(self.r) and int(j)<=int(self.c) and int(i)>0 and int(j)>0 :
                
            if i+j in self.userinfo:
                print("\n");
            
                print('\033[1m'+'Name :',self.userinfo[i+j]['Name']);
                print('Gender : ',self.userinfo[i+j]['Gender']);
                print('Age :',self.userinfo[i+j]['Age']);
                print('TicketPrice :','$'+str(self.userinfo[i+j]['TicketPrice']));
                print('Phone no. : ',self.userinfo[i+j]['Phone no']);
                print('************************************************');
                print('\033[0m');
            else:
                print("\n");
                print(i+j+' is not booked yet' );
            
        
        else:
            print('\n\033[91mYour input should be Valid Positive integers.\033[00m');
            #self.show_booked_ticket_n_userinfo();
                
            
        self.options();
            
            
            
    def exit(self):
        pass;

x= BookYourMovie();
            
            
            
            
            
        
    
        
        