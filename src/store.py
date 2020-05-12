"""
python3 store.py
ex.:
The Dugout
    1. Running
    2. Baseball
    3. Basketball
    4. Exit
Select the number of a department

Attributes:
- name
- department

Optional extra attributes:
- Store hours
- Store capacity
"""

class Store:
    # hours = 12

    def __init__(self, name, departments):
        self.name = name
        self.departments = departments


##  For readability
    def __str__(self):
        output = ""

        output += self.name + "\n"

        for department in enumerate(self.departments):
            output += str(index+1) + ". " + department + "\n"

        output += len (self.departments)

##  Used for debugging
   # def __repr__(self):
   #     return (f"Store name is {self.name}")


store = Store("The Dugout", ["Running", "Baseball", "Basketball"])

print(store)  # <__main__.Store object at 0x032D81D8> : show storage location in memory

