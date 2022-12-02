import shutil

du = shutil.disk_usage("/")

# disk space
print("Your total disk space ->", du)

# amount of free dispace space in percentage
print("Free disk space % : ", round(du.free/ du.total * 100))

