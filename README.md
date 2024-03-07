# Summary

Build a docker container image from the provided docker file and then run the docker container, along with an IP address, to retrieve the latitude and longitude of the IP address from IPStack.  

# What are the files in this repository?

* GeoIP.py: The base python program that queries the IPStack API and returns the latitude and longitude of an IP address that is provided from a command line parameter

* Dockerfile: The Docker file that has python3 installed on a debian linux base image, copies the GeoIP program file into the "/" directory, installs "requests" python library, and executes the program once the container has been built and run. 


# Prerequisite



Docker installed on the device you are cloning this repo on. 


# How to Use

* Build command:
  * docker build -t geoipimg .
  
* Run command:
    * docker run geoipimg “IP Address”

* **_Note: If you don’t provide an IP Address as a parameter/argument in the command line, executing your command will return the expected arguments/parameters that need to be provided in the command line_**

# Security Consideration

A free IPStack account was created for the purposes of this assignment, which does not support the use of http**s** in the browser URL. Thus, any API connection is unencrypted when running the container. Furthermore, The IPStack API access key is viewable in the source code of the GeoIP file for the purposes of this assignment, but in a production/test environment, it is imperative to have the access key stored somewhere else securely and should always be shared securely to prevent account and data theft and breaches. 
