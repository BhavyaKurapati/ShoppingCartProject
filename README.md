implementation base on the http://automationpractice.com/index.php webpage.

**Softwares installed**
Browsers: chrome, firefox
selenium==4.4.3
pytest==7.1.3
webdriver-manager==3.8.3

**Process to be followed**

1. Clone the project
2. create virtual environment 
3. open terminal with created virtual environment and install the packages(using requirements.txt)

**Running tests**

Enter tests folder and use pytest command to run the tests(tests are categorized as positive and negative)
Ex: Use following command to run and generate html reports
pytest -v Test_Login.py --html=Test_Login.html
