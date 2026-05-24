class Employee:
    language = "Python" # class attribute
    salary = 300000
 
Ahin.language= "JavaScript" # it's an instance attribute
print(Ahin.salary, Ahin.language)

# instance attribute , take preference over class attribute during assignment & retrival
# that's why we'll get language in output as JavaScript
