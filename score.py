import yaml
import pandas as pd

stream=open('t20s/287853.yaml', 'r')

x=yaml.load(stream)

deliveries=x['innings'][0]['1st innings']['deliveries']
d=[]
for delivery in deliveries:
	key=list(delivery)[0]
	x=delivery[key]
	# print(x)
	total=x.pop('runs')['total']
	x.pop('wicket', '')
	x.pop('extras', '')
	x['runs']=total
	x['over']=key
	d.append(x)


x=pd.DataFrame(d)
print(x.shape)