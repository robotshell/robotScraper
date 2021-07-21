# RobotScraper       
RobotScraper is a simple tool written in Python to check each of the paths found in the robots.txt file and what HTTP response code they return.


# Disclaimer :warning:
**The author of this document take no responsibility for correctness. This project is merely here to help guide security researchers towards determining whether something is vulnerable or not, but does not guarantee accuracy.**

# Usage
```
python3 robotScraper.py -d twitter.com -s output.txt 

 ____       _           _   ____                                 
|  _ \ ___ | |__   ___ | |_/ ___|  ___ _ __ __ _ _ __   ___ _ __ 
| |_) / _ \| '_ \ / _ \| __\___ \ / __| '__/ _` | '_ \ / _ \ '__|
|  _ < (_) | |_) | (_) | |_ ___) | (__| | | (_| | |_) |  __/ |   
|_| \_\___/|_.__/ \___/ \__|____/ \___|_|  \__,_| .__/ \___|_|   
                                                |_|   

RobotScraper v.1.0 - Open Source Project | Author: Robotshell | Twitter: https://twitter.com/robotshelld

Starting RobotScraper to recollect directories and pages from robots.txt in twitter.com
[+] Checking if the robots.txt file exists
[✓] File robots.txt exists:
...
...
...
[+] Checking https://twitter.com/?_escaped_fragment_
[✓] Obtained a 200 OK success status response code in directory: /?_escaped_fragment_                           
                                                                                                                
[+] Checking https://twitter.com/*?lang=
[✓] Obtained a 200 OK success status response code in directory: /*?lang=                                       
                                                                                                                
[+] Checking https://twitter.com/hashtag/*?src=
[✓] Obtained a 200 OK success status response code in directory: /hashtag/*?src=                                
                                                                                                                
[+] Checking https://twitter.com/search?q=%23
[✓] Obtained a 200 OK success status response code in directory: /search?q=%23                                  
                                                                                                                
[+] Checking https://twitter.com/i/api/
[✓] Obtained a 403 status response code in directory: /i/api/        
...
...
...

```

# PoC
![Example image](https://raw.githubusercontent.com/robotshell/dorkSraper/main/poc.gif)

# About me
[Twitter](https://twitter.com/robotshelld)


# Donation
* If you've earned a bug bounty using this tool, please consider donating to support it's development. You can help me to develop more useful scripts and tools. Thanks :heart_eyes:

[<img src="https://www.paypalobjects.com/en_US/ES/i/btn/btn_donateCC_LG.gif">](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=F4YABU5AH3NTQ&source=url)

