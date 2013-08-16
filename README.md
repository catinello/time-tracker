Time Tracker (tt)
===

Lightweight command line tool to track time for projects.

##Installation:##

    # pip install https://github.com/catinello/tt/archive/0.1.tar.gz

##Usage:##

    Usage: tt {--start|--stop|--list} [PROJECT]

##Requirements:##

Python 2.7 (tested on Debian and Ubuntu)

##Examples:##

Create a new project and start a session:

    $ tt --start newproject
    Project newproject was created.

Stop a running session:

    $ tt --stop newproject
    Session: 6.9066 minutes

List all sessions with a calculated total amount of hours:

    $ tt --list newproject
    Session: Fri 09. August 2013 11:06 -> Fri 09. August 2013 11:13 -> 6.906 min
    Session: Fri 09. August 2013 11:14 -> Fri 09. August 2013 11:17 -> 3.292 min
    Total: 0.1699 hours

##Logging:##

Every start or stop command is logged via syslog to reaudit later.

    # grep newproject /var/log/syslog
    Aug  9 11:06:05 dev /usr/local/bin/tt[30948]: --start -> newproject
    Aug  9 11:13:00 dev /usr/local/bin/tt[30958]: --stop -> newproject
    Aug  9 11:14:06 dev /usr/local/bin/tt[30961]: --start -> newproject
    Aug  9 11:17:24 dev /usr/local/bin/tt[30968]: --stop -> newproject

##Data:##

All project data is stored in the home directory of the user. 

    $ ls ~/.tt
    newproject

##License:##

[&copy; Antonino Catinello][HOME] - [MIT-License][MIT]

[MIT]:https://github.com/catinello/tt/blob/master/LICENSE
[HOME]:http://antonino.catinello.eu

