class Patient:
    def __init__(self, name:str, bill_amount:float):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def set_name(self, new_name:str):
        self.__name = new_name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, new_bill_amount:float):
        if new_bill_amount >= 0:
            self.__bill_amount = new_bill_amount
        else:
            print("Bill amount cannot be negative.")

    def calculate_bill(self):
        return self.__bill_amount

class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.8

class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85
    
regular_patient = Patient("Juan Dela Cruz", 15000)
senior_patient = SeniorPatient("Maria Santos", 15000)
philhealth_patient = PhilHealthPatient("Pedro Reyes", 15000)

print("Hospital Billing System")
print("-----------------------")

print(f"Patient Name: {regular_patient.get_name()}")
print(f"Original Bill: ₱{regular_patient.get_bill_amount():,.2f}")
print(f"Final Bill: ₱{regular_patient.calculate_bill():,.2f}")
print("")

print(f"Senior Patient Name: {senior_patient.get_name()}")
print(f"Original Bill: ₱{senior_patient.get_bill_amount():,.2f}")
print(f"Final Bill: ₱{senior_patient.calculate_bill():,.2f}")
print("")

print(f"PhilHealth Patient Name: {philhealth_patient.get_name()}")
print(f"Original Bill: ₱{philhealth_patient.get_bill_amount():,.2f}")
print(f"Final Bill: ₱{philhealth_patient.calculate_bill():,.2f}")