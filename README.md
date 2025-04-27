<h1 align="center">
  <br>
  <a href="https://github.com/robotshell/robotScraper"><img src="https://i.ibb.co/41MDdWD/robotscraper.png" alt="robotScraper" style="width:100%"></a>
</h1>

## Description

RobotScraper is an open-source tool designed to scrape and analyze both the `robots.txt` and `sitemap.xml` files of a specified domain. This Python script helps in identifying directories and pages that are allowed or disallowed by the `robots.txt` file, as well as all URLs listed in the `sitemap.xml` file. Results can be saved to output files for further analysis. It is useful for web security researchers, SEO analysts, and anyone interested in examining the structure and access rules of a website.

## Requirements

- Python 3.x
- `requests` package
- `beautifulsoup4` package
- `xml.etree.ElementTree` (included in Python standard library)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/robotshell/robotScraper
    cd robotScraper
    ```

2. Install the required Python packages:
    ```sh
    pip install requests beautifulsoup4
    ```

## Usage

To run the RobotScraper, you can use the following command syntax:

```sh
python robotScraper.py -d domain [-s output.txt] [-m mode]
```

### Parameters

- `-d, --domain`: Specifies the target domain to analyze
- `-s, --save`: Enable saving output and specify the output file for robots.txt results
- `-m, --mode`: Specify the mode: `robots` (default) or `sitemap`

### Examples

```sh
# Check both robots.txt and sitemap.xml (sitemap results saved to sitemap.txt)
python robotScraper.py -d example.com

# Check only robots.txt and save results to output.txt
python robotScraper.py -d example.com -s output.txt

# Check only sitemap.xml and save results to urls.txt
python robotScraper.py -d example.com -m sitemap -s urls.txt
```

### Features

- Extracts and analyzes all entries from robots.txt
- Extracts all URLs from sitemap.xml, including nested sitemaps
- Verifies the accessibility of found URLs
- Handles SSL certificate verification issues
- Color-coded terminal output for better readability
- Saves results to specified output files

# Disclaimer
This tool is intended for educational and research purposes only. The author and contributors are not responsible for any misuse of this tool. Users are advised to use this tool responsibly and only on systems for which they have explicit permission. Unauthorized access to systems, networks, or data is illegal and unethical. Always obtain proper authorization before conducting any kind of activities that could impact other users or systems.
