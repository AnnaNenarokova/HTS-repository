#!/usr/bin/python3
import enasearch
from collections import OrderedDict

wgs = ['SAMEA2619399', 'SAMEA2591057', 'SAMEA2591132', 'SAMEA2591107', 'SAMEA2619531', 'SAMEA2619686', 'SAMEA2619791', 
	'SAMEA2619854', 'SAMEA2591084', 'SAMEA2619857', 'SAMEA2591122', 'SAMEA2619802', 'SAMEA2619677', 'SAMEA2619747', 
	'SAMEA2591074', 'SAMEA2619766', 'SAMEA2619815', 'SAMEA2619818', 'SAMEA2619678', 'SAMEA2619840', 'SAMEA2619782', 
	'SAMEA2619838', 'SAMEA2619952', 'SAMEA2619950', 'SAMEA2619779', 'SAMEA2619667', 'SAMEA2619903', 'SAMEA2619923', 
	'SAMEA2619962', 'SAMEA2619879', 'SAMEA2591108', 'SAMEA2620014', 'SAMEA2619376', 'SAMEA2619888', 'SAMEA2619927', 
	'SAMEA2619548', 'SAMEA2619907', 'SAMEA2620836', 'SAMEA2620666', 'SAMEA2620852', 'SAMEA2620894', 'SAMEA2620756', 
	'SAMEA2620734', 'SAMEA2620890', 'SAMEA2620651', 'SAMEA2620786', 'SAMEA2620542', 'SAMEA2620672', 'SAMEA2620828', 
	'SAMEA2620815', 'SAMEA2620273', 'SAMEA2620094', 'SAMEA2620384', 'SAMEA2620413', 'SAMEA2620210', 'SAMEA2620404', 
	'SAMEA2620259', 'SAMEA2620339', 'SAMEA2620004', 'SAMEA2620027', 'SAMEA2620198', 'SAMEA2620256', 'SAMEA2620039', 
	'SAMEA2620078', 'SAMEA2620035', 'SAMEA2620081', 'SAMEA2620194', 'SAMEA2620097', 'SAMEA2620021', 'SAMEA2619974', 
	'SAMEA2620065', 'SAMEA2620106', 'SAMEA2620227', 'SAMEA2620588', 'SAMEA2621213', 'SAMEA2620230', 'SAMEA2619970', 
	'SAMEA2621003', 'SAMEA2621242', 'SAMEA2621232', 'SAMEA2621204', 'SAMEA2621198', 'SAMEA2621229', 'SAMEA2621203', 
	'SAMEA2621278', 'SAMEA2621277', 'SAMEA2621272', 'SAMEA2621221', 'SAMEA2621222', 'SAMEA2621085', 'SAMEA2621176', 
	'SAMEA2621132', 'SAMEA2621216', 'SAMEA2621173', 'SAMEA2621066', 'SAMEA2621076', 'SAMEA2621075', 'SAMEA2621107', 
	'SAMEA2621061', 'SAMEA2621155', 'SAMEA2621099', 'SAMEA2621101', 'SAMEA2621092', 'SAMEA2621151', 'SAMEA2621037', 
	'SAMEA2621191', 'SAMEA2620979', 'SAMEA2620967', 'SAMEA2620950', 'SAMEA2620995', 'SAMEA2620970', 'SAMEA2620947', 
	'SAMEA2621033', 'SAMEA2620991', 'SAMEA2620882', 'SAMEA2621021', 'SAMEA2621020', 'SAMEA2620861', 'SAMEA2620925', 
	'SAMEA2621045', 'SAMEA2620929', 'SAMEA2621044', 'SAMEA2620879', 'SAMEA2621448', 'SAMEA2621254', 'SAMEA2621259', 
	'SAMEA2621295', 'SAMEA2622021', 'SAMEA2621536', 'SAMEA2621779', 'SAMEA2621287', 'SAMEA2621839', 'SAMEA2621423', 
	'SAMEA2621487', 'SAMEA2621271', 'SAMEA2622197', 'SAMEA2622219', 'SAMEA2621990', 'SAMEA2621812', 'SAMEA2622074', 
	'SAMEA2622119', 'SAMEA2622149', 'SAMEA2591098', 'SAMEA2621509', 'SAMEA2621401', 'SAMEA2622097', 'SAMEA2621859', 
	'SAMEA2622357', 'SAMEA2622048', 'SAMEA2621260', 'SAMEA2622362', 'SAMEA2622545', 'SAMEA2622694', 'SAMEA2622402', 
	'SAMEA2622336', 'SAMEA2622331', 'SAMEA2622696', 'SAMEA2622695', 'SAMEA2622478', 'SAMEA2622677', 'SAMEA2622452', 
	'SAMEA2622518', 'SAMEA2622690', 'SAMEA2622656', 'SAMEA2622678', 'SAMEA2622657', 'SAMEA2622376', 'SAMEA2622568', 
	'SAMEA2622673', 'SAMEA2622429', 'SAMEA2623488', 'SAMEA2623155', 'SAMEA2620570', 'SAMEA2623390', 'SAMEA2623135', 
	'SAMEA2623098', 'SAMEA2623079', 'SAMEA2623370', 'SAMEA2623295', 'SAMEA2623314', 'SAMEA2623116', 'SAMEA2623350', 
	'SAMEA2622901', 'SAMEA2623275', 'SAMEA2622841', 'SAMEA2622842', 'SAMEA2622843', 'SAMEA2622800', 'SAMEA2622716', 
	'SAMEA2622801', 'SAMEA2622799', 'SAMEA2622738', 'SAMEA2622796', 'SAMEA2622715', 'SAMEA2622837', 'SAMEA2622821', 
	'SAMEA2622658', 'SAMEA2622710', 'SAMEA2622652', 'SAMEA2622736', 'SAMEA2622737', 'SAMEA2622822', 'SAMEA2622823', 
	'SAMEA2622763', 'SAMEA2622817', 'SAMEA2622733', 'SAMEA2622764', 'SAMEA2622765', 'SAMEA2623426', 'SAMEA2623446', 
	'SAMEA2623513', 'SAMEA2623693', 'SAMEA2623794', 'SAMEA2623673', 'SAMEA2623649', 'SAMEA2623463', 'SAMEA2623907', 
	'SAMEA2623808', 'SAMEA2623756', 'SAMEA2623734', 'SAMEA2623850', 'SAMEA2623826', 'SAMEA2623868', 'SAMEA2623919', 
	'SAMEA2623774', 'SAMEA2623886', 'SAMEA2620855', 'SAMEA2620217', 'SAMEA2620000', 'SAMEA2621013', 'SAMEA2619935', 
	'SAMEA2622759', 'SAMEA2622676', 'SAMEA2622173', 'SAMEA2622316', 'SAMEA2622499', 'SAMEA2622923', 'SAMEA2623059', 
	'SAMEA2623627', 'SAMEA2620980', 'SAMEA2621548', 'SAMEA2621551', 'SAMEA2620812']

with open('/home/kika/tara/depth_2.tsv', 'w') as out:
	for i in wgs:
		print(i)
		a = enasearch.retrieve_data(
				ids='{}'.format(i),
				display='xml')
		b = OrderedDict()
		for key in a.keys():
			b = a[key] 
		c = OrderedDict()
		for key in b.keys():
			c = b[key]
		d = OrderedDict()
		for key in c.keys():
			if 'SAMPLE_ATTRIBUTE' in key:
				d = c[key]
		e = OrderedDict()
		for key in d.keys():
			e = d[key][24]
		for key in e.keys():
			if 'VALUE' in key:
				print('found')
				out.write('{}\t{}\n'.format(i, e[key]))
