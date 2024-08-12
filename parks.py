# -*- coding: utf-8 -*-

"""
A program to analyze data from the National Park Service regarding the species found in the parks.

@author: Sackitey Joseph
"""

 
class Parks:
    
    def __init__(self, code, name, state, acres, latitude, longitude):
        
        self.code = code
        self.name = name
        self.state = state
        self.acres = acres
        self.latitude = latitude
        self.longitude = longitude
        self.species = []
        
    def __str__(self):
        
        park_data = f"{self.code}, {self.name}, {self.state}, {self.acres}, {self.latitude}, {self.longitude},{self.species}"
        return park_data
    
    
    def parks_with_most_species(self):
        
        """
        To calculatet he park with the most number of species per 10000 acres

        Returns
        -------
        TYPE :string
            name of park.
        TYPE: Int
            value of the max number of species per park .

        """
        
        
        self.max_park = None
        self.max_species_by_area = 0
    
        for park in self.species:
            if not park:
                continue
    
            number_of_species = len(self.species)
            self.species_by_area = (number_of_species / int(self.acres)) * 10000
    
            if self.species_by_area > self.max_species_by_area:
                self.max_species_by_area = self.species_by_area
                self.max_park = self.name
    
        return self.max_park, self.max_species_by_area

    
    
    def common_family(self):
        
        """
        To find the common family of mammals in each park

        Returns
        -------
        TYPE dictionary
            conataining the names and the park and the name of their corresponding common families of mammals.

        """
        
        
        self.common_families = {}
    
        mammals_list = []

        for specie in self.species:
            if specie.category == "Mammal":
                mammals_list.append(specie.family)

        if mammals_list:
            most_common_family = max(set(mammals_list), key=mammals_list.count)
            self.common_families[self.name] = most_common_family

        return self.common_families
    
    
    def count_conservation_status(self):
        
        """
        Count the number of species for each conservation status in each park
    
        Returns
        -------
        TYPE: dictionary
            containing the name of the park and the corresponding counts for each conservation status.
        """
        
        
        count_dict = {}
        status_counts = {'Endangered': 0, 'Species of Concern': 0, 'Threatened': 0, 'Proposed Endangered': 0, 'Under Review': 0, 'In Recovery': 0}

        for park in self.species:
            self.status = park.conservation_status
            
            if self.status in status_counts:
                status_counts[self.status] += 1
                count_dict[self.code] = status_counts
    
        return count_dict

    
    
        

