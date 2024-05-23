
#A ditionary is a special structure that allows us to store data in key-value pairs.
monthConversions = {
        "Jan": "January",
        "Feb": "February",
        "Mar": "March",
        "Apr": "April",
        "May": "May",
        "Jun": "June",
        "Jul": "July",
        "Aug": "August",
        "Sep": "September",
        "Oct": "October",
        "Nov": "November",
        "Dec": "December"
}

#This is for invalid input values.
print(monthConversions.get("Dec" , "Not a valid key"))


