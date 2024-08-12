# -*- coding: utf-8 -*-

"""
A program to analyze data from the National Park Service regarding the species found in the parks.

@author: Sackitey Joseph
"""

class Species:
    def __init__(self, species_id, category, order, family, scientific_name, common_names, record_status, occurrence, nativeness, abundance, seasonality, conservation_status):
        self.species_id = species_id
        self.category = category
        self.order = order
        self.family = family
        self.scientific_name = scientific_name
        self.common_names = common_names
        self.record_status = record_status
        self.occurrence = occurrence
        self.nativeness = nativeness
        self.abundance = abundance
        self.seasonality = seasonality
        self.conservation_status = conservation_status
        
        
        