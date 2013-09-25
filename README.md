Time Tracker (tt)
===

A lightweight command line tool to track time for projects or whatever you want.

##Installation:##

    # pip install https://github.com/catinello/tt/archive/0.3.tar.gz

##Alternative:##

    # wget https://github.com/catinello/tt/archive/0.3.tar.gz
    # tar xvzf 0.3.tar.gz; cd tt-0.3
    # make install

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

##Use case:##

Logging terminal bash sessions on tty relation with year + month tag:

    $ echo "$(which tt) --start $(date +%Y%m).$(basename $(tty))" >> ~/.bashrc
    $ echo "$(which tt) --stop $(date +%Y%m).$(basename $(tty))" >> ~/.bash_logout

Works great via ssh or chroot:

    $ ssh 192.168.8.199
    Last login: Fri Aug 10 10:01:20 2013 from 192.168.8.143
    Project 201308.0 was created.
    $

    $ exit
    logout
    Session: 4.3926 minutes
    Connection to 192.168.8.199 closed.

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

