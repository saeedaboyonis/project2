**Country  information APP**

In this app you could pass a country name and get some information about it, such as:

Country’s Full Name

Country’s Capital

Country’s Common Language

Country’s Currency Name

Country’s Currency rate (Base currency is EURO)


**Prerequisites**

The following items should be installed in your system:

1- Python 3 or newer

2- Command line tool

3- Docker


**To run it follow these instructions:**

1- Git all the app files to a directory in your system

2- Open command line and navigate to this directory

3- Run this command "docker build -t main ."

4- Then run "docker run -i -t -p 5000:5000 main"

5- Instead of 3+4 you can use docker-compose and run "docker-compose up --build"

6- Go to your browser and navigate to "http://localhost:5000/?country=CountryName"
  
7- you can replace 'CountryName' with any country name you want




  
