import re

class Worker:
    """Worker class (at the moment) creates a new worker.
    The attributes of worker will be his name (a must required argument),
    a list of his shifts (without any mapping to respective week numbers yet),
    and his quota/limit (not yet utilized)"""

    def __init__(self, worker_name):
        self.name = worker_name
        self.shifts = list()
        self.quota = None
        self.total_hours = int(0)

    def set_quota(self):
        self.quota = int(input("Enter the max. number of hours " + self.name + " is allowed to work in a week: "))


    def shift_hour_counter(self, ask):

        hours = (re.findall('\d+', ask))

        shift_hours= (int(hours[1]) - int(hours[0]))
        return int(shift_hours)

    def set_shifts(self):
        """This function will just prompet the user to enter shifts of the current worker for the current week and store them in self.shifts"""
        days=('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

        for each in days:
            print("Enter ", self.name,"'s shift for ", each, " ")
            ask = input()
            self.shifts.append(ask)
            if ask == "-":
                pass
            else:
                self.total_hours += self.shift_hour_counter(ask)

        #Appending the allowed quota hours, it will show up under the heading "Allowed Hrs."
        self.shifts.append(self.quota)
        # Appending the total_hours below so that it comes against its heading "Actual Hrs."
        self.shifts.append(self.total_hours)
        if self.total_hours > self.quota:
            self.shifts.append("Doing " + str(self.total_hours - self.quota) + " more hours")


    def send_to_file(self, fname):

        """Checks whether a file for current week exists,
        if file doesn't exist: then calls function "create_new_file()

        if file exists: then checks whether current worker's name/shifts exist in the current week's file.

        If current worker's shifts don't exists, then calls "update_existing_file()" to simply append to existing file
        Otherwise calls "update_file_version()" to create a new file with all data from old file, except current worker"""

        # A better way would by to import "os" and then check if "os.path.exists(filename)" exists
        # For now, I have instead decided to use the try-except block

        try:
            with open(fname+ ".txt", "r") as infile:

                flag = False
                for line in infile:
                    if line.split()[0] == self.name:
                        flag = True
                        break
                if flag == True:
                    self.update_file_version(fname)
                else:
                    self.update_existing_file(fname)

        except IOError:
            self.create_new_file(fname)

    def create_new_file(self, fname):
        print("********CREATE NEW FILE********")
        print("Shifts of", fname, "do not exist as a file. \nCreating new file..." )
        headings = ('Names', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Allowed Hrs', 'Actual Hrs', 'Comment')
        with open(fname+ ".txt", "w") as file:
            for each in headings: file.write(each + "\t\t")
            file.write("\n" + self.name + "\t\t")
            for each in self.shifts: 
                file.write(str(each) + "\t\t")

        print("\nA new file has been created with the name",fname, "\n")

    def update_existing_file(self, fname):
        print("********UPDATE EXISTING FILE********")
        print("\nShifts of", self.name, "does not exist in the file", fname, "...Updating existing file")
        with open(fname+ ".txt", "a") as file:
            file.write("\n" + self.name + "\t\t")
            for each in self.shifts:
                file.write(str(each) + "\t\t")

        print("\nThe file", fname, "has been updated and now includes shifts of", self.name, "as well\n")

    def update_file_version(self, fname):
        print("********UPDATE FILE VERSION********")

        print("\nTo update ", self.name, "'s shifts in the current week, system needs to create a new file")
        print("Shifts of all other workers will be automatically copied to the new file")
        new_name = input("\nEnter the name of new file, recommended name is \"" + fname + "_v1\" :")

        with open(fname+ ".txt", "r") as infile:
            with open(new_name+ ".txt", "a") as outfile:

                for line in infile:
                    if line.split()[0] != self.name:
                        outfile.write(line)
                outfile.write(self.name + "\t\t")
                for each in self.shifts:
                    outfile.write(str(each) + "\t\t")

        print("\nAn updated version of the original file", fname, "is created with a new name", new_name, "\n")
        fname = new_name #filename updated for future use

		
    def convert_file_to_xsls(self):
        #This function should open the current shift's file and use its data to create another excel sheet file.
        #The calculation of many formulas (e.g. counting total hours of each worker) can also be set while creating
        #this file by adding different formulas. Modules like "xslxwriter" could be utilized for this purpose.
        pass
