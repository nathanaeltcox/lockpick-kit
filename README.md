# lockpick-kit
Penetration testing tool for password cracking.

Brute force an ssh connection with a dictionary attack, using the Hydra tool in Kali. It automatically writes all output to text files. 
You can use a dictionary you already have or create an ad hoc dictionary.

To install: This script is designed for use on a Kali Linux machine, in a Python 3 environment. Place a copy in the directory where you 
keep your scripts. If you have a username or password dictionary that you would like to use, place it in the same directory.

To run: Run in command line using "python lockpick-kit.py". You will be prompted to enter a username. You have several options here:
	1. If you think you know the target's username, enter it.
	2. If you have a username dictionary you would like to use, hit enter. You will then be prompted to enter the name of your
		dictionary. If you enter nothing, the default name "UsernameDictionary.txt" will be entered.
	3. If you have several username possibilities, you can build an ad hoc username dictionary. Hit enter, and when you are prompted
		to enter the dictionary name, enter "build". You will then be prompted to enter the name of your new dictionary. If you
		hit enter, it will default to "UsernameDictionary.txt". If you choose something other than the default, make sure it is
		the same filename you entered in step 2 above. Next, you will be prompted for input. Put as many possible usernames as 
		you think you need. When you are finished, enter "exit".

When you have finished entering the username(s), you will be prompted to input your target's IP address. After you input the IP address,
you will be prompted to input the name of the password dictionary you want to use. You have several options here:
	1. If you have a dictionary already, enter the name of the dictionary. If you hit enter without any input, the name will default
		to "PasswordDictionary.txt".
	2. If you want to build a new ad hoc password dictionary, or add keywords to an already existing dictionary, input "build". You
		will be prompted to input the name of the dictionary. If you hit enter without any input, it will default to
		"PasswordDictionary.txt". You will then be prompted for input. Input as many keywords as you think you need. Enter the 
		capitalized and lowercase versions as separate keywords. When you are finished, enter "exit".

Results of the scan will be printed to the command terminal, and written to a document titled "PwordResults.txt".
