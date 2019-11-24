from time import localtime, strftime


def welcome(scheduled):
    return """\
                                         /\   /\\
 +-+-+-+-+-+-+-+-+-+-+-+-+ +-+-+-+      / 4'.'0 \\
 |S|l|a|s|h|R|o|o|t|C|T|F| |4|.|0|     / .o\  ...\\
 +-+-+-+-+-+-+-+-+-+-+-+-+ +-+-+-+    /.'  |\ | '. o____
            __                        '    |_\|    |____|
            \ \___      _   %s-%s-%s     |_|<o>  |
          .--""___\..--"/    %s:%s:%s      |_| |   |
      .__.|-"'"..... ' /       WITA   _____|_|_|\__|
______\_______________/__________..-'::::::::::::::::-..
 Enter Ticket: """ % tuple(strftime("%d|%m|%Y|%H|%M|%S",
                           localtime(scheduled)).split("|"))


def congrat(flag):
    print """
 o____
 |____| %s
 |
 | "Happy Holiday"
 |
.':::::::::::::::::-.""" % flag


def glhf():
    print """
          o
          | Oops!
     <o>  |
      |   |
    __|\__|__
.-':::::::::::'-."""


def goodbye():
    print " Have a GOOD day ^_^"

with open("private.pem", "r") as f:
    privatekey = f.read()

def getKey():
    print privatekey
