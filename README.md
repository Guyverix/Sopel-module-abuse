# Sopel-module-abuse

## Configuration:
The abuse file must be defined in the default.cfg file.
Here is an example config entry.

[abuse]

abuse_text = /home/user/.sopel/abuse.txt


## Installation:
Copy the abuse.py file into your modules directory after editing the default.cfg file.
chown the file to whatever userid is running your sopel daemon
and if necessary chmod 664 the abuse.py file to make sure that it can be read easily.

The same goes for the abuse.txt file.  It should also be chmodded and chowned whereever
you decide to put it.  It is important to note that there is the ability to add new
abuse to the file from IRC, so there will need to be sufficient privileges given to the 
file so Sopel can append to the file.

Reload sopel inside IRC and confirm that it picked up the changes by issuing
.help abuse   * the period is the default trigger, yours may be different.

## Operation:
### In channel:
.abuse userid

This will cause YOUR userid to abuse the victim

### In private to Sopel:
.abuse userid #channel

This will cause a RANDOM userid to abuse the victim :)

.add_abuse String of text

This will append "String of text" to the end of the abuse file

You must remember however that within "String of text" there is a variable VICTIM that 
must be spelled correctly and exist for the abuse to make sense.  If you miss VICTIM 
or miss-spell it, then the abuse will look kinda silly.

Remember you are NOT making complete sentences.

### Valid example:
is going to smack VICTIM over the head with a trout!

### Invalid examples:
Sopel is going to smack VICTIM over the head with a trout!
I am goign to smack <userid> over the head with a trout!
You falls over somebody.
VICTIM falls over somebody.

You must remember the acceptable sentence format:

<somebody> string VICTIM string


## Notes:
If Sopel does not pick up the new module with a reload, then a full  restart of the 
daemon will likely be necessary.

Editing abuse.txt file on the fly is fine, as Sopel opens the file
for every new abuse, so changes are automatically added to the system
even if they were not added via the .add_abuse option.

I have attempted to add debug logic into the script if people
have trouble and need to find the source of the problem. 

Simply uncomment the stuff that says DEBUG in it, and make sure
to watch your indents so that Sopel / Python does not complain.
Then comment them out again when you are done.

I am still learning Python, if you see oddball stuff it is likely due 
to me not knowing better, not me attempting to be tricky.


## Creator Etc section:
* Created by: Chris Hubbard
* Contact: guyverix@yahoo.com
* Created on: 02-02-2016
* Version: 0.1.0

An abuse module is nothing new under the sun.  Likely I have been influenced by different ones 
I have seen over the years.  I am sure that there are some that are more fully fleshed out
but this one does what I like, as I am attempting to learn Python and this seemed like an 
interesting small project.  Any suggestions on improvments would be greatly appreciated
as I already know that the system needs some better error correcttion in place, and some
additional meat on its bones.  

