from pratice_11_3 import Employee
def test_give_default_raise():
   test_employee =  Employee("TongXin","Lu",6000)
   test_employee.give_raise()
   assert test_employee.salary == 11000

def test_give_custom_raise():
   custom_employee = Employee("TongXin","Lu",3000)
   custom_employee.give_raise(2000)
   assert custom_employee.salary == 5000