#program that starts a gdb session and loads a binary to the target.Target is left in halted state.
import subprocess

def startGDB(binPath,cfgPath):
    subprocess sp=popen(['openocd','-f',cfgPath]);
    string="load "+binPath;
    subprocess.call("arm-none-eabi-gdb -ex 'target remote localhost:3333' -ex 'monitor reset halt' -ex "+string,shell=True);
    return;
#test code
#startGDB("/home/greg/CS3950/HelloArm.elf");
