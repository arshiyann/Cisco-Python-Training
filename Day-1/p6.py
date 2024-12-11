s_sname = input =(f"Enter Shell Name: ")
rframe = ""
if s_sname == "bash":
   rframe = "bash"
elif s_sname == "ksh":
   rframe = "ksh"
elif s_sname == "csh":
   rframe = "csh"
else:
   
   print("No Login")
   rframe = "/etc/profile"

print(f'Entering {rframe} bash shell')