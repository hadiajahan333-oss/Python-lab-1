def employee_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

employee_info(
    name="Ali",
    age=25,
    department="IT",
    salary=50000
)