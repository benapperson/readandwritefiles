with open("EmployeePay.csv", encoding="utf-8") as employeepay:

    for line in employeepay:

        print(line[:-1])
