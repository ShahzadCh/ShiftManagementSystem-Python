from worker import Worker
#from week import Week

worker_list = ["Shaz", "Umar", "Kabir"] #temporarily fixed for testing purpose

fname = input("Enter the week number (e.g. Week1) to create/update shifts for that week: ")
for each in worker_list:
    items =Worker(each)

    items.set_quota()
    items.set_shifts()
    items.send_to_file(fname)


