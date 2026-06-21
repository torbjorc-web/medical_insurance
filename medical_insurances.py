class Patient:
    def __init__(self, name, age, sex, bmi, num_of_children, smoker):
        """Task 1: Constructor with all patient parameters"""
        self.name = name
        self.age = age
        self.sex = sex              # 0 for male, 1 for female
        self.bmi = bmi              # patient's BMI
        self.num_of_children = num_of_children  # number of children
        self.smoker = smoker        # 0 for non-smoker, 1 for smoker
    
    # Task 3 & 4: estimated_insurance_cost() method
    def estimated_insurance_cost(self):
        """Calculate and display patient's estimated yearly medical insurance costs"""
        estimated_cost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500
        print(f"{self.name}'s estimated insurance costs is {estimated_cost} dollars.")
        return estimated_cost
    
    # Task 5, 6, & 7: update_age() method
    def update_age(self, new_age):
        """Update patient's age and recalculate insurance costs"""
        self.age = new_age
        print(f"{self.name} is now {self.age} years old.")
        self.estimated_insurance_cost()
    
    # Task 8, 9, 10, & 11: update_num_children() method
    def update_num_children(self, new_num_children):
        """Update patient's number of children and recalculate insurance costs"""
        self.num_of_children = new_num_children
        
        # Control flow for correct grammar (child vs children)
        if self.num_of_children == 1:
            print(f"{self.name} has {self.num_of_children} child.")
        else:
            print(f"{self.name} has {self.num_of_children} children.")
        
        self.estimated_insurance_cost()
    
    # Task 12 & 13: patient_profile() method
    def patient_profile(self):
        """Return a dictionary containing all patient information"""
        patient_information = {
            "name": self.name,
            "age": self.age,
            "sex": self.sex,
            "bmi": self.bmi,
            "num_of_children": self.num_of_children,
            "smoker": self.smoker
        }
        return patient_information


# Task 2: Create and test patient1 instance
patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)

# Test all methods
print(patient1.name)
patient1.estimated_insurance_cost()
patient1.update_age(26)
patient1.update_num_children(1)
patient1.update_num_children(2)
print(patient1.patient_profile())
