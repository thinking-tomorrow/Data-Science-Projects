import yaml
import pandas as pd

stream=open('t20s/287853.yaml', 'r')

def get_innings(inning_name):
	x=yaml.load(stream)
	deliveries=x['innings'][int(inning_name[0])][inning_name]['deliveries']
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

	return pd.DataFrame(d)


def get_match_data():
	ing_1=get_innings('1st innings')
	ing_2=get_innings('2nd innings')

	df=ing_1.concat(ing_2)
	return df


a=get_match_data()
print(a)