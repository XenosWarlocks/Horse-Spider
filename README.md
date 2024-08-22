# Horse-Scraping
Horse Scraper is a Python-based project designed to perform Google searches, extract links from the search results, and scrape the content from those links. The project uses Selenium for simulating human-like interactions to avoid being flagged as a bot. The scraped data can be exported in multiple formats, such as CSV, JSON, and Excel.

## Authors

- [@octokatherine](https://www.github.com/octokatherine) really helped me pick the name for this project; otherwise, I wouldn't have started this project.
- [@XenosWarlocks](https://www.github.com/XenosWarlocks) 


## Features

- Perform Google searches and extract URLs from the results.
- Handle pagination to scrape multiple pages.
- Simulate human interactions (e.g., delays, mouse movements) to avoid bot detection.
- Scrape content from the extracted URLs.
- Export the scraped data to CSV, JSON, or Excel.
- Store scraped data in a database.

## Installation

### Prerequisites

- Python 3.8 or higher
- Google Chrome (latest version)
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) (compatible with your Chrome version)

### Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/Horse-Scraping.git
   cd Horse-Scraping
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
   
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```


### Usage
**Running the Scraper**
   ```bash
   python __main__.py
   ```

### Structure
Horse-Spider/
├── backend/
│   ├── __init__.py
│   ├── google_search.py       # Handles Google search and link extraction
│   ├── scraper.py             # Scrapes content from extracted links
│   └── data_processing.py     # Converts scraped data to CSV, JSON, or Excel
│   └── database.py            # Handles storing data into the database
├── database/
│   └── db_handler.py          # Handles data storage in a database
├── output/                    # Directory where output files are stored
│   ├── data.csv
│   ├── data.json
│   └── data.xlsx
└── __main__.py                # Main script to run the entire process

