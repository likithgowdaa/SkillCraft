import requests
from bs4 import BeautifulSoup
import csv

URL = "https://books.toscrape.com/"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def scrape_products(url):
    """Scrape product information from the e-commerce website."""

    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    products = []

    for product in soup.select("article.product_pod"):
        name = product.select_one("h3 a")["title"]
        price = product.select_one(".price_color").text.strip()
        availability = product.select_one(".availability").get_text(strip=True)

        rating_element = product.select_one("p.star-rating")
        rating = rating_element.get("class")[1] if rating_element else "Unknown"

        products.append({
            "Product Name": name,
            "Price": price,
            "Rating": rating,
            "Availability": availability
        })

    return products


def save_to_csv(products, filename="products.csv"):
    """Save scraped product information to a CSV file."""

    if not products:
        print("No products found.")
        return

    fieldnames = products[0].keys()

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(products)

    print(f"\nData successfully saved to {filename}")


def main():
    print("===== E-commerce Web Scraper =====")
    print(f"Website: {URL}")

    try:
        products = scrape_products(URL)

        print(f"\nProducts found: {len(products)}")

        for product in products:
            print("\n-----------------------------")
            print(f"Product: {product['Product Name']}")
            print(f"Price: {product['Price']}")
            print(f"Rating: {product['Rating']}")
            print(f"Availability: {product['Availability']}")

        save_to_csv(products)

    except requests.RequestException as error:
        print(f"Error accessing website: {error}")

    except Exception as error:
        print(f"An unexpected error occurred: {error}")


if __name__ == "__main__":
    main()
