# AutoInflateSleepNumberBed

This Python script (autoInflate.py) will use the SleepyQ GITHUB project library to connect to your sleep number bed as a remote control and tell it to inflate to a specific pressure on a timed interval to combat leaky matress bladder. This is a product defect and eventually happens to everyone!

### **Welcome**

If you are reading this, then I suspect that you're one of Sleep Numbers many victims that was sold an insanely expensive glorified camping air mattress wrapped in the skin of a traditional mattress inflated by a glorified aquarium pump that for some reason costs $5-10k? Well, I'm here to help. My name is Jerry (aka. [Barnacules](https://twitter.com/barnacules)) and I finally had it with Sleep Number after blowing through 5 different mattress bladders (ie. _wanna be Coleman air mattresses_) over 3 years impacting both sides of my dual zone king bed.

Whenever this problem would occur it would start as a very slow leak where I would get up, go to the bathroom, come back and sit on the bed and it would feel softer than it should be. I would then check my pressure on the remote and when I pushed it up or down one pressure number it would then start the pump and inflate for a while to get back to it. This is because the Sleep Number bed does not check it pressure periodically and re-inflate if it's low. It only checks the pressure when you change the bed pressure. This is a terrible design because it means the second the mattresses start to leak even a super small leak that takes days for the bed to go fully flat unless you manually change the pressure up and down trying to get it to re-inflate it will just keep getting lower and lower.

This leak can be in the bladders which is most common since the bladders are all defective and if any sunlight so much as kisses the mattress over a period of time the connectors will start leaking and the rubbing in-between the cloth covers will break down leading to zillions of micro leaks you will never patch successful. Under warranty it's not that big of a deal since they will send someone out and replace it within a week or two which is still agony but at least it gets fixed. Well, for the first years or so then they start telling you that it's a pro-rated charge after each year where you have to pay a portion of the mattress then they will start saying you have to pay for labor even though each time they replace the bladder it's supposed to have a new warranty it will never get to.

So, I would stock up on cheap bladders if you can find them since you will need them, maybe not today, maybe not tomorrow but you will since all of these bladders are new old stock from 10-15 years ago. Now, if you can't get a new bladder because Sleep Number is jerking you around or refuses to service your mattress in a reasonable amount of time you can sink the mattresses in your bathtub or swimming pool to try and find the leak by following the bubbles and hope it's not a zillion mini holes so you can patch it with silicone to fix the problem but in-between servicing your bed this script will come in handy to keep it inflated by force feeding it an inflate command to a specified pressure at a timed interval which defaults to 5 minutes but can be tuned to meet your requirements based on speed of the leak.

Do take notice that this WILL add additional wear and tear to your pump since it will be turning on and off much more frequently than usual. I ran it like this for 4+ months before I was issued a full refund after threatening to release this script to the internet and make a full video on how insecure their SleepIQ system is and how I could issue commands to fold my neighbor's bed in half if I wanted too in the middle of the night. Once they noticed I had almost a million subscribers on YouTube they just handed my money back and had someone come and happily take the mattresses and bases away forever. But, I doubt you're going to be that lucky so I leave this script here as one of the many workarounds you will need being a Sleep Number bed owner moving forward.

Also, if replacing or patching your bladder doesn't solve the problem and it's still leaking you may find the seals in your pump are bad since that is also a big failure point depending on frequency and pressure you use. For this you'll have to take the pump apart and rebuild it which honestly these pumps suck and hard to service without creating new problems and getting them to seal right is a pain in the butthole. That being said though you might be able to find one second hand on eBay to replace it if this is the case, but you want to rule out the mattress bladder first since it's cheaper to replace then the $1000-$2000 pump.

If it does end up being the pump this script will still save you though and keep the bed inflating provided the leak isn't faster, then the pump can inflate the bed. This script has already helped a ton of people I've sent it to on Twitter and now I'm posting all this because a good friend of mine just messaged me an hour ago asking me to please give them the script since their Sleep Number bed finally did it and their husband could sleep with the bed going flat overnight. So, now I'm publishing it to the entire world so hopefully you can pass this on to any friends and family you're responsible for duping into buying this terrible garbage bed so you can sleep a little easier knowing you helped them with a stop gap method to get them by for a while longer while they do battle with Sleep Number which I suspect isn't going to be in business too much longer if they keep up these terrible business practices.

Hit me up on [Twitter.com/barnacules](https://twitter.com/barnacules) if you found this Python script useful to keep your bed inflated or if it helped a friend. Also, please tell me your story on how long you've had your bed before the failure, what model it is, and if you've had more than one repair since you've owned it. Misery loves company so come on over and tag me and let's let the rage out. Even though I no longer have a Sleep Number bed and I'm now happily back with a standard mattress that doesn't leave me cold and deflated in the morning I still have scars that will never heal that Sleep Number bed left me with and talking to you guys about it is still therapy!

Feel free to fork and improve this project as you see fit, I just would ask that you reference the original project and give me a shout out for the idea if anything. It's pretty amazing what problems we can solve with software today since the hardware is so basic. Also note that the API I'm using called SleepyQ (linked below in instructions) really made this project extra simple without having to write the wrapper to the web API myself and it also exposes some functionality I don't use like turning the under-bed light on and off or turning the vibration motors on and off. It would be trivial to upgrade the script to make the vibration motor turn on and off for a few seconds to indicate the script is still running or even have it flicker the light under the bed on and off as a visual queue the script is still running so you don't have to go check the computer to see if it's still running.

Okay... Now let's get onto how to use this damn thing since you've read my life story now brought to you by Adderall & Coffee 🍿🤣

### **Pre-Requirements (Step 1)**

- Download & Install [Python3](https://www.python.org/downloads/)
- Download & Install [SleepyQ](https://github.com/technicalpickles/sleepyq) _*Follow projects instructions*_
- Download _autoInflate.py_ from AutoInflateSleepNumberBed project (this project)

### **Configuration (Step 2)**

- Login to your [SleepIQ](https://www.sleepnumber.com/login) account to verify username & password are correct
- Open **_autoInflate.py_** locally in your favorite text editor (_read/write mode_)
- Change _**userName**_ (**line 16**) & _**passWord**_ (**line 17**) variables to Username & Password that works on Website
- Change _**pressure**_(**line 19**)_to desired normal pressure you sleep at (\_default: 80_)
- Optionally change _**timer**_ variables to number of seconds between applying pressure (_default: 600_)
- Save _**autoInflate.py**_ with your changes

### **Execution (Final Repeated Step)**

- Open a shell window (cmd.exe for Windows) or (bash for Linux)
- Navigate to folder containing _**autoInflate.py**_
- Run '_**python3.exe autoInflate.py**_' and push Enter
- Script will now run until you close the shell or hit CTRL-C to break execution

### **Extra Added Bonus Stuff**

Once you have the script tuned and working as expected and screen output shows no errors & bed is inflating to desired pressure and holding you can then open **Task Scheduler** in Windows (or similar on other platforms) and create a basic task that triggers on **Computer Startup** that starts the program by setting program to **cmd.exe** and passing "**python3 autoInflate.py** and make sure you set **Star In** folder to the actual directory where the script is located locally on your hard drive."

**Enjoy your good night's rest not waking up laying on the wood base & ping me over on Twitter if found this project useful**
Jerry (aka. [Barnacules](https://twitter.com/barnacules))
[YouTube/Twitch/Twitter/Instagram/TikTok/Discord/Facebook](http://linktr.ee/barnacules)
