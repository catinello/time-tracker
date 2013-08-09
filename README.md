Time Tracker (tt)
===

Lightweight command line tool to track time for projects.

##Installation:##

    # pip install https://github.com/catinello/tt/archive/0.1.tar.gz

##Usage:##

    Usage: tt {--start|--stop|--list} [PROJECT]

##Examples:##

Create a new project and start a session:

    # tt --start newproject
    Project newproject was created.

Stop a running session:

    # tt --stop newproject
    Session: 6.9066 minutes

List all sessions with a calculated total amount of hours:

    # tt --list newproject
    Session: Fri 09. August 2013 11:06 -> Fri 09. August 2013 11:13 -> 6.906 min
    Session: Fri 09. August 2013 11:14 -> Fri 09. August 2013 11:17 -> 3.292 min
    Total: 0.1699 hours

##Logging:##

Every start or stop command is log via syslog to reaudit later.

##Data:##

All project data is stored in the home directory of the user. 

    # ls ~/.tt
    newproject
