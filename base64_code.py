import base64
import os

os.system('cls')

bgwhite = '\x1b[47m'
bgwhitewithblack = '\x1b[38;5;15m'
black = '\x1b[30m'
white = '\x1b[37m'
blue = '\x1b[34m'
green = '\x1b[32m'
red = '\x1b[41m'
wrongwithbgMagentha = '\x1b[38;5;9m'
magenta = '\x1b[45m'
stop = '\x1b[0m'

print(f"""{wrongwithbgMagentha}░█▀▄░█▀█░█▀▀░█▀▀░▄▀▀░█░█░░░░░░░░░█▀▀░█▀█░█▀▀░█▀█░█▀▄░█▀▀░█▀▄░░░▄▀░░░░█▀▄░█▀▀░█▀▀░█▀█░█▀▄░█▀▀░█▀▄
░█▀▄░█▀█░▀▀█░█▀▀░█▀▄░░▀█░░░░░░░░░█▀▀░█░█░█░░░█░█░█░█░█▀▀░█▀▄░░░▄█▀░░░█░█░█▀▀░█░░░█░█░█░█░█▀▀░█▀▄
░▀▀░░▀░▀░▀▀▀░▀▀▀░░▀░░░░▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀▀░░▀▀▀░▀░▀░░░░▀▀░░░▀▀░░▀▀▀░▀▀▀░▀▀▀░▀▀░░▀▀▀░▀░▀ {stop}""")

print('\n \n')

while True:
    decision = input(f'{blue}Encode or Decode :{stop} ')
    print('\n')

    if decision == 'Encode':
        try:
            passw = input(
                f' {green}Enter your message (that needed to be encoded) :{stop} ')
            passw_bytes = passw.encode("ascii")

            base64_encbytes = base64.b64encode(passw_bytes)
            base64_encstring = base64_encbytes.decode("ascii")
        except Exception:
            print('\n')
            print(f' {red}something went wrong !! please try again...{stop}')
            quit()
        else:
            print('\n')
            print(f'{green}Encoded message is : {blue}{base64_encstring}{stop}')
            print('\n')
    elif decision == 'Decode':
        try :
            passwd = input(f' {green}enter the encoded message :{green} ')
            passwd_bytes = passwd.encode("ascii")

            base64_decbytes = base64.b64decode(passwd_bytes)
            base64_decstring = base64_decbytes.decode("ascii")
        except Exception:
            print('\n')
            print(f' {red}something went wrong !! please try again...{stop}')
        else :
            print('\n')
            print(f' {green}Decoded message is : {blue}{base64_decstring}{stop}')
            print('\n')
    elif decision == 'encode':
        try:
            passw = input(
                f' {green}Enter your message (that needed to be encoded) :{stop} ')
            passw_bytes = passw.encode("ascii")

            base64_encbytes = base64.b64encode(passw_bytes)
            base64_encstring = base64_encbytes.decode("ascii")
        except Exception:
            print('\n')
            print(f' {red}something went wrong !! please try again...{stop}')
            quit()
        else:
            print('\n')
            print(f'{green}Encoded message is : {blue}{base64_encstring}{stop}')
            print('\n')
    elif decision == 'decode':
        try :
            passwd = input(f' {green}enter the encoded message :{green} ')
            passwd_bytes = passwd.encode("ascii")

            base64_decbytes = base64.b64decode(passwd_bytes)
            base64_decstring = base64_decbytes.decode("ascii")
        except Exception:
            print('\n')
            print(f' {red}something went wrong !! please try again...{stop}')
        else :
            print('\n')
            print(f' {green}Decoded message is : {blue}{base64_decstring}{stop}')
            print('\n')
    else:
        print('\n')
        print(f' {red}please type in method & try again !!{stop}\n {wrongwithbgMagentha}(example : if you want to Encode message type in : Encode & to Decode message type in: Decode){stop}')
        print('\n')
