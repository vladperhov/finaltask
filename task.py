import subprocess
cmd = ['hostnamectl']
with open('/home/task/index.html', 'w') as out:
    return_code = subprocess.call(cmd, stdout=out)
