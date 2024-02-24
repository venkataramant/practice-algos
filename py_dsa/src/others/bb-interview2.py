# our service stast receiving company names and at any point in time, 
# we want to report top k most freqeuent companies (k not known in advance)

# Define API/Services to be called 
# From Start of API have to store the info
#Clients -1 
    # static (keeping this information in a system --- run pull mechanism)
    # Transistent (Dynamic -- Queue System)

# Intermediate System (Messaging Bus)/Buffer

# API/Services 
#(Directly invoked or receving from Message/Queue System or pull the information every 30 second)

# BackedSystemt to Calculate Frequency calculation
# Store them in Distributed Cache/Storage System

# Scope InMemory, Single System, One API Exposed to receive Comapny Name as input
# and maintian a map with ComapnyName--> No of Times it repeated.

'''
A
B
C
A
D
E
F
B
C
A
C

A-2
B-2
C-3
D-1
E-1
F-1



Dictionary
Frequence/No --> list
3 -- (A,C)
2 --

A (Remove from n)//2
  (Add to n+1)//3
  
1-->(2,(B)) -->(3,(C))-->(4,(A))

[-4:]

Map
2:-->same_list
3-->same_list

Integer represetning --frequency
"String"
"123" comapny VS 123


get_top(2):
A/C

unique company (2 mil)-- 



'''

class CompanyTracker:
    def __init__(self):
        self.company_info=dict()
        self.frequency_tracker=list()
    def insert_comapny(self,company_name):
        if company_name not in self.company_info:
            self.company[company]=1
            self._update_frequency(company_name,1)
        else:
            new_frequency=self.company_info[company_name]+1
            self.company_info[company]=new_frequency
            self._update_frequency(company_name,new_frequency)
        
            
    def _update_frequency(self,comapny_name,new_frequency):
        if new_frequency not  in self.frequency_tracker:
                new_frequency_list=list()
                self.frequency_tracker[new_frequency]=new_frequency_list
        self._add_comapny_to_frequceny_tracker(comapny_name,new_frequency)
            
        if new_frequency!=1:
            self._remove_comapny_from_frequceny_tracker(comapny_name,new_frequency-1)

    def _add_comapny_to_frequceny_tracker(self,comapny_name,frequency):
        frequency_list=self.frequency_tracker[frequency]
        frequency_list.append(comapny_name)
        self.frequency_tracker[new_frequency]=frequency_list # reupdate map not necessary
    def _remove_comapny_from_frequceny_tracker(self,comapny_name,old_frequency):
        frequency_list=self.frequency_tracker[old_frequency]
        frequency_list.remove(comapny_name)
        self.frequency_tracker[old_frequency]=frequency_list # reupdate map not necessary
        
    def get_top_k(self,k):
        
        return self.frequency_tracker[-1* k:] # out of bound expression
    def get_bottom_k(self,k):
        return self.frequency_tracker[0:k]
    def display():

'''
1. Same Comapny can appear at same_Time_stamp and retrieved at same_Time
2. Add Company(n) and Retrive it ranks
3. Sanitation Checks (I removed ..valdiating size/regular expression/validity)
4.
'''
        
if __name__=="__main__":
    pass
