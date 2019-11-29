from worker import Worker
#from week import Week

shah = Worker("Shahzad")
ali = Worker("Ali")
kabir = Worker("Kabir")

#TRY UNCOMMENTING THE SET.SHIFTS() AND SEND_TO_FILE() FOR ONE PERSON ONLY, THEN FOR ALL 3 GIVING THE SAME FILE NAME

shah.set_quota()
shah.set_shifts()
#ali.set_shifts()
kabir.set_shifts()

#If I attempt to change an odd shift (like every other shift stays the same, but change Friday's shift) of a worker
# which has existing shifts in the same week,
#I can also change a worker's shifts list into a list which stores dictionaries, so that I can change only individual
#day by using its key, instead of having to enter the whole week again.
#the problem is list are unordered, but then I can store/export them in a file by calling the keys in a fixed order from Mon-Sun.

shah.send_to_file()
#ali.send_to_file()
kabir.send_to_file()