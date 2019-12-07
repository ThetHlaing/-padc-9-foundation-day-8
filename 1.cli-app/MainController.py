from Department import Department


class MainController:

    @staticmethod
    def addNewDepartment():

        deparment = Department()
        deparment.name = input("Please enter the department name : ")
        deparment.save()
