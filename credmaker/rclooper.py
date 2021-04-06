#!/usr/bin/env python3

# import the csv library
# for more info., NOTE: https://docs.python.org/3/library/csv.html
import csv

# make f a file object, by reading csv_users.txt
f = open("csv_users.txt", "r")

# set i equal to 0. We're going to use this as a counter
i = 0

# Now we want to use the csv.reader() This function will read each line of the file in row. Row becomes a list, where each comma separated value becomes a new value in that list.
for row in csv.reader(f):

# Let's increment i by 1. This will appear at the end of our admin.rc file. Don't forget to indent 4 spaces.
    i = i + 1

# Now set filename equal to admin.rc%d. %d is a place holder for a digit, where the digit we want to apply is the value of i found at the end of this line of code. Don't forget to indent 4 spaces.
    filename = "admin.rc%d"%(i)

# Now make rcfile the open file object, filename, so we can write to it. Don't forget to indent 4 spaces.
    rcfile = open(filename, "w")

# Now write the value of OS_AUTH_URL to rcfile. We also want to write the value of row[0] which is the first value in the first row of csv_users.txt. Don't forget to indent 4 spaces.
    print("export OS_AUTH_URL=" + row[0], file=rcfile)


# Now just write the value of OS_IDENTITY_API_VERSION=3 to rcfile. Don't forget to indent 4 spaces.
    print("export OS_IDENTITY_API_VERSION=3", file=rcfile)

# Now write the value of OS_PROJECT_DOMAIN_NAME to rcfile. We also want to write the value of row[1] which is the second value within a row of csv_users.txt. Don't forget to indent 4 spaces.
    print("export OS_PROJECT_NAME=" + row[1], file=rcfile)

# Now write the value of OS_PROJECT_DOMAIN_NAME to rcfile. We also want to write the value of row[2] which is the third value within a row of csv_users.txt. Don't forget to indent 4 spaces.

    print("export OS_PROJECT_DOMAIN_NAME=" + row[2], file=rcfile)

# Now write the value of OS_USERNAME to rcfile. We also want to write the value of row[3] which is the fourth value within a row of csv_users.txt. Don't forget to indent 4 spaces.
    print("export OS_USERNAME=" + row[3], file=rcfile)

# Now write the value of OS_USERNAME_DOMAIN_NAME to rcfile. We also want to write the value of row[4] which is the fifth value within a row of csv_users.txt. Don't forget to indent 4 spaces.
    print("export OS_USER_DOMAIN_NAME=" + row[4], file=rcfile)

# Now write the value of OS_PASSWORD to rcfile. We also want to write the value of row[5] which is the sixth value within a row of csv_users.txt. Don't forget to indent 4 spaces.
    print("export OS_PASSWORD=" + row[5], file=rcfile)

# Now close the rcfile, as we've completed our first file. Memory will thank you, and the loop will repeat.
    rcfile.close()



