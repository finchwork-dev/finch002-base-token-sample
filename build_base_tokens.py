import json,csv,sys
d=json.load(open(sys.argv[1]))['tokens'][:int(sys.argv[2])]
w=csv.writer(open(sys.argv[3],'w',newline=''))
w.writerow(['chainId','address','name','symbol','decimals'])
for t in d: w.writerow([t['chainId'],t['address'],t['name'],t['symbol'],t['decimals']])
