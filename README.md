# RobotScraper       
RobotScraper is a simple tool written in Python to check each of the paths found in the robots.txt file and what HTTP response code they return.


# Disclaimer :warning:
**The author of this document take no responsibility for correctness. This project is merely here to help guide security researchers towards determining whether something is vulnerable to Open Redirect or not, but does not guarantee accuracy.**

# Usage
```
python3 robotScraper.py tesla.com

 ____       _           _   ____                                                                                                                                      
|  _ \ ___ | |__   ___ | |_/ ___|  ___ _ __ __ _ _ __   ___ _ __                                                                                                      
| |_) / _ \| '_ \ / _ \| __\___ \ / __| '__/ _` | '_ \ / _ \ '__|                                                                                                     
|  _ < (_) | |_) | (_) | |_ ___) | (__| | | (_| | |_) |  __/ |                                                                                                        
|_| \_\___/|_.__/ \___/ \__|____/ \___|_|  \__,_| .__/ \___|_|                                                                                                        
                                                |_|                                                                                                                   
                                                                                                                                                                      
RobotScraper v.1.0 - Open Source Project
Author: Robotshell                                                                                                                                                    
Github: https://github.com/robotshell                                                                                                                                 
                                                                                                                                                                      
Starting RobotScraper to recollect directories and pages with the syntax disallow from robots.txt in tesla.com
[+] Checking if the robots.txt file exists
[✓] File robots.txt exists:
...
...
...
[+] Checking https://tesla.com/includes/
[✓] Obtained a 403 status response code in directory: /includes/                                                                                                      
                                                                                                                                                                      
[+] Checking https://tesla.com/misc/
[✓] Obtained a 403 status response code in directory: /misc/                                                                                                          
                                                                                                                                                                      
[+] Checking https://tesla.com/modules/
[✓] Obtained a 403 status response code in directory: /modules/                                                                                                       
                                                                                                                                                                      
[+] Checking https://tesla.com/profiles/
[✓] Obtained a 403 status response code in directory: /profiles/                                                                                                      
                                                                                                                                                                      
[+] Checking https://tesla.com/scripts/
[✓] Obtained a 403 status response code in directory: /scripts/                                                                                                       
                                                                                                                                                                      
[+] Checking https://tesla.com/themes/
[✓] Obtained a 403 status response code in directory: /themes/   
...
...
...

```
# About me
[Twitter](https://twitter.com/robotshelld)


# Donation
* If you've earned a bug bounty using this tool, please consider donating to support it's development. You can help me to develop more useful scripts and tools. Thanks :heart_eyes:

[<img src="https://www.paypalobjects.com/en_US/ES/i/btn/btn_donateCC_LG.gif">](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=F4YABU5AH3NTQ&source=url)

