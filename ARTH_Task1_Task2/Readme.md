
## Task 1- ## 
Does client takes the entire data to master or does master provides the IP addresses of Datanodes so that client can upload the file to the Datanodes. 
Question- Who is the one uploading the file?
Answer- Client gets the IP from Master and uploads the file to DataNode.

## Task 2- ##
Question: Does client go to master and then read the file on slave via Master or Does Client go to slave directly and read the data?
Answer: Client goes to slave directly and reads the data stored on slave.

## Task 3- ##
ARTH- The School Of Technologies

✴️ Setup a Hadoop cluster with one NameNode(Master) and 4 DataNodes(Slave) and one Client Node.

✴️ Upload a file through client to the NameNode.

✴️ Check which DataNode the Master chooses to store the file.

✴️ Once uploaded try to read the file through Client using the cat command and while Master is trying to 
access the file from that DataNode where it stored the file delete that DataNode  or crash it and see with
help of the replicated storage how master retrieves the file and present it to client.


