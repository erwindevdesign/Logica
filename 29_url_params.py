import re

#url =  "https://retosdeprogramacion.com?year=2023&challenge=0&languaje=python"
url = input("Input the url to check: ")

components = url.split("&")

""" This code extracts the parameters from a URL using both 
split method and regular expression. The split methos separates
the URL into components separated by `&`, and then it looks for 
components containing a parameter using the `=` character. If
a parameter is found, it is extrated and printed. The regular 
expression method uses the `re.findall()` funtion to search 
parameter values using a regular expression pattern. The 
pattern matches strings that start with `=` and contain one or 
more alphanumeric characters, dots, underscores, percentage 
signs, or hyphens.

Returns: 
    - None
"""

for component in components:
    if "=" in component:
        param = component.split("=")
        if len(param) == 2 and param[1] != "":
            print(param[1])
            
regex = r"=([a-zA-Z0-9._%-]+)"
params = re.findall(regex, url)
print(params)