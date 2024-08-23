from backend.google_search import get_google_search_links
from backend.scraper import run_scraper
from backend.data_processing import convert_csv_to_excel, convert_csv_to_json
from backend.database import store_data_to_db
from database.db_config import DatabaseConfig

def main():
    query = "ESG risks in bank investment portfolio"
    links = get_google_search_links(query)

    # Run scraper with enhanced features
    run_scraper(links)

    # Convert CSV to Excel and JSON
    convert_csv_to_excel("output/output.csv", "output/output.xlsx")
    convert_csv_to_json("output/output.csv", "output/output.json")

    # Store data in the database
    db_config = DatabaseConfig("database/esg_data.db")
    store_data_to_db("output/output.csv", db_config)

if __name__ == "__main__":
    main()
