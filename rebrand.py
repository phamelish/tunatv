import os
import re

dir = '/home/carlos/Documents/tunatv/training_site/donate.html'


with open(dir, 'r') as file:
	file_contents = file.read()

modified_contents = re.sub(re.escape('tunatv'), 'Elotelevision', file_contents, flags=re.IGNORECASE)

with open(dir, 'w') as file:
	file.write(modified_contents)
