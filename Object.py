from datetime import *
class Worker(object):

    def __init__(self, cc, lastName, dateIn):
        self.cc = cc
        self.lastName = lastName
        self.dateIn = dateIn

    def __str__(self):
        dd = str(self.dateIn.day)
        mm = str(self.dateIn.month)
        aa = str(self.dateIn.year)
        return "%s %s %s"%("\nCC: "+self.cc,"\nApellido: "+self.lastName,"\nFecha de ingreso: "+dd+"/"+mm+"/"+aa)

    def calcSalary(self):
        pass

class PersonnelHired(Worker):
    def __init__(self, cc, lastName, dateIn, salary):
        Worker.__init__(self, cc, lastName, dateIn)
        self.salary=salary 

    def calcSalary(self):
        dateCurrent = date.today()
        yearsIn = dateCurrent.year-self.dateIn.year
        if self.dateIn.month>dateCurrent.month or (
                self.dateIn.month == dateCurrent.month and
                    self.dateIn.day > dateCurrent.day):
            yearsIn -= 1
        if yearsIn <= 3:
            salaries = float(self.salary + (self.salary * 0.05))
        elif yearsIn > 3 and yearsIn <= 7:
            salaries = float(self.salary + (self.salary * 0.1))
        elif yearsIn > 7 and yearsIn <= 15:
            salaries = float(self.salary + (self.salary * 0.15))
        else:
            salaries = float(self.salary + (self.salary * 0.2))
        return salaries

    def __str__(self):
        return "%s %s"%(str(super(PersonnelHired, self).__str__()), "\nSueldo: "
                        + str(self.calcSalary()) + "Pesos\n")


class PersonneReply(Worker):
    def __init__(self, cc, lastName, dateIn, attended):
        Worker.__init__(self, cc, lastName, dateIn)
        self.attended = attended

    def calcSalary(self):
        salaries = int(self.attended * 50000)
        return salaries

    def __str__(self):
        return "%s %s"%(str(super(PersonneReply, self).__str__()),"\nSueldo: "
                        + str(self.calcSalary()) + " Pesos\n")