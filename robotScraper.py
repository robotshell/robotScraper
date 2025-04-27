import sys
import requests
import urllib3
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# SSL uyarılarını devre dışı bırak
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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
	print(colors.WARNING + "RobotScraper v.1.1 - Open Source Project | " + colors.OKGREEN + "Author: " + colors.WARNING + "Robotshell | " + colors.OKGREEN + "Twitter: " + colors.WARNING + "https://twitter.com/robotshelld\n" + colors.ENDC)

#CORE FUNCTION
def getRobots(domain, enable_save, filename):

	print (colors.OKCYAN + "Starting RobotScraper to recollect directories and pages from " + colors.WARNING + "robots.txt " + colors.OKCYAN + "in " + colors.FAIL + domain + colors.ENDC)
	print (colors.OKCYAN + "[+] Checking if the" + colors.WARNING + " robots.txt " + colors.OKCYAN + "file exists" + colors.ENDC)

	r = requests.get("https://" + domain + "/robots.txt", verify=False)

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
				r2 = requests.get(newDomain, verify=False)
				
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
def getSitemap(domain, enable_save, filename):
    print(colors.OKCYAN + "Starting RobotScraper to extract URLs from " + colors.WARNING + "sitemap.xml " + colors.OKCYAN + "in " + colors.FAIL + domain + colors.ENDC)
    print(colors.OKCYAN + "[+] Checking if " + colors.WARNING + "sitemap.xml " + colors.OKCYAN + "file exists" + colors.ENDC)

    try:
        r = requests.get("https://" + domain + "/sitemap.xml", verify=False)

        if r.status_code == 200:
            print(colors.OKCYAN + "[✓] File " + colors.WARNING + "sitemap.xml " + colors.OKCYAN + "exists:" + colors.ENDC)
            print()
            
            sitemap_urls = []
            
            try:
                root = ET.fromstring(r.content)
                namespace = {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"}
                
                for url in root.findall(".//ns:url", namespace):
                    loc = url.find("ns:loc", namespace)
                    if loc is not None and loc.text:
                        sitemap_urls.append(loc.text)
                        print(colors.OKGREEN + "[✓] Found URL: " + colors.WARNING + loc.text + colors.ENDC)
                        
                        if enable_save == 1:
                            with open(filename, "a") as file:
                                file.write(loc.text + "\n")
                
                for sitemap in root.findall(".//ns:sitemap", namespace):
                    loc = sitemap.find("ns:loc", namespace)
                    if loc is not None and loc.text:
                        print(colors.OKGREEN + "[✓] Found nested sitemap: " + colors.WARNING + loc.text + colors.ENDC)
                        try:
                            nested_r = requests.get(loc.text, verify=False)
                            if nested_r.status_code == 200:
                                nested_root = ET.fromstring(nested_r.content)
                                for url in nested_root.findall(".//ns:url", namespace):
                                    nested_loc = url.find("ns:loc", namespace)
                                    if nested_loc is not None and nested_loc.text:
                                        sitemap_urls.append(nested_loc.text)
                                        print(colors.OKGREEN + "[✓] Found URL in nested sitemap: " + colors.WARNING + nested_loc.text + colors.ENDC)
                                        
                                        if enable_save == 1:
                                            with open(filename, "a") as file:
                                                file.write(nested_loc.text + "\n")
                        except Exception as e:
                            print(colors.FAIL + "[✗] Error processing nested sitemap: " + colors.WARNING + str(e) + colors.ENDC)
            except ET.ParseError:
                print(colors.FAIL + "[✗] XML parsing error. Trying alternative parsing method." + colors.ENDC)
                soup = BeautifulSoup(r.content, 'xml')
                urls = soup.find_all('loc')
                
                for url in urls:
                    sitemap_urls.append(url.text)
                    print(colors.OKGREEN + "[✓] Found URL: " + colors.WARNING + url.text + colors.ENDC)
                    
                    if enable_save == 1:
                        with open(filename, "a") as file:
                            file.write(url.text + "\n")
            
            print(colors.OKCYAN + "\n[+] Total URLs found in sitemap: " + colors.WARNING + str(len(sitemap_urls)) + colors.ENDC)
            return sitemap_urls
        else:
            print(colors.FAIL + "[✗] Sitemap.xml not found (Status code: " + str(r.status_code) + ")" + colors.ENDC)
            return []
    except Exception as e:
        print(colors.FAIL + "[✗] Error accessing sitemap: " + colors.WARNING + str(e) + colors.ENDC)
        return []

def main():
    banner()
    enable_save = 0
    robots_filename = ""
    sitemap_filename = "sitemap.txt"
    sitemap_mode = False

    if len(sys.argv) == 1:
        print(colors.FAIL + "ERROR: No domain or parameters found" + colors.ENDC)
    elif len(sys.argv) == 2:
        arg = sys.argv[1]
        
        if arg == "-h" or arg == "--help":
            print(colors.BOLD + "HELP SECTION:" + colors.ENDC)
            print("Usage:" + colors.OKCYAN + '\trobotscraper.py domain' + colors.ENDC)
            print("Example:" + colors.OKCYAN + '\trobotscraper.py example.com -s output.txt' + colors.ENDC)
            print("-d,--domain" + colors.OKCYAN + "\tSpecifies the domain" + colors.ENDC)
            print("-h,--help" + colors.OKCYAN + "\tThis help" + colors.ENDC)
            print("-v,--version" + colors.OKCYAN + "\tShow version" + colors.ENDC)
            print("-s,--save" + colors.OKCYAN + "\tEnable save output and specifies the output file for robots.txt results" + colors.ENDC)
            print("-m,--mode" + colors.OKCYAN + "\tSpecify mode: robots (default) or sitemap" + colors.ENDC)
            print(colors.OKCYAN + "Note: When no mode is specified, both robots.txt and sitemap.xml will be checked" + colors.ENDC)
        elif arg == "-v" or arg == "--version":
            print(colors.WARNING + "RobotScraper v.1.1" + colors.ENDC)
        else:
            print(colors.FAIL + "ERROR: Incorrect argument or syntax" + colors.ENDC)

    elif len(sys.argv) > 2:
        if sys.argv[1] == "-d" or sys.argv[1] == "--domain":
            domain = sys.argv[2]
            
            for i in range(3, len(sys.argv)):
                if sys.argv[i] == "-s" or sys.argv[i] == "--save":
                    if i+1 < len(sys.argv):
                        enable_save = 1
                        robots_filename = sys.argv[i+1]
                elif sys.argv[i] == "-m" or sys.argv[i] == "--mode":
                    if i+1 < len(sys.argv):
                        if sys.argv[i+1].lower() == "sitemap":
                            sitemap_mode = True

            if sitemap_mode:
                # Sadece sitemap modu
                getSitemap(domain, enable_save, robots_filename)
            else:
                # Hem robots.txt hem de sitemap.xml'i kontrol et
                print(colors.OKGREENL + "\n[+] Checking robots.txt..." + colors.ENDC)
                getRobots(domain, enable_save, robots_filename)
                
                print(colors.OKGREENL + "\n[+] Checking sitemap.xml..." + colors.ENDC)
                # Sitemap sonuçlarını her zaman sitemap.txt'ye kaydet
                getSitemap(domain, 1, sitemap_filename)
if __name__ == "__main__":
    main()
