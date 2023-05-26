# MITRE Techniques Fetcher

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Fetch all up-to-date MITRE data directly from the [MITRE official website](https://attack.mitre.org/)

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/TalKatz1/MITRE-Techniques-Fetcher.git
   ``` 

2. Navigate to the project directory:

   cd MITRE-Techniques-Fetcher

3. Install the dependencies:

   pip install -r requirements.txt

## Usage

1. Run the script:

   ```python
   python mitre_fetch.py
   ```

   * Use the `--add-sub-techniques` flag to include sub-techniques (optional).
   * Use the `--to-json` flag to save output on a json file (optional).
   * Use the `--to-csv` flag to save output on a csv file (optional).

   if none of the output flags isn't in use, the raw data will be printed in terminal.

2. View the results

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please create an issue or submit a pull request.

## License

The source code for the site is licensed under the MIT license, which you can find in the [LICENSE](LICENSE) file.
