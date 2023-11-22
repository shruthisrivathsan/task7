from datetime import datetime
timestamp = datetime.now().strftime ("%Y-%m-%d, %H:%M:%S")
print(timestamp)
filename = "mydata " + timestamp +".text"
print(filename)
f =open(filename, "w")
f.write(timestamp)
f.close()
