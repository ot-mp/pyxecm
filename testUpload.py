from pyxecm import otcs	
import random

File_Path = "C:\\test.txt"

Self_OTCS = otcs.OTCS("http","1.9.1.","80",None,"Ad","ad","Content Server Members","cs","X3",None,"/CS/cs.exe",3,"/tmp/contentserver",None)

otcs.OTCS.authenticate(Self_OTCS)

Resulter = otcs.OTCS.upload_file_to_parent(Self_OTCS,File_Path,"doc"+str(random.uniform(0,1)),None,244444,None)

Node_id = Resulter.get("results").get("data").get("properties").get("id")

print(Node_id)