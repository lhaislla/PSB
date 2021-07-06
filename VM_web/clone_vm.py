import subprocess
import sys
import virtualbox
import os
vbox  =  virtualbox.VirtualBox ()
sessão = virtualbox.Session ()
machine = vbox.find_machine ("windows")
subprocess.run(vbox)
       