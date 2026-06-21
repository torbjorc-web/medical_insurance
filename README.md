Medical Insurance Project
This project uses a Python Patient class to store patient information, update patient data, and estimate yearly medical insurance costs.

What It Does
Stores patient details such as name, age, sex, BMI, number of children, and smoking status.

Updates patient information with class methods.

Calculates estimated yearly medical insurance costs.

Returns patient data as a dictionary.

Insurance Cost Formula
The estimated insurance cost is calculated using this formula:

estimated_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

Methods
__init__(name, age, sex, bmi, num_of_children, smoker)

estimated_insurance_cost()

update_age(new_age)

update_num_children(new_num_children)

patient_profile()

Example Usage
python
patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)
print(patient1.name)
patient1.estimated_insurance_cost()
patient1.update_age(26)
patient1.update_num_children(1)
print(patient1.patient_profile())
Purpose
This project is a beginner-friendly example of using Python classes to organize data and make code more reusable.
