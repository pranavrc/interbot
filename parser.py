def parsemsg(msg):
    complete=msg[1:].split(':',1) #Parse the message into useful data
    info=complete[0].split(' ')
    msgpart=complete[1]
    sender=info[0].split('!')
    if msgpart[0]=='`' and sender[0]==OWNER: #Treat all messages starting with '`' as command
        cmd=msgpart[1:].split(' ')
        if cmd[0]=='op':
            s.send('MODE '+info[2]+' +o '+cmd[1]+'n')
        if cmd[0]=='deop':
            s.send('MODE '+info[2]+' -o '+cmd[1]+'n')
        if cmd[0]=='voice':
            s.send('MODE '+info[2]+' +v '+cmd[1]+'n')
        if cmd[0]=='devoice':
            s.send('MODE '+info[2]+' -v '+cmd[1]+'n')
        if cmd[0]=='sys':
            syscmd.syscmd(msgpart[1:],info[2])
        
    if msgpart[0]=='-' and sender[0]==OWNER : #Treat msgs with - as explicit command to send to server
        cmd=msgpart[1:]
        s.send(cmd+'n')
        print 'cmd='+cmd


