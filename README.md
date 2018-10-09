# ion
automating newsletters, first iteration, mostly for clubs at ucsd who want to reach their members.

to make your own you will need mail.py along with three files: config.py, addresses.py, and login.py

config.py can contain anything you want, for now it contains:
1. ``` subject = 'some subject' ```
2. ``` message = 'some message' ```

address.py **must** contain a list of strings with destination emails and a source address
1. ```emails = ['email@gmail.com', 'email2@ucsd.edu']```
2. ```sourceAddress = 'source@ucsd.edu'```

login.py **must** have USERNAME and PASSWORD variables
where USERNAME is just the email without the @someEmailProvider.com

1.```USERNAME = 'source'```
2.```PASSWORD = 'super secret password'```

----

at the very least, if a club wants to make their own newsletter and they log on to their .edu email through gmail the smtp server is most likely **_not_** gmail. It is probably maintained by the university, ex: smtp.universityNameHere.edu


