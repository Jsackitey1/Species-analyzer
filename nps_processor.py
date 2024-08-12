# -*- coding: utf-8 -*-
"""
A program to analyze data from the National Park Service regarding the species found in the parks.

@author: Sackitey Joseph

"""

import species, parks,csv

def load_species(filename1):
    """
    To load the species from the csv file into the program

    Parameters
    ----------
    filename1 :string
        string name of the speceis.csv file to be read from.

    Returns
    -------
    all_species : list
        list of all the species.
    park_codes : list
        list of the codes of each park.

    """
    all_species = []
    park_codes = []

    with open(filename1, "r", encoding="utf8") as common:
        freader = csv.reader(common, delimiter=',', quotechar='"')
        
        for val in freader:
            e = species.Species(val[0],val[2], val[3], val[4], val[5], val[6], val[7], val[8], val[9], val[10], val[11],val[12])
            all_species.append(e)

        park_codes = [i.species_id[:4] for i in all_species]

    return all_species, park_codes



def load_parks(filename1, filename2):
    """
    To load the parks into the data and extend it with the corresponding species data

    Parameters
    ----------
    filename1 : string
        name of the species.csv file.
    filename2 : string
        name of the parks.csv file.

    Returns
    -------
    all_parks : list
        list of all the parks.
    all_species : list
        list of all the species.

    """
    
    all_parks = []
    all_species, park_codes = load_species(filename1) 
    del all_species[0] 
    
    with open(filename2, "r", encoding="utf8") as myparks:
        preader = csv.reader(myparks, delimiter=',', quotechar='"')
        next(preader)
        
        for val in preader:
            e = parks.Parks(val[0], val[1], val[2], val[3], val[4], val[5])
            all_parks.append(e)
        
        for val in all_parks:
            associated_species = [species_instance for species_instance in all_species if species_instance.species_id.startswith(val.code)]
            val.species.extend(associated_species)
                    
        
    return all_parks, all_species
        
         
def main():
    
    
    """
    Main program to write data to the text file

    Returns
    -------
    None.

    """
    
    filename1 = "species.csv" 
    filename2 = "parks.csv"  
    all_parks,all_species = load_parks(filename1, filename2)
    with open("nps_summary.txt", "w") as outputfile:
                
        list_1=[]
        list_2=[]
        for park in all_parks:
            a,b = park.parks_with_most_species()
            
            list_1.append(b)
            list_2.append(a)
        
        max_value=max(list_1)
               

        for i,z in zip(list_1,list_2):
            
            if i== max_value:
                outputfile.write(f"Park with Most Species by area of 10000 acres:\t{z}\nNumber of Species per Area in {z}:\t{i:.2f}\n")
        outputfile.write("\n")
       
        outputfile.write("Parks and their corresponding common species\n") 
        
        for park in all_parks:
            common_families = park.common_family()
        
            for category, name in common_families.items():
                outputfile.write(f"{category}:\t {name}\n")
    
                break  
            
        outputfile.write("\n")
        outputfile.write("Number of endangered species by category in each park\n")  
        
        for park in all_parks:    
            results= park.count_conservation_status()
            
            for category,name in results.items():
                outputfile.write(f"{category}: \t{name}\n")

        
        
if __name__ == "__main__":
    
    main()

