# cowin_api_slot_lookup
Lookup vaccination slots with mailer notification at frequent intervals\n

Run the cowin_api_invoke.py code post modifying the following arguments:
 1.District ID-If it is unknown then lookup the id master for the apt district and paste its id 
 2.Age
 3.Number of days to iterate for searching the vaccination availability
 4.From Email address
 5.To Email Address
 6.Email Password
 7.Time to halt before next iteration
 8. Mailing Activity[if 'y' or 'Y' then the entire list for the apt group containing free spots and date is mailed] else the details of  only those vaccination spots will be mailed that have free spots.
 
The current code has been tested only on gmail.com mail domain.For other domains the code cowin_api_fetch.py needs to be altered[Line no.80]
