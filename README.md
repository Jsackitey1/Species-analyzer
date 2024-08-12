## National Park Species Data Analysis

This project focuses on analyzing species data from the U.S. National Park Service, using datasets sourced from [NPSpecies](https://irma.nps.gov/NPSpecies/). The goal is to load and process the data, enabling in-depth analysis to answer key questions about biodiversity and conservation within national parks.

### Key Objectives:
- **Identify Parks with the Most Species per Area:** Analyze and rank national parks based on species density relative to their size.
- **Determine the Most Common Mammal Families:** Identify and report the most prevalent mammal families across different parks.
- **Assess Endangered Species:** Quantify and categorize endangered species in each park, broken down by conservation status.

### Project Structure:

- **Classes:**
  - **`Park` Class:**
    - Stores information about each park, including code, name, state, acreage, and species list.
    - Methods:
      - `species_by_area`: Calculates species density (species per 10,000 acres).
      - `most_common_family`: Identifies the most common family within a specified category.
      - `conservation_status_by_category`: Returns a count of species by conservation status for a given category.
  - **`Species` Class:**
    - Stores data for individual species, including ID, category, order, family, scientific name, common names, and conservation status.

- **Processing Script:**
  - **`nps_processor.py`:** 
    - Main script to read and process data from CSV files, create `Park` objects, and analyze the data.
    - Outputs the results to `nps_summary.txt`.

- **Testing:**
  - **`test_nps_processor.py`:** 
    - Contains unit tests to validate data processing and analysis using a sample test dataset (`test_species.csv`).

### Deliverables:
- **`nps_summary.txt`:** 
  - A summary file that contains the results of the analysis when run against the full dataset (`species.csv`).

### Getting Started:
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/you/nps-species-analysis.git
   ```
2. **Run the Analysis:**
   ```bash
   python nps_processor.py
   ```
3. **View Results:**
   - Check the `nps_summary.txt` file for the detailed analysis.

### Contributions:
Contributions and improvements are welcome! Feel free to open an issue or submit a pull request.
