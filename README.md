**Country  information APP**

In this app you could pass a country name and get some information about it, such as:

Country’s Full Name

Country’s Capital

Country’s Common Language

Country’s Currency Name

Country’s Currency rate (Base currency is EURO)


**Prerequisites**

The following items should be installed in your system:

1- python 3 or newer

2- command line tool

3- docker


**To run it follow these instructions:**

1- git all the app files to a directory in your system

2- open command line and navigate to this directory

3- run this command "docker build -t main ."

4- then run "docker run -i -t -p 5000:5000 main"

5- instead of 3+4 you can use docker-compose and run "docker-compose up --build"

6- go to your browser and navigate to "http://localhost:5000/?country='a country name'"
  
7- you can replace 'a country name' with any country name you want




  
