import os
import subprocess
import pprint

class console():

    def __init__(self):
        self.default_script = "ws.c"
        self.working_code = self.write_overhead()
        
    def write_overhead(self):
        return "#include <stdio.h> \nint main()\n{ \n"

    def update_and_execute(self):
        # executes and returns the updated code
        
        try_code = self.working_code + self.inp + "\nreturn 0;\n}"

        # write code to file for execution
        f = open(self.default_script, "w")
        f.write(try_code)
        f.close()
        
        compile_cmd = "gcc {}".format(self.default_script)
        execute_cmd = "./a.out"
        
        # compile using gcc and check for error, if error skip line
        process_1 = subprocess.Popen(compile_cmd.split(), stdout=subprocess.PIPE, stderr = subprocess.PIPE)
        stdout_1, stderr_1 = process_1.communicate()
        
        if(stderr_1 != None and "error" in stderr_1.decode("utf-8")):
            print(stderr_1)
            return 

        # execute .out
        process_2 = subprocess.Popen(execute_cmd.split(), stdout=subprocess.PIPE)
        stdout_2, stderr_2 = process_2.communicate()

        if(stderr_2 != None and "error" in stderr_2.decode("utf-8")):
            print(stderr_2)
            return
        else:
            print(stdout_2.decode("utf-8")) 

        self.working_code = self.working_code + self.inp + "\n"

    def write_intro(self):
        print()
        print("Running C Shell; v1.0;")
        print("using workspace: {}".format(self.default_script))
        print("imported libraries: stdio.h")
        print()


    def run_cli(self):

        while True:
            self.inp = input(">> ")
            
            if(self.inp == "exit"):
                exit()
            else:
                self.update_and_execute()
                # print(code)
        

if __name__ == "__main__":
    new_console = console()
    new_console.write_intro()
    new_console.run_cli()

    
    

    