import subprocess
cmd = ['hostnamectl\n']
with open('/home/task/apache_ubuntu/files/index.html.j2', 'w') as out:
    return_code = subprocess.call(cmd, stdout=out)
