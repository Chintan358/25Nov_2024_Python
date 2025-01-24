import pywhatkit
 

try:
   
  # sending message to receiver
  # using pywhatkit
  pywhatkit.sendwhatmsg("+919265117502", 
                        "Hello from GeeksforGeeks", 
                        22, 28)
  print("Successfully Sent!")
 
except:
   
  # handling exception 
  # and printing error message
  print("An Unexpected Error!")