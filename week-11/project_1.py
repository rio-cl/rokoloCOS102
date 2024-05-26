import pandas as pd

df = pd.read_csv("SIS.csv")


class Category:
    def __init__(self):
        self.pirates = {'MatNo': [], 'Name': [], 'Age': [], 'Grade': []}
        self.yankees = {'MatNo': [], 'Name': [], 'Age': [], 'Grade': []}
        self.bulls = {'MatNo': [], 'Name': [], 'Age': [], 'Grade': []}
        self.encaps = {'MatNo': [], 'Name': [], 'Age': [], 'Grade': []}
        self.error_message = ""

    def checker(self, matno, name, age, grade):
        if 14 < age <= 18:
            self.pirates['MatNo'].append(matno)
            self.pirates['Name'].append(name)
            self.pirates['Age'].append(age)
            self.pirates['Grade'].append(grade)
        elif 18 < age <= 22:
            self.yankees['MatNo'].append(matno)
            self.yankees['Name'].append(name)
            self.yankees['Age'].append(age)
            self.yankees['Grade'].append(grade)
        elif 22 < age <= 25:
            self.bulls['MatNo'].append(matno)
            self.bulls['Name'].append(name)
            self.bulls['Age'].append(age)
            self.bulls['Grade'].append(grade)
        elif age > 25:
            self.encaps['MatNo'].append(matno)
            self.encaps['Name'].append(name)
            self.encaps['Age'].append(age)
            self.encaps['Grade'].append(grade)
            self.error_message = "You do not meet any of the age requirements."
            print(self.error_message)
        else:
            self.error_message = "You do not meet any of the age requirements."
            print(self.error_message)

    def get_error_message(self):
        return self.error_message

    def save_to_csv(self):
        pd.DataFrame(self.pirates).to_csv('The_Pirates.csv', index=False)
        pd.DataFrame(self.yankees).to_csv('The_Yankees.csv', index=False)
        pd.DataFrame(self.bulls).to_csv('The_Bulls.csv', index=False)


# Create an instance of Category
obj = Category()

# Iterate over the DataFrame rows and categorize each student
for i, j in df.iterrows():
    obj.checker(j['MatNo'], j['Name'], j['Age'], j['Grade'])

obj.save_to_csv()
