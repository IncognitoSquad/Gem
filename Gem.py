import requests, time, os, json, yaml, ctypes
try:
    from colorama import *
except:
    print("Didn't detect Colorama, Installing Colorama...")
    print("NOTE: Might print errors, Ignore")
    os.system("pip install colorama")
    os.system("pip3 install colorama")
try:
    from yaml import *
except:
    print("Didn't detect PyYaml, Installing PyYaml...")
    print("NOTE: Might print errors, Ignore")
    os.system("pip install pyyaml")
    os.system("pip3 install pyyaml")
init()

found = 0
checked = 0
api = open("config.yml", "r")
cfg = yaml.load(api, Loader=yaml.FullLoader)
url = "http://api.thealtening.com/v2/generate?key=" + cfg['auth']['api']

working = open("working.txt", "w")

ascii = """
 ██████  ███████ ███    ███ 
██       ██      ████  ████ 
██   ███ █████   ██ ████ ██ 
██    ██ ██      ██  ██  ██ 
 ██████  ███████ ██      ██ 
                            
                            """
ctypes.windll.kernel32.SetConsoleTitleW("Gem ┃ 1.0 ┃ Checked: None ┃ Found: None ┃     [ made by IncognitoSquad ]")
print(Fore.YELLOW + ascii)
time.sleep(2)
print("")
print("")
a = input("What Server (Hypixel/Mineplex): ")
b = input("Amount of accounts to check: ")


if(a.lower() == "hypixel"):
    print(Fore.CYAN + "Starting...")
    print("")
    try:
        for i in range(int(b)):
            checked = checked + 1
            ctypes.windll.kernel32.SetConsoleTitleW("Gem ┃ 1.0 ┃ Checked: " + str(checked) + " ┃ Found: " + str(found) + "     [ made by IncognitoSquad ]")
            response = requests.get(url)
            json_data = json.loads(response.text)
            checker = json_data['info']
            if (str(checker).lower() == "vip" or str(checker).lower() == "vip+" or str(
                    checker).lower() == "mvp" or str(checker).lower() == "mvp+" or str(
                checker).lower() == "mvp++"):
                print(Fore.BLACK + "[" + Fore.GREEN + "+" + Fore.BLACK + "] " + Fore.WHITE + "Found Ranked Account: " +
                      json_data['token'] + ":" + json_data['password'] + " With info " + json_data['info'])
                working.write(json_data['username'] + ":" + json_data['token'] + " Info: " + json_data['info'] + "\n")
                found = found + 1
        working.close()
    except:
        print(Fore.BLACK + "[" + Fore.RED + "+" + Fore.BLACK + "] " + Fore.WHITE + "Something went wrong, Maybe wrong API?")
        pass
elif(a.lower() == "mineplex"):
    print(Fore.CYAN + "Starting...")
    print("")
    try:
        for i in range(int(b)):
            checked = checked + 1
            ctypes.windll.kernel32.SetConsoleTitleW("Gem ┃ 1.0 ┃ Checked: " + str(checked) + " ┃ Found: " + str(found) + "      [ made by IncognitoSquad ]")
            response = requests.get(url)
            json_data = json.loads(response.text)
            checker = json_data['info']
            if (str(checker).lower() == "ultra" or str(checker).lower() == "hero" or str(
                    checker).lower() == "legend" or str(checker).lower() == "titan" or str(
                    checker).lower() == "eternal" or str(checker).lower() == "immortal"):
                print(Fore.BLACK + "[" + Fore.GREEN + "+" + Fore.BLACK + "] " + Fore.WHITE + "Found Ranked Account: " + json_data['token'] + ":" + json_data['password'] + " With info " + json_data['info'])
                working.write(json_data['username'] + ":" + json_data['token'] + " Info: " + json_data['info'] + "\n")
                found = found + 1
        working.close()
    except:
        print(Fore.BLACK + "[" + Fore.RED + "+" + Fore.BLACK + "] " + Fore.WHITE + "Something went wrong, Maybe wrong API?")
        pass
