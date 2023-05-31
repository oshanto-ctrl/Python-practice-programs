"""
Write a while loop that asks people why they like programming.
Each time someone enters a reason, add their reason to a file
that stores all the response
"""

filename = "pollresponse.txt"

def store_response(response):
    with open(filename, 'a') as file_obj:
        file_obj.write(f"'{response.strip()}'\n")
        file_obj.write(f"\n")
        
while(True):
    prompt = f"Why you like programming?:"
    response = input(prompt)
    store_response(response)
    continue_response = input("Like to let someone else resonse (y/n)")
    if continue_response != 'y':
        break
    else:
        response = ""

    print("[response stored]")

print("<<<ENDS>>>")