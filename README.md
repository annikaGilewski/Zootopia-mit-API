# Zootopia with API

Zootopia with API is a Python project that retrieves animal information from the API Ninjas Animals API and displays it on a generated HTML webpage.

Users can enter the name of an animal and view information such as its diet, location, and type. If no animal is found, the website displays an appropriate message.

### Features
* Retrieve animal data from an external API.
* Generate an HTML webpage displaying animal information.
* Display the animal's diet, location, and type when available.
* Show an error message if the API request fails.
* Inform the user when no matching animal is found.
* Store the API key in a .env file instead of directly in the Python code.

### Requirements
* Python 3
* An API key from API Ninjas
* The Python packages listed in requirements.txt

### Installation
1. Clone this repository:
git clone YOUR_REPOSITORY_URL
2. Navigate to the project directory:
cd Zootopia-mit-API
3. Install the required packages:
pip install -r requirements.txt 
4. Create a .env file in the root directory and add your API key:
API_KEY=your_api_key_here
Replace your_api_key_here with your own API Ninjas API key.

### Usage
Run the following command from the project directory:
python animals_web_generator.py
Enter the name of an animal when prompted.
The program retrieves the animal data from the API and generates an animals.html file. Open this file in your browser to view the results.
If no matching animal is found, the webpage displays a corresponding message.

### Project Structure
Zootopia-mit-API/
* ├── animals_web_generator.py
* ├── data_fetcher.py
* ├── animals_template.html
* ├── requirements.txt
* ├── .env
* ├── .gitignore
* └── README.md

### Security
The API key is stored in a local .env file. This file should not be committed to Git or uploaded to GitHub.