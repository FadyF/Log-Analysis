#Log Analysis Project


##Project Description:

   Creation of a reporting tool; which ia python code; that prints out reports based on the datat that exist in the database.
   there were three questions given to answer.


###These question are:

  * What are the most popular three articles of all time? 
  * Who are the most popular article authors of all time?  
  * On which days did more than 1% of requests lead to errors? 

##Project Installation:

  * Vagrant 
  * VirtualBox 
  * vagrant-setup files given in the nanodergree
  * Database setup <a> [https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip]</a> downloaded and unzipped
  * unzipped file newsdata.sql file put in vagrant directory
  
  
## Usage

  * To start the Virtual Machine head to vagrant directory
  * Run `vagrant up` to build the virtual machine then run `vagrant ssh` to connect
  * Head the to newsdata.sql file directory and use the command:
     
    `psql -d news -f newsdata.sql`

  ####Now the database is loaded.
  
  * By running the command: `\d` you can see the contents of the tables

  * To run this project run command : `python News.py`

 
   