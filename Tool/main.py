




import os
import random
import sys
import time

# all the containers to store items in the memory

proxy:list = []
working_proxy:list = []

proxy_count:int = 0
errors:int = 0
inactive_proxy:int = 0



R = '\033[31m' # red 
G = '\033[32m' # green 
Y = '\033[33m' # yellow
C = '\033[36m' # cyan

E = '\033[0m' # end


if len(sys.argv) == 4:
     
     try:
        sys.argv[3] = int(sys.argv[3])
        
        with open(str(sys.argv[1]),"r") as P:
             for line in P:
                 file_proxy= line.strip()
                 proxy.append(file_proxy)
             print(f"{R}{len(proxy)}{G} found in {C}{sys.argv[1]}{E}")
                 
        with open (str(sys.argv[2]),"w") as f:
            f.write("ALL WORKING PROXIES HERE!\n")

        
        while True:
        
            IP = random.choice(proxy)
            all_proxy = len(proxy)
            local_time = time.strftime("%H:%M:%S")

            try:
                print(f"{Y}[{local_time}]{C} Proxy Found{E} : {G}({proxy_count}{E}/{all_proxy}) | {C}Erros:{R}[{errors}]{E} | Non_Usable:[{inactive_proxy}] ")
                res = os.system(f'ping -c 1 {IP.split(":")[0]} >/dev/null 2>%1')
        
                if res == 0:
                    if IP in str(working_proxy):
                        pass
                
                
                    else:
                        if proxy_count >= int(sys.argv[3]):
                            print(f"{G}[SUCCESS]{E} Finished and saved all the proxies to {sys.argv[2]}")
                            sys.exit(0)
                            
                        else:
                            proxy_count += 1
                            working_proxy.append(IP)
                            print(f"{R}{working_proxy}{E}")
                            with open(str(sys.argv[2]),"a") as f:
                                f.write(f"{IP}\n")
            
                else:
                    inactive_proxy += 1
        
            except Exception as e:
                       errors += 1
                
     except Exception as Excp:
            print(Excp)
            sys.exit(1)
else:
    raise TypeError(f"{sys.argv[0]} : Invalid argument for importfilename exportfilename number ")
    



