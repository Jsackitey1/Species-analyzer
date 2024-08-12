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
import unittest
import species
import parks
import csv
import os
import nps_processor as processor

class TestParkFunctions(unittest.TestCase):
    
    def setUp(self):
        
        with open("test_species.csv", "w", newline="", encoding="utf8") as species_file:
            species_writer = csv.writer(species_file)
            species_writer.writerow(["species_id", "common_names", "order", "family", "scientific_name", "conservation_status"])
            species_writer.writerow(["ACAD-1000", "Grizzly Bear", "Mammal", "Ursidae", "Ursus arctos horribilis", "Endangered"])
        
        with open("test_parks.csv", "w", newline="", encoding="utf8") as parks_file:
            parks_writer = csv.writer(parks_file)
            parks_writer.writerow(["code", "name", "state", "acres", "latitude", "longitude"])
            parks_writer.writerow(["ACAD", "Acadia", "Maine", "49075.26", "44.35", "-68.21"])
        
    def tearDown(self):
        
        os.remove("test_species.csv")
        os.remove("test_parks.csv")


    def test_load_species(self):
        
        all_species, park_codes = processor.load_species("test_species.csv")
        self.assertEqual(len(all_species), 1)
        self.assertEqual(len(park_codes), 1)
        self.assertEqual(all_species[0].species_id, "ACAD-1000")
        self.assertEqual(park_codes[0], "ACAD")
        
    def test_load_parks(self):
        
        all_parks, all_species = processor.load_parks("test_species.csv", "test_parks.csv")
        self.assertEqual(len(all_parks), 1)
        self.assertEqual(len(all_species), 1)
        self.assertEqual(all_parks[0].code, "ACAD")
        self.assertEqual(all_species[0].species_id, "ACAD-1000")
        
    def test_parks_with_most_species(self):
        
        park = parks.Parks("ACAD", "Acadia", "Maine", "49075.26", "44.35", "-68.21")
        park.species = [species.Species("ACAD-1000", "Grizzly Bear", "Mammal", "Ursidae", "Ursus arctos horribilis", "Endangered")]
        
        name, num_species = park.parks_with_most_species()
        self.assertEqual(name, "Acadia")
        self.assertEqual(num_species, 0.002040146709248742)
        
    def test_common_family(self):
        
        park = parks.Parks("ACAD", "Acadia", "Maine", "49075.26", "44.35", "-68.21")
        park.species = [species.Species("ACAD-1000", "Grizzly Bear", "Mammal", "Ursidae", "Ursus arctos horribilis", "Endangered")]
        common_families = park.common_family()
        self.assertEqual(common_families, {"ACAD-1000": "Ursidae"})
        
    def test_count_conservation_status(self):
        
        park = parks.Parks("ACAD", "Acadia", "Maine", "49075.26", "44.35", "-68.21")
        park.species = [species.Species("ACAD-1000", "Grizzly Bear", "Mammal", "Ursidae", "Ursus arctos horribilis", "Endangered")]
        counts = park.count_conservation_status()
        self.assertEqual(counts, {'Endangered': 1, 'Species of Concern': 0, 'Threatened': 0, 'Proposed Endangered': 0, 'Under Review': 0, 'In Recovery': 0})
        
if __name__ == '__main__':
    
    unittest.main()






