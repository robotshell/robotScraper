<h1 align="center">
  <br>
  <a href="https://github.com/robotshell/robotScraper"><img src="https://i.ibb.co/41MDdWD/robotscraper.png" alt="robotScraper" style="width:100%"></a>
</h1>

## Description

RobotScraper is an open-source tool designed to scrape and analyze the `robots.txt` file of a specified domain. This Python script helps in identifying directories and pages that are allowed or disallowed by the `robots.txt` file and can save the results if needed. It is useful for web security researchers, SEO analysts, and anyone interested in examining the structure and access rules of a website.

## Requirements

- Python 3.x
- `requests` package
- `beautifulsoup4` package

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
python robotScraper.py domain [-s output.txt]
