import pymongo
import MySQLdb
db1=MySQLdb.connect("localhost","root","1","flight")
con=db1.cursor()
client=pymongo.MongoClient()
db=client.test
flight=db.flight
sql="DELETE FROM `flight_number`;"
con.execute(sql)
db1.commit()
res=list(flight.find())
print len(res)
l=[]
ctr=0
for r in res:
	if len(r["flight_details"])==1:
		print r
		try:
			sql="INSERT INTO `flight_number`(`Airlines`,`Flight No`,`Source`,`Source Code`,`Destination`,`Destination Code`,`Duration`,`Departure Time`,`Arrival Time`,`class`,`Fare`) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%d');"%(str(r["flight_details"][0]["airlines"]),str(r["flight_details"][0]["flight_no"]),str(r["flight_details"][0]["inter_source"]),str(r["flight_details"][0]["inter_source_code"]),str(r["flight_details"][0]["inter_destination"]),str(r["flight_details"][0]["inter_destination_code"]),str(r["flight_details"][0]["duration"]),str(r["flight_details"][0]["depart_time"]),str(r["flight_details"][0]["arrival_time"]),str(r["classtype"]),int(r["total_fare"]))
			con.execute(sql)
			db1.commit()
		except:
			sql="INSERT INTO `flight_number`(`Airlines`,`Flight No`,`Source`,`Source Code`,`Destination`,`Destination Code`,`Duration`,`Departure Time`,`Arrival Time`,`Fare`) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%d');"%("N/A",str(r["flight_details"][0]["flight_no"]),str(r["flight_details"][0]["inter_source"]),str(r["flight_details"][0]["inter_source_code"]),str(r["flight_details"][0]["inter_destination"]),str(r["flight_details"][0]["inter_destination_code"]),str(r["flight_details"][0]["duration"]),str(r["flight_details"][0]["depart_time"]),str(r["flight_details"][0]["arrival_time"]),int(r["total_fare"]))
			con.execute(sql)
			db1.commit()
for r in res:
	if len(r["flight_details"])!=1:
		for i in range(0,len(r["flight_details"])):
			fno=str(r["flight_details"][i]["flight_no"])
			sql="SELECT COUNT(*) FROM `flight_number` WHERE `Flight No`='%s';"%(str(fno))
			con.execute(sql)
			res=con.fetchone()
			if int(res[0])==0:
				try:
					sql="INSERT INTO `flight_number`(`Airlines`,`Flight No`,`Source`,`Source Code`,`Destination`,`Destination Code`,`Duration`,`Departure Time`,`Arrival Time`,`class`) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');"%(str(r["flight_details"][i]["airlines"]),str(r["flight_details"][i]["flight_no"]),str(r["flight_details"][i]["inter_source"]),str(r["flight_details"][i]["inter_source_code"]),str(r["flight_details"][i]["inter_destination"]),str(r["flight_details"][i]["inter_destination_code"]),str(r["flight_details"][i]["duration"]),str(r["flight_details"][i]["depart_time"]),str(r["flight_details"][i]["arrival_time"]),str(r["classtype"]))
					con.execute(sql)
					db1.commit()
				except:
					sql="INSERT INTO `flight_number`(`Airlines`,`Flight No`,`Source`,`Source Code`,`Destination`,`Destination Code`,`Duration`,`Departure Time`,`Arrival Time`,`Fare`) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%d');"%("N/A",str(r["flight_details"][i]["flight_no"]),str(r["flight_details"][i]["inter_source"]),str(r["flight_details"][i]["inter_source_code"]),str(r["flight_details"][i]["inter_destination"]),str(r["flight_details"][i]["inter_destination_code"]),str(r["flight_details"][i]["duration"]),str(r["flight_details"][i]["depart_time"]),str(r["flight_details"][i]["arrival_time"]),int(r["total_fare"]))
					con.execute(sql)
					db1.commit()

