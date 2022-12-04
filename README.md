<br />
<a name="readme-top"></a>
<div align="center">

  <h3 align="center">Invoice Generator</h3>

  <p align="center">
    A small program to price a cart of products and apply available discounts.
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#quick-start">Quick Start</a></li>
      </ul>
    </li>
    <li><a href="#customization">Customization</a></li>
    <li><a href="#future-improvements">Future Improvements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This program is a small project to price a cart of products and apply available discounts. The program is written in Python.
It accepts a list of products(in given datasets) and returns the total price of the cart. The program also applies pre-set discounts to the cart.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

This project is built with Python 3. The program uses the following libraries: json, collections.

[![Python][Python]][python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

Install Python 3.8 or higher.
Please refer to the [official Python documentation](https://www.python.org/) for installation instructions.

### Quick Start

1. Clone the repo to your local machine
   ```sh
   git clone https://github.com/lht19900714/Invoice-Generator.git
   ```
2. change directory to the project folder
   ```sh
   cd Invoice_Generator
   ```
3. Run the program
   ```sh
    python3 main.py --products=<product_name>
    ```
    where <product_name> is the name of the product in the dataset. The program accepts multiple products as arguments.
    ```sh
    python3 createCart --products=<product_name1> --products=<product_name2> --products=<product_name3>
    ```
<br />
If you want to run this program with typing "python3", you can do following steps.

1. make the main.py file executable
   ```sh
   chmod +x createCart
   ```
   
2. Run the program
   ```sh
    ./createCart --products=<product_name>
    ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Customization

The datasets are stored in the data folder. You can add new products and discounts to the datasets. 
The program will automatically apply the discounts to the cart.
Make sure to follow the format of the datasets.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Future Improvements

1. Add unit tests
2. Add more exception handling

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[python-url]: https://www.python.org/
[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
