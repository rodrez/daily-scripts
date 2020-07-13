import requests
import json
import time
import sys
import os

# Function for implementing the loading animation 
def load_animation(): 
  
    # String to be displayed when the application is loading 
    load_str = f'abussing hamnster on the hamster wheel to gather {epic_id} stats.'
    ls_len = len(load_str) 
  
  
    # String for creating the rotating line 
    animation = "|/-\\"
    anicount = 0
      
    # used to keep the track of 
    # the duration of animation 
    counttime = 0        
      
    # pointer for travelling the loading string 
    i = 0                     
  
    while (counttime != 100): 
          
        # used to change the animation speed 
        # smaller the value, faster will be the animation 
        time.sleep(0.075)  
                              
        # converting the string to list 
        # as string is immutable 
        load_str_list = list(load_str)  
          
        # x->obtaining the ASCII code 
        x = ord(load_str_list[i]) 
          
        # y->for storing altered ASCII code 
        y = 0                             
  
        # if the character is "." or " ", keep it unaltered 
        # switch uppercase to lowercase and vice-versa  
        if x != 32 and x != 46:              
            if x>90: 
                y = x-32
            else: 
                y = x + 32
            load_str_list[i]= chr(y) 
          
        # for storing the resultant string 
        res =''              
        for j in range(ls_len): 
            res = res + load_str_list[j] 
              
        # displaying the resultant string 
        sys.stdout.write("\r"+res + animation[anicount]) 
        sys.stdout.flush() 
  
        # Assigning loading string 
        # to the resultant string 
        load_str = res 
  
          
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len 
        counttime = counttime + 1
      
    # for windows OS 
    if os.name =="nt": 
        os.system("cls") 
          
    # for linux / Mac OS 
    else: 
        os.system("clear") 


authorization_key = '7c88c917-e4a04331-8de5dec0-40ddb434'
epic_id = "willygatillo fb"


print(f'Getting data for {epic_id}')
user_id = requests.get(f'https://fortniteapi.io/lookup?username={epic_id}', headers={'Authorization': authorization_key})

data = user_id.json()

print(f'{epic_id} Account ID: {data["account_id"]}')
account = data['account_id']

# Player Stats
# print(f'Abussing hamnster on the hamster wheel to gather {epic_id} stats.')
load_animation()


stats = requests.get(f'https://fortniteapi.io/stats?account={account}', headers={'Authorization': authorization_key})

stats_data = stats.json()

print(f'{epic_id} data.\n')
print(stats_data['global_stats'])



		
