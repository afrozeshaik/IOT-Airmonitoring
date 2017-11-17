from datetime import datetime
import matplotlib.pyplot as plt


datetime_object = datetime.strptime('Apr 24 13:30:26 2017', '%b %d %H:%M:%S %Y')

with open('GPSCordinates.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 
times=[]
conc=[]
fintimes=[]
fincon=[]
#print content[1].strip().split()
for i in xrange(1,len(content)):
	conc.append(float(content[i].strip().split()[4]))
	a=content[i].strip().split()
	times.append(a[11]+' '+a[12]+' '+a[13]+' '+a[14])
for i in xrange(len(times)):
	if i%2==0:
		fintimes.append(times[i][:-1])
		fincon.append(conc[i])
for i in xrange(len(fincon)):
	print fintimes[i],fincon[i]

	

dateobj=[]
for i in xrange(len(fintimes)):
	dateobj.append(datetime.strptime(fintimes[i], '%b %d %H:%M:%S %Y'))

plt.plot(dateobj,fincon)
plt.xlabel('Time')
plt.ylabel('Ammonia Concentration (PPM)')
plt.show()




#Apr 24 13:30:26 2017
#datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
#10,11,12,13,14'''