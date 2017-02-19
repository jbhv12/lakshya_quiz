l=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
l=[0,1]
l=[]
d={
    'Wireless specification 802.11ac allows for how many MIMO streams?':['8',['4','10','6']],
    'Which linguist greatly influenced theoretical computer science with such models as a hierarchy of formal grammars?':['Noam Chomsky',['Steven Pinker', 'Marvin Minsky', 'Max Mueller']],
    'who served as CEO of Apple from 1993 to 1996?':['Michael Spindler',['Steve Jobs','Tim Cook','Avie Tevanian']],
    'A heated exchange on the internet is often known as what ?':['A flame war',['Cyberbullying', 'Trolling','A grudge match','A skirmish']],
    'In the meme "Most interesting man in the world", what does he have on the table?':['Beer',['vodka','whiskey','Wine']],
    'Sockets that use TCP or STCP are known as what ?':['Stream sockets',['Raw sockets','Connectionless socket','Data Socket']],
    'What term is used to describe the usually deliberate writing of valid code in an almost human - unreadable manner ?':['Obfuscation',['Strangling','Obsolescence','Encryption']],
    'who started the GNU project ?':['Richard Stallman',['Linus Torvalds','Marc Andreessen','Matthew McConaughey']],
    'Which scientist designed the ana- lytical engine , the first attempt at general computing device ?':['Charles Babbage',['George Boole','Isaac Newton','Leonard Euler']],
    'Who is popularly known as the Father of Pentium chip?':['Vinod Dham',['Marcian Hoff','Masatoshi Shima','Kim Jong Un']],
    'Which company resulted out of a communication problem between a couple at the Stanford University due to some protocol issue?':['Cisco',['Vodafone','D-Link','IEEE']],
    'Pavel Baudis created which antivirus software in 1990s in order to counter the famous Vienna Computer Virus ?':['Avast',['Norton','Kaspersky','AVG']],
    "X began as a response to disaster. Japan's devastating Tohoku earthquake in March 2011 damaged telecommunications infrastructure nationwide. obliging employees at NHN Japan created X to rely on Internet-based resources to communicate. What is X?":['Line',['Twitter','WeChat','Kik']],
    'Whos is CEO of Whatsapp ?':['Jan Koum',['Brian Acton','Pavel Durov']],
    'Who made the Amoeba OS(for which the Python programming language was originally developed)?':['Andrew S. Tanenbaum',['Guido van Rossum','Ken Thompson','Dennis Ritchie']],
    'Expand MPEG.':['Moving Picture Expert Group',['Motion Picture Expert Group','Moving Photographic Expert Group','Motion Photographic Expert Group']],
    'All Windows drivers are dated to one perticular date. Which?':['June 21, 2006',['August 24, 2001','16 November 2006','July 22, 2009']],
    'IEEE 1394 is more commonly known as?':['Firewire',['Bluetooth','Wi-Fi','Ethernet-n','NFC']],
    'Which of these Linux distributions was derived from German phrase translated as " Soft- ware and Systems Development " ?':['SUSE',['Fedora','Ubuntu','SAS']],
    'The first widely known and successful programming lan- guage was developed from 1954 to 1957 at IBM , and was known as?':['Fortran',['Lisp','C','Assembly']]
    }

for i,j in zip(d,range(len(d))):
    l.append(j)

print(l)
