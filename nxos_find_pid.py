out=json.loads(clid('show inv'))
for PID in out['TABLE_inv']['ROW_inv']:
  if PID['productid'] == "N9K-C9236C":
     print PID['productid']
