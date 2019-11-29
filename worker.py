class Worker:
    """Worker class is currently the class to create a new worker
    The attributes of worker will be his name (a must required argument),
    a list of his shifts (without any mapping to week number yet),
    and his quota/limit (not yet utilized)"""
	
	#TEST COMMENT	
    def __init__(self, worker_name):
        self.name = worker_name
        self.shifts = []
        self.quota = None

    def set_quota(self):
        self.quota = input("Enter the max. number of hours " + self.name + " is allowed to work: ")

    def set_shifts(self):
        """This function will just prompet the user to enter shifts of the current worker for the current week and store them in self.shifts"""
        days=('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
        ##days are deliberately made as a set, instead of a list. They will be frozen/locked anyway so why not use a set
        for each in days:
            print("Enter ", self.name,"'s shift for ", each, " ")
            ask=input()
            self.shifts.append(ask)


    #def get_shifts(self):
        #return (self.shifts) #I can actually directly use self.shifts when needed.

    def send_to_file(self):
        """Checks whether a file for current week exists,
        if file doesn't exist: then calls function "create_new_file()

        if file exists: then checks whether current worker's name/shifts exist in the current week's file.

        If current worker's shifts don't exists, then calls "update_existing_file()" to simply append to existing file
        Otherwise calls "update_file_version()" to create a new file with all data from old file, except current worker"""

        fname = input("Enter the week number to create/update the file and shifts of " + self.name + ": ")

        ##I can do that by importing "os" and then checking if "os.path.exists(filename)" exists
        ##I have decided to use try-except block to check if file exists already or not
        ##file = open(filename, "a")
        try:
            with open(fname+ ".txt", "r") as infile:

                ##Checking if current worker already has some shifts in current week.
                ##If YES, then create the new file to be able to delete worker's previously entered shifts by calling update_file_version
                ##Otherwise append this existing file by calling "update_existing_file()" function.
                flag = False
                for line in infile:
                    if line.split()[0] == self.name:
                        flag = True
                        # current worker's old(unwanted) entry exists already, new version of the file should be created
                        break
                if flag == True:
                    self.update_file_version(fname)
                else:
                    #flag==False meaning current worker has no previous shift in current week, so existing file can be updated
                    self.update_existing_file(fname)

        except:
            #means the try part could not find current week's file, so no file exists, create one from scratch.
            self.create_new_file(fname)

    def create_new_file(self, fname):
        print("********CREATE NEW FILE********")
        print("Shifts of ", fname, " do not exist \nCreating new file" )
        days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
        with open(fname+ ".txt", "w") as file:
            for each in days: file.write("\t" + each)
            file.write("\n")
            file.write(self.name + "\t")
            for each in self.shifts:
                file.write(str(each) + "\t")
            file.write("\n")

    def update_existing_file(self, fname):
        print("********UPDATE EXISTING FILE********")
        with open(fname+ ".txt", "a") as file:
            file.write(self.name + "\t")
            for each in self.shifts:
                file.write(str(each) + "\t")
            file.write("\n")

    def update_file_version(self, fname):
        print("********UPDATE FILE VERSION********")

        print("To update ", self.name, "'s shifts in the current week, system needs to create a new file")
        print("Shifts of all other workers will be automatically copied to the new file")
        name = input("Enter the name of new file, recommended name is \"" + fname + "_v1\" ")
        # TROUBLE: what if same person's shifts were added for the third time meaning that there
        # was already a filname.1.txt?

        with open(fname+ ".txt", "r") as infile:
            with open(name+ ".txt", "a") as outfile:

                for line in infile:
                    if line.split()[0] != self.name:
                        outfile.write(line)
                outfile.write(self.name + "\t")
                for each in self.shifts:
                    outfile.write(str(each) + "\t")
                outfile.write("\n")