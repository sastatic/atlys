# Atlys Assignment - Scraping Tool

## Introduction

This scraping tool is designed to automate the process of extracting product information from a target website. It scrapes product names, prices, and images from each page of the catalogue and stores the data in a local database. The tool is developed using Python's FastAPI framework and includes features such as configuration management, retry mechanism, authentication, notification, and caching.

## Functionalities

- **Scraping Functionality**:

  - Extracts product information like name, price, and image from each page of the catalogue.
  - Parses HTML content to extract the required data.
  - Supports configuration settings such as limiting the number of pages to scrape and providing a proxy string for scraping.

- **Configuration Management**:

  - Allows users to configure settings like the maximum number of pages to scrape and the proxy string to use for scraping.
  - Settings are adjustable through the tool's interface.

- **Data Storage**:

  - Stores scraped product information in a database for further processing.
  - Data is stored in a local JSON file, but the tool supports other storage strategies.

- **Retry Mechanism**:

  - Implements a retry mechanism in case of failed scraping requests.
  - Attempts the request again after a certain delay.

- **Authentication**:

  - Requires authentication for the API endpoint triggering the scraping process.
  - Uses a static token provided by the user for authentication.

- **Notification**:

  - Notifies designated recipients about the status of the scraping operation after each session.
  - Notifications can be as simple as printing a message in the console or sending an email.

- **Caching Mechanism**:
  - Optimizes performance by implementing a caching mechanism.
  - Does not update the data of products with unchanged prices in the database.

## Usage

1. Configure the scraping settings such as the maximum number of pages to scrape and the proxy string.
2. Trigger the scraping process using the provided API endpoint with authentication.
3. Monitor the scraping progress and receive notifications about the scraping status.
4. Access the scraped product information stored in the local database for further processing.

## Installation

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the scraping tool using `python main.py`.
4. Access the API endpoint for triggering the scraping process.

## Contributors

- Sarwar Ali
