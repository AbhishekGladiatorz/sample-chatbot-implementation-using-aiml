# coding=utf-8
import aiml
import os
import sys



# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("aiml/std-startup.xml")

kernel.respond("load aiml b")

os.system('cls' if os.name == 'nt' else 'clear') # clear terminal

# Press CTRL-C to break this loop
while True:
    message = raw_input(">> ")
    if message == "quit" or message == "exit": # exit from chat
        print("bye...")
        exit()
    elif message == "save":
        kernel.saveBrain("bot_brain.brn")
    else:
        bot_response = kernel.respond(message)
        # Do something with bot_response
        print(bot_response)
