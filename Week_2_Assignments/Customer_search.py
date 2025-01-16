import csv
import json

class Customer:
    def __init__(self, customer_id, company_name, contact_name, country):
        self.customer_id = customer_id
        self.company_name = company_name
        self.contact_name = contact_name
        self.country = country

    def to_customer_dict(self):
        return {
            "CustomerID": self.customer_id,
            "CompanyName": self.company_name,
            "ContactName": self.contact_name,
            "Country": self.country
        }

class CustomerSearch:
    def __init__(self, db):
        self.db = db

    def search_by_country(self, country):
        return [
            customer
            for customer in self.db
            if country.lower() in customer.country.lower()
        ]

    def search_by_company_name(self, company):
        return [
            customer
            for customer in self.db
            if company.lower() in customer.company_name.lower()
        ]

    def search_by_contact(self, contact):
        return [
            customer
            for customer in self.db
            if contact.lower() in customer.contact_name.lower()
        ]


class CustomerReport:
    @staticmethod
    def export_to_csv(data, file_path):
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["CustomerID", "CompanyName", "ContactName", "Country"])
            for customer in data:
                writer.writerow(
                    [customer.customer_id, customer.company_name, customer.contact_name, customer.country]
                )
        print(f"Data exported to {file_path}")

    @staticmethod
    def export_to_json(data, file_path):
        with open(file_path, mode='w') as file:
            json_data = [customer.to_customer_dict() for customer in data]
            json.dump(json_data, file, indent=4)
        print(f"Data exported to {file_path}")


if __name__ == "__main__":
    database = [
        Customer(1, "Company A", "Alice", "USA"),
        Customer(2, "Company B", "Bob", "Canada"),
        Customer(3, "Company C", "Charlie", "USA"),
        Customer(4, "Company D", "David", "UK"),
    ]

    search = CustomerSearch(database)

    results = search.search_by_country("USA")
    print(f"Found {len(results)} customers in the USA.")

    report = CustomerReport()
    report.export_to_csv(results, "customers_in_usa.csv")

    report.export_to_json(results, "customers_in_usa.json")
