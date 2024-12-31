import json

class Employee:
    def __init__(self, emp_id, name, department, working):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.working = working

    def terminate(self):
        self.working = False

    def is_working(self):
        return self.working


class EmployeeDatabase:
    @staticmethod
    def save_to_database(employee, file_path):
        data = {
            "id": employee.emp_id,
            "name": employee.name,
            "department": employee.department,
            "working": employee.working,
        }
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Employee data saved to {file_path}")


class EmployeeReport:
    @staticmethod
    def generate_xml(employee):
        report = f"""<Employee>
    <ID>{employee.emp_id}</ID>
    <Name>{employee.name}</Name>
    <Department>{employee.department}</Department>
    <Working>{employee.working}</Working>
</Employee>"""
        return report

    @staticmethod
    def generate_csv(employee):
        report = f"{employee.emp_id},{employee.name},{employee.department},{employee.working}"
        return report


if __name__ == "__main__":
    employee = Employee(emp_id=101, name="Alice", department="Engineering", working=True)

    print("Is Working:", employee.is_working())

    EmployeeDatabase.save_to_database(employee, "employee.json")

    xml_report = EmployeeReport.generate_xml(employee)
    print("\nXML Report:")
    print(xml_report)

    csv_report = EmployeeReport.generate_csv(employee)
    print("\nCSV Report:")
    print(csv_report)

    employee.terminate()
    print("\nAfter Termination - Is Working:", employee.is_working())
