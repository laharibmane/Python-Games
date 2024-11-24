
import csv

class CSVToolkit:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_csv(self):
        """Read and display content of the CSV file."""
        try:
            with open(self.file_name, mode='r') as file:
                reader = csv.reader(file)
                data = [row for row in reader]
                return data
        except FileNotFoundError:
            print(f"Error: {self.file_name} not found.")
            return []

    def write_csv(self, data, headers=None):
        """Write data to the CSV file. Overwrites existing content."""
        with open(self.file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            if headers:
                writer.writerow(headers)
            writer.writerows(data)
        print(f"Data written to {self.file_name} successfully.")

    def append_csv(self, rows):
        """Append rows to the CSV file."""
        with open(self.file_name, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print(f"Data appended to {self.file_name} successfully.")

    def search_csv(self, keyword):
        """Search for a keyword in the CSV file."""
        results = []
        data = self.read_csv()
        for i, row in enumerate(data):
            if any(keyword in cell for cell in row):
                results.append((i, row))
        return results

    def analyze_csv(self):
        """Provide basic analysis of the CSV content."""
        data = self.read_csv()
        if not data:
            print("No data to analyze.")
            return
        
        num_rows = len(data)
        num_columns = len(data[0]) if num_rows > 0 else 0
        print(f"Rows: {num_rows}, Columns: {num_columns}")

        column_lengths = [len([row[col] for row in data]) for col in range(num_columns)]
        print("Column-wise element counts:", column_lengths)

# Example Usage:
if __name__ == "__main__":
    toolkit = CSVToolkit("example.csv")

    # Writing data to a CSV file
    headers = ["Name", "Age", "City"]
    data = [["Alice", 25, "New York"], ["Bob", 30, "Los Angeles"], ["Charlie", 22, "Chicago"]]
    toolkit.write_csv(data, headers)

    # Reading and displaying content
    print("Content of CSV:", toolkit.read_csv())

    # Appending rows
    new_data = [["David", 28, "San Francisco"], ["Eve", 35, "Seattle"]]
    toolkit.append_csv(new_data)

    # Searching in the CSV
    keyword = "Alice"
    results = toolkit.search_csv(keyword)
    print(f"Search results for '{keyword}':", results)

    # Analyzing the CSV
    toolkit.analyze_csv()