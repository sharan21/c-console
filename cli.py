import os
import subprocess

scripts_dir = './scripts/'

default_script = scripts_dir + "ws.c"
default_out = scripts_dir + "ws.out"
code = ""

def write_overhead(f):
    f.write("#include <stdio.h> \n")
    f.write("int main(){ \n")

def complete_and_execute(f):

    f.write("return 0;\n}")
    # bashCommand = "gcc {} -o {}".format(default_script, default_out)
    
    
    # process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    # output, error = process.communicate()




if __name__ == "__main__":

    f = open(default_script, "w")

    print("Running C Shell; v1.0;")
    print("using workspace: {}".format(default_script))
    print("imported libraries: stdio.h")

    write_overhead(f)


    while True:

        inp = input(">")
        
        if(inp == "exit"):
            exit()
            f.close()
        else:
            f.write(inp+";\n")
            # complete_and_execute(f)
            # print(inp)