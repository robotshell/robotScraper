#!/usr/bin/env python

# Robot Scraper
#
# ORHOund is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Knock is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Knock. If not, see <http://www.gnu.org/licenses/>.

# Standard Python libraries
import sys
import requests
from bs4 import BeautifulSoup

class colors:
    HEADER = '\033[1;35m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKCYANL = '\033[1;36m'
    OKGREEN = '\033[92m'
    OKGREENL = '\033[1;32m' 
    OKREDL = '\033[1;31m' 
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def banner():
	print(colors.HEADER  + """
 ____       _           _   ____                                 
|  _ \ ___ | |__   ___ | |_/ ___|  ___ _ __ __ _ _ __   ___ _ __ 
| |_) / _ \| '_ \ / _ \| __\___ \ / __| '__/ _` | '_ \ / _ \ '__|
|  _ < (_) | |_) | (_) | |_ ___) | (__| | | (_| | |_) |  __/ |   
|_| \_\___/|_.__/ \___/ \__|____/ \___|_|  \__,_| .__/ \___|_|   
                                                |_|   
""" + colors.ENDC)
	print(colors.WARNING + "RobotScraper v.1.0 - Open Source Project | " + colors.OKGREEN + "Author: " + colors.WARNING + "Robotshell | " + colors.OKGREEN + "Twitter: " + colors.WARNING + "https://twitter.com/robotshelld\n" + colors.ENDC)

#CORE FUNCTION
def getRobots(domain,enable_save, filename):

	print (colors.OKCYAN + "Starting RobotScraper to recollect directories and pages from " + colors.WARNING + "robots.txt " + colors.OKCYAN + "in " + colors.FAIL + domain + colors.ENDC)
	print (colors.OKCYAN + "[+] Checking if the" + colors.WARNING + " robots.txt " + colors.OKCYAN + "file exists" + colors.ENDC)

	r = requests.get("https://" + domain + "/robots.txt")

	if r.status_code == 200:
		print (colors.OKCYAN + "[✓] File" + colors.WARNING + " robots.txt " + colors.OKCYAN + "exists:" + colors.ENDC)
		print()
		
		soup = BeautifulSoup(r.text, 'html.parser')

		with open("robots.txt", "w") as file:
    			file.write(str(soup))
		print (soup)

		file = open("robots.txt", "rt")

		for line in file:
			a = 0
				
			if "Allow:" in line:
				directory = line.replace('Allow: ', '')
				a = 1

			if a == 0:
				directory = line.replace('Disallow: ', '')


			if directory[0] == '/':
	
				newDomain = "https://" + domain + directory
				r2 = requests.get(newDomain)
				
				print (colors.OKCYAN + "[+] Checking " + colors.WARNING + newDomain + colors.ENDC, end = '')

				if r2.status_code == 200:
					
					print (colors.OKGREEN + "[✓] Obtained a " + colors.WARNING + "200 OK " + colors.OKGREEN +  "success status response code in directory: " + colors.WARNING + directory + colors.ENDC)
					
					if enable_save == 1:
						file = open(filename, "a")
						file.write(str(directory))
						file.close()

				elif r2.status_code == 302:
					print (colors.OKGREEN + "[✓] Obtained a " + colors.WARNING + "302 Found redirect " + colors.OKGREEN +  "status response code in directory: " + colors.WARNING + directory + colors.ENDC)
				
				else:
					print (colors.FAIL + "[✓] Obtained a " + colors.WARNING + str(r2.status_code) + colors.FAIL +  " status response code in directory: " + colors.WARNING + directory + colors.ENDC)

		file.close()

     	
#MAIN FUNCTION
def main():
	banner()
	enable_save = 0
	filename = ""

	if len(sys.argv) == 1:
		print (colors.FAIL + "ERROR: No domain or parameters found" + colors.ENDC)
	elif len(sys.argv) == 2:
		arg = sys.argv[1]
		
		if arg == "-h" or arg == "--help" :
			print (colors.BOLD + "HELP SECTION:" + colors.ENDC)
			print ("Usage:" + colors.OKCYAN + '\trobotscraper.py domain' + colors.ENDC)
			print ("Example:" + colors.OKCYAN + '\trobotscraper.py example.com -s output.txt' + colors.ENDC)
			print ("-d,--domain" + colors.OKCYAN + "\tSpecifies the domain" + colors.ENDC)
			print ("-h,--help" + colors.OKCYAN + "\tThis help" + colors.ENDC)
			print ("-v,--version" + colors.OKCYAN + "\tShow version" + colors.ENDC)
			print ("-s,--save" + colors.OKCYAN + "\tEnable save output and specifies the output file" + colors.ENDC)
		elif arg == "-v" or arg == "--version":
			print (colors.WARNING + "RobotScraper v.1.0" + colors.ENDC)
		else:
			print (colors.FAIL + "ERROR: Incorrect argument or sintaxis" + colors.ENDC)

	elif len(sys.argv) > 2 and len(sys.argv) <= 5:

		if sys.argv[1] == "-d" or sys.argv[1] == "--domain":
			
			domain = sys.argv[2]
			
			if(len(sys.argv) > 3):
				if sys.argv[3] == "-s" or sys.argv[3] == "--save":
					enable_save = 1
					filename = sys.argv[4]

			getRobots(domain,enable_save,filename)
				
main()
