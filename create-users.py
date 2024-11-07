#!/usr/bin/python3
#### Henok Tekle
#### Create-Users.PY
#### Program Creation Date: 11/6/2024
#### Program Last Updated Date: 11/6/2024

#these imports are being used to interact with the operating system, using regular expressions to pattern match, and to interact with the system.
import os
import re
import sys

def main():
    for line in sys.stdin:

        #this "regular expression" is searching for the presence of a # because they are comments so they can be skipped.
        match = re.match("^#",line)

        print("The contents of the match variable were: ", match)

        #this field seperates the lines into a list format and strips the line of whitespace.
        fields = line.strip().split(':')

        print("Length of Fields was: ", len(fields))
        #If the line doesn't have 5 fields skip it.
        #If the IF statement evaluates to true then the continue will skip the rest of the loop.
        #This IF statement relies on what happened in the prior two lines of code by using match to detect the fields.
        if match or len(fields) != 5:
            continue

        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])
        groups = fields[4].split(',')
        print("==> Creating account for %s..." % (username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)
        #print cmd
        os.system(cmd)
        print("==> Setting the password for %s..." % (username))
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)
        #print cmd
        os.system(cmd)

        for group in groups:
            #this if statement checks that the group name is not `-`.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                os.system(cmd)

if __name__ == '__main__':
    main()
