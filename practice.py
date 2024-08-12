
# -*- coding: utf-8 -*-
"""
For this assignment you will be analyzing data from 
the National Park Service regarding the species found in the parks.


Using the parks and species data provided, you will create a program 
to load the data into a series of classes and analyze the data to answer 
questions related to the data. This data comes from https://irma.nps.gov/NPSpecies/. ;

For this project, you will need to submit a series of python files 
as well as the final output.


Questions to answer:
which park has the most species by area
what is the most common family of mammals in each park
how many endangered species exist in each park, broken down by category

Required file submission
park.py
species.py
nps_processor.py
test_nps_processor.py
nps_summary.txt

Park
class to store the information about each park
properties
code - string
name - string
state - list of state codes 
acres - int
latitude - float
longitude - float
species - list of species

methods
species_by_area - returns the number of species per 10000 acres
most_common_family - returns the most common family found for the specified category
conservation_status_by_categiry - returns the category and count of species for the 
specified conservation status

Species
class to store the individual species data
properties
species_id
category
order
family
scientific_name
common_names
record_status
occurrence
nativeness
abundance
seasonality
conservation_status

nps_processor
this is the main program that will read the data from the files in to a list of park objects 
the program should write the results to a nps_summary.txt file
test_nps_processor

this should contain a series of test methods which validates the data returned 
for a sample test file
for the tests, you should use the test_species.csv file
nps_summary.txt

this will contain the output when run against the full species.csv file

@author: Sackitey Joseph

"""
import csv

def read_file(filename):   
    all_lines = []
    with open(filename, "r", encoding="utf8") as csvfile:
        ereader = csv.reader(csvfile, delimiter = ',', quotechar='"')        
        # for e in ereader:
        #     print(e)
        for line in csvfile:
            line = line.strip("\n")
            all_lines.append(line)
        lf,species_id,category,order,family,scientific_name,common_names,record_status,occurrence,nativeness,abundance,seasonality,conservation_status):
    #     self.species_id=species_id
    #     self.category=category
    #     self.family=family
    #     self.scientific_name=scientific_name
    #     self.common_names=common_names
    #     self.record_status=record_status
    #     self.occurence= occurrence
    #     self.nativeness=nativeness
    #     self.abundance= abundance
    #     self.seasonality=seasonality
    #     self.conservation_status=conservation_status
        
    #     def common_family(self):
            
    #         self.family_names= []
    #         self.order_names= []
    #         self.mammals_list= []
    #         with open(filename,"r",encoding="utf8") as common:
    #             freader = csv.reader(common,delimiter = ',',quotechar='"')
    #             for f in freader:
    #                 f= f.strip("\n")                    
    #                 self.family_names.append(self.family)
    #                 self.order_names.append(self.order)
    #             for order in range(len(self.order_names)):
                    
    #                 if order=="Mammal":
    #                     self.mammals_list.append(self.family_names[order])
    #         return self.mammals_list
        
    #     def count_mammals_list(self):
            
    #         mammals_list= common_family(filename)
    #         names_count_list=[]
    #         for name in mammals_list:
    #               names_count_list.append(name.count())
                 
    #         index_max_num= names_count_list.index(max(names_count_list))
            
    #         return index_max_num, mammals_list
        
        
    #     def print_max_specie(self):
            
    #         results=count_mammals_list(filename)
    #         self.index,self.list_of_mammals=results
            
    #     def __str__(self):
            
    #         return f"The most common family of mammals is:{self.list_of_mammals[self.index]}"

# @classmethod
    # def load_species(cls, filename):
    #     all_species = []
    #     with open(filename, "r", encoding="utf8") as common:
    #         freader = csv.reader(common, delimiter=',', quotechar='"')
    #         for val in freader:
    #             # Ensure the number of values matches the number of parameters in __init__
    #             if len(val) == 12:
    #                 new_species = cls(*val)
    #                 all_species.append(new_species)
    #             else:
    #                 print(f"Skipping invalid row: {val}")

    #     return all_species

       

# filename = "species.csv"
# all_species = Species.load_species(filename)

# Now you can print or use the instances in some way
# for species_instance in all_species:
#     print(species_instance.__dict__)

# def common_family(self):
            
            
#     with open(filename,"r",encoding="utf8") as common:
#         freader = csv.reader(common,delimiter = ',',quotechar='"')
#         for f in freader:
#             f= f.strip("\n")                    
#             self.family_names.append(self.family)
#             self.order_names.append(self.order)
#         for order in range(len(self.order_names)):
            
#             if order=="Mammal":
#                 self.mammals_list.append(self.family_names[order])
#     return self.mammals_list
        
# def count_mammals_list(self):
    
#     mammals_list= common_family(filename)
#     names_count_list=[]
#     for name in mammals_list:
#           names_count_list.append(name.count())
         
#     index_max_num= names_count_list.index(max(names_count_list))
    
#     return index_max_num, mammals_list

        
# def print_max_specie(self):
    
#     results=count_mammals_list(filename)
#     self.index,self.list_of_mammals=results
    
#     def __str__(self):
        
#         return f"The most common family of mammals is:{self.list_of_mammals[self.index]}"

# if __name__ == "__main__":
    
#     filename="species.csv"
#     h= species(filename)



                        


                


    