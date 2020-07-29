# python-hierarchy

[![Python: 3.8](https://img.shields.io/badge/Python-3.8-blue.svg)](#)
[![license: MIT](https://img.shields.io/badge/license-MIT-orange.svg)](https://opensource.org/licenses/MIT)

The csv converter tool is meant to take in a traditional csv of hotels (as defined by Noken), and spit out a json that can be used for upload into the automation tool. This tool is menat to prevent coding and json creation on the content curation side of the busienss. 

Arguments:
    `-h`: help file of usage of the script
    `-f`: input file name
    `-c`: two didgit country code

    Default settings:
    `output_path` is the current directory

    Example:
    ```
    # Takes in a france.csv and country code
    >> python main.py -f /Users/Documents/CSVs/France.csv -c fr
    ```
