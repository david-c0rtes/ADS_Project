# Project Name - Pied Piper 
Pied Piper is a platform that contains all club related opportunities/leadership positions 

Our platform has two main functions:
1. It allows club representatives looking to hire to post available job positions at their clubs
2. It allows IE Students to search among the available positions to find their ideal job



# INSTALLATION
To be able to run our program, make sure you have the following things installed:

  - Python programming language - It will work in all versions between 3.6 and 3.8. 
  - Libraries - In order to run our program, we make use of the following 2 libraries: heapq_max and re  
        To download the library type the following command   
    ```pip install heapq_max ``` 
  
  Now that we have the required libraries set up, open the file named app.py and run the program. 

# USAGE
After a user enters our platform, they will be welcomed and asked what their intentions are:   
 - Posting a new job    
 - Searching for a job   
 - Closing an existing job position   
 
The user will now have to enter their choice. After their choice is validated, the respective action will be carried out and the user will be asked more questions based on their choice. 


1) Posting a new job: - Our job inserting function has the purpose of enabling club representatives to upload available job positions.   
    - The user will first be asked to enter some details about the job
    - **User input**: A job title, the position, the club, the location (Madrid, Segovia or Online), an email address, the time of the year (spring or fall), and a job description.  
    - **Output**: A confirmatory message saying that the job has been added.   


2) Searching for a job: -  Our job searching function has the purpose of showing IE students the available job positions that best match their preferences.
    - It will start by displaying a list with all available positions showing only unique titles.  
    - **User Input**: The interested position (which needs to be chosen from the above list), the preferred location (Madrid, Segovia or Online), and the time of the year (spring or fall).  
    - **Output**: Job options that best match the user's preferences displayed in descending order of priority. The jobs that share no priorities will be filtered out.  


3) Deleting an existing job: - Our job deleting function has the purpose of enabling club representatives to remove an existing job post that has already been filled in.  
    - First, the user will be shown a list of all available job positions  
    - **User Input**: Name of the job that the user wishes to close.   
    - **Output**: Confirmatory message saying that the job has been deleted.  




# SOME EXTRA INFORMATION ABOUT THE CODE
In order to carry out our objective, we have used the following data structures:

  1. Hash Tables - Used to store all details regarding the opportunities 
  2. Heaps - used to find the most appropriate opportunity for the user based on their preferences  

And the following Algorithms:

  1. Insertion 
  2. Deletion 
  3. Searching 


# CREDITS
The authors for this project are:   
Abdul Salam  
Anshumaan Ravi  
Isabel Ordovas  
Natalia Caceres   
Natalia Nowak   




