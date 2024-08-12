# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 21:17:42 2023
This is a test function to test my nps_processor 
@author: duaha
"""
import nps_processor

def test_highest_species_park():
    #setting the value of my expected 
    expected = "Acadia National Park"
    #computing from the function 
    computed = nps_processor.highest_species_park()
    #setting my success variable 
    success = (expected == computed)
    #wrtiting a message to the user if the test fails 
    test_msg = f"Expected : {expected}, Computed : {computed}"
    #asserting my variables 
    assert success, test_msg
    

#defining my function
def test_most_fam_question():
    #setting my expected 
    #in the function I returned a list so this is the expected list 
    fam_expected = ['Cervidae', 'Antilocapridae', 'Antilocapridae', 'Antilocapridae',
                    'Cervidae', 'Antilocapridae', 'Antilocapridae', 'Antilocapridae', 
                    'Antilocapridae', 'Cervidae', 'Canidae', 
                    'Cervidae', 'Antilocapridae', 'Cervidae', 'Bovidae', 'Heteromyidae', 'Delphinidae', 
                    'Cervidae', 'Bovidae', 'Cricetidae', 'Bovidae', 'Camelidae', 'Antilocapridae',
                    'Antilocapridae', 'Cricetidae', 
                    'Antilocapridae', 'Antilocapridae', 'Bovidae', 'Bovidae',
                    'Cervidae', 'Cervidae', 'Bovidae', 'Cervidae', 'Bovidae', 'Bovidae', 'Bovidae', 'Cricetidae', 'Cervidae', 
                    'Antilocapridae', 'Bovidae', 'Bovidae', 'Bovidae', 'Sciuridae', 'Bovidae', 'Cervidae', 
                    'Antilocapridae', 'Vespertilionidae', 'Bovidae', 'Cervidae', 
                    'Antilocapridae', 'Cervidae', 'Sciuridae', 'Bovidae', 'Antilocapridae', 'Bovidae', 'Bovidae']
    
    #setting my computed variable and writing the code for it 
    fam_computed = nps_processor.most_com_family
    #setting my success variable and comparing the computed and expected 
    fam_success = (fam_expected == fam_computed)
    #writing a message to the user of the test function fails 
    fam_tst_message = f"Expected : {fam_expected}, Computed : {fam_computed}"
    #asserting my variables 
    assert fam_success, fam_tst_message
    
#defining my function   
def test_endagered_species():
    #setting my expected list 
    #since I returned a list for the function in the nps processor this is my expected list 
    endangered_expected = [3, 2, 2, 11, 13, 2, 2, 7, 6, 4, 24, 4, 4, 1, 0, 24,
                           5, 16, 0, 0, 9, 2, 11, 0, 13, 3, 2, 40, 44, 4, 2, 6,
                           6, 8, 0, 3, 6, 13, 6, 1, 3, 2, 4, 2, 21, 2, 1, 4, 4, 
                           3, 1, 3, 5, 2, 4, 5]
    
    
    #computing that list from my nps_processor 
    endangered_computed = nps_processor.species_endangered
    #setting my succes variable and comparing the computed and the expected 
    endangered_success = (endangered_expected == endangered_computed)
    #writing a message to the user if the test fails 
    endangered_tst_msg = f"Expected : {endangered_expected}, Computed : {endangered_computed}"
    #asserting my variables 
    assert endangered_success,endangered_tst_msg
    
#calling back my functions 
if __name__ == "__main__":
    test_highest_species_park()
        
    test_most_fam_question()
    
    test_endagered_species()

