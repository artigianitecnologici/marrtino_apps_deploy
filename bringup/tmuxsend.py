import os
import time

class TmuxSend:

    # listwindows = [ 'windowname', ... ]
    def __init__(self, sessionname, listwindows):
        self.nwindows = len(listwindows)
        self.sessionname = sessionname
        os.system('tmux -2 new-session -d -s %s' %self.sessionname) # tmux session
        os.system('tmux select-window -t %s:0' %self.sessionname)
        os.system('tmux rename-window \'quit\'')                  # window 0 - quit
        for i in range(0,self.nwindows):
            os.system('tmux new-window -t %s:%d -n \'%s\'' %(self.sessionname, i+1, listwindows[i]))    

    def roslaunch(self, wid, mdir, mlaunch, mparams=''):
        os.system('tmux select-window -t %s:%d' %(self.sessionname,wid))
        os.system('tmux send-keys "cd $MARRTINO_APPS_HOME/%s" C-m' %(mdir))
        os.system('tmux send-keys "roslaunch %s.launch %s" C-m' %(mlaunch, mparams))

    def roskill(self, rosnode):
        wid = 0
        os.system('tmux select-window -t %s:%d' %(self.sessionname,wid))
        os.system('tmux send-keys "rosnode kill %s" C-m' %(rosnode))

    def python(self, wid, mdir, mpy, mparams=''):
        os.system('tmux select-window -t %s:%d' %(self.sessionname,wid))
        os.system('tmux send-keys "cd $MARRTINO_APPS_HOME/%s" C-m' %(mdir))
        os.system('tmux send-keys "python %s %s" C-m' %(mpy, mparams))

    def cmd(self, wid, cmd):
        os.system('tmux select-window -t %s:%d' %(self.sessionname,wid))
        os.system('tmux send-keys "%s" C-m' %(cmd))

    def killall(self, wid):
        self.Cc(wid)
        time.sleep(3)
        self.Ck(wid)

    def Cc(self, wid):
        os.system('tmux select-window -t %s:%d' %(self.sessionname,wid))
        os.system('tmux send-keys C-c')

    def Ck(self, wid):
        os.system('tmux select-window -t %s:%d' %(self.sessionname,wid))
        os.system('tmux send-keys C-\\')

    def quitall(self):
        self.roskill('-a')
        time.sleep(3)
        for i in range(0,self.nwindows):
            self.Cc(i+1)  # C-c on all the windows
            time.sleep(1)
        for i in range(0,self.nwindows):
            self.Ck(i+1)  # C-\ on all the windows
            time.sleep(1)

