
![alt text](https://github.com/faflik/beans/blob/main/BakedBeans.png)

Buy some VPS or Raspberry Pi to run script 24 hours per day, then follow steps below

1. Install dependencies
    ~~~
    pip install -r requirements.txt
    ~~~

2. create .env file 
    ~~~
    touch .env
    ~~~

3. paste to the .env file yours wallet address and private key for this address
    ~~~
    ADDRESS=0xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    KEY=0xVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
    ~~~

    If you have hardware wallet use "mnemonic code converter"
    
4. use crontab to run script automatically every four hours for rebake, and and on Sundays at 23:59 for eating
   ~~~
   crontab -e
   ~~~
   
   ~~~
   1 */4 * * 1,2,3,4,5,6 python3 /PATH_TO_FILE/beans/reBake.py
   59 23 * * 7 python3 /PATH_TO_FILE/beans/eatBeans.py
   ~~~
    Edit PATH_TO_FILE. 
     - For root user /root/beans/...
     - For standard user /home/USERNAME/beans/...
        
5. To configure edit config.py:
   ~~~
   MIN_BALANCE = 0.02  
   ~~~
   minimum account BNB balance below which stop compound and claim
   
If this is helpful, send me an airdrop for beer:
 0x74ABf1db8c8b45aD529Bd3012bE1990F605360D6
 <p align="center"> 
  Visitor count<br>
  <img src="https://profile-counter.glitch.me/beans/count.svg" />
</p>
