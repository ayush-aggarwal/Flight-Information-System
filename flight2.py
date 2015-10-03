import pymongo
import MySQLdb
db1=MySQLdb.connect("localhost","root","1","flight")
con=db1.cursor()
client=pymongo.MongoClient()
db=client.test
flight=db.flight
sql="DELETE FROM `flight_details`;"
con.execute(sql)
db1.commit()
res=list(flight.find())
for r in res:
	f=""
	for i in range(0,len(r["flight_details"])):
		f=f+str(r["flight_details"][i]["flight_no"])+","
	f=f[:len(f)-1]
	print f
	sql="INSERT INTO `flight_details` (`Source`,`Source Code`,`Destination`,`Destination Code`,`Departure`,`Arrival`,`Flight Numbers`,`Duration`,`Fare`,`Class`,`Baggage`) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%d','%s','%s');"%(str(r["source"]),str(r["source_code"]),str(r["destination"]),str(r["destination_code"]),str(r["flight_details"][0]["depart_time"]),str(r["flight_details"][len(r["flight_details"])-1]["arrival_time"]),str(f),str(r["total_duration"]),int(r["total_fare"]),str(r["classtype"]),str(r["baggage"]))
	con.execute(sql)
	db1.commit()
