from twitter_scraper import Scraper

scrap = Scraper(format="csv")

scrap.scrape(filepath="C:/Users/utilisateur/Documents/3 - PROJETS/Brief_Cyber_detective/twitter/Thief.csv",
             query="The Book Thief", results_count=5000, language="en")
