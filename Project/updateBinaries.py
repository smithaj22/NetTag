import subprocess
import sys
import os
import shutil

'''updates the folder to what is up on the github
'''
'''def binUpdate():'''
print ("starting program")
os.mkdir("hold")
os.chdir("hold")
print("dir made")
try:
    subprocess.check_call(['git', 'init'])
    subprocess.check_call(['git', 'remote', 'add', '-f', 'origin', 'https://github.com/smithaj22/NetTag.git'])
    subprocess.check_call(['git', 'config', 'core.sparseCheckout', 'true'])
    subprocess.check_call(['echo' ,'\"NETTAG/boards/\"', '>>', '.git/info/sparse-checkout'])
    subprocess.check_call(['git', 'pull', 'origin', 'master'])
    os.chdir("../")
    shutil.rmtree("NETTAG")
    subprocess.check_call(['mv', 'hold/','NETTAG'])

except:
    os.chdir("../")
    shutil.rmtree("hold")
    print("dir deleted")
    print "Error in update script:\n", sys.exc_info()[0]
    raise
