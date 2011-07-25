def syscmd(commandline,channel):
    cmd=commandline.replace('sys ','')
    cmd=cmd.rstrip()
    os.system(cmd+' >temp.txt')
    a=open('temp.txt')
    ot=a.read()
    ot.replace('n','|')
    a.close()
    s.send('PRIVMSG '+channel+' :'+ot+'n')
    return 0 
