import pprint
d ={}
d ['K1'] = [{'url':'cisco.com','port':80,'IP':'1.2.3.4'},{'url':'meraki.com','port':90,'IP':'122.3.4'}]
#ßd['K2'] = {{'K1':}}

pprint.pprint(d)

print(d['K1'][1]['port'])