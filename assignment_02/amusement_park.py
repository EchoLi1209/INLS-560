# This lesson covers that order matters when using elif in some situations.

age = 101

if age < 4:
    print("Admission is $0")
elif age < 18:
    print("Admission is $25")
elif age > 60:
    print("Admission is $35")

# this is not going to work here. put before age > 60
# elif age > 100:
#    print("Admission is $0 and you get a free beer!")
else:
    print("Admission is $40")
