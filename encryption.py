

Conversation opened. 3 messages. All messages read.

Skip to content
Using MEST Mail with screen readers
Search



Click here to enable desktop notifications for MEST Mail.   Learn more  Hide
Mail
COMPOSE
Labels
Inbox (16)
Starred
Sent Mail
Drafts (5)
More 
Hangouts

 
 
  More 
1 of 401  
 
Expand all Print all In new window
Custom Encryption/Decryption System 
Inbox
x 

Ayodeji Oyinloye <ayodeji.oyinloye@meltwater.org>
Attachments3:11 PM (11 hours ago)

to me, Luqman, John 
Hi guys,

Find attached my code for the assignment. Feel free to share yours so we can compare methodologies and logic.

Kind Regards,
Oyinloye Ayodeji I.


Screen Shot 2016-07-28 at 10.28.19 AM.png
Ayodeji Oyinloye | Entrepreneur-in-Training
M: +233 265 231 422 | SKYPE: oyinloyeayodeji
Website: www.oyinloyeayodeji.com
www.meltwater.org
FacebookTwitter
Attachments area

John Otu		Attachments3:20 PM (10 hours ago)
Well done AY. Mine is attached. --

John Otu
Attachments10:15 PM (4 hours ago)

to Ayodeji, me, Luqman 
Hi guys,
I noticed that because I used the length of the key for encryption, my code will decrypt files with another key that has the same length as the original key. I have now edited it to work with distinct keys and have attached it below. Kindly review and let me know what i can change. Thanks

Attachments area
	
Click here to Reply, Reply to all, or Forward
0.3 GB (1%) of 30 GB used
Manage
Program Policies
Powered by Google
Last account activity: 27 minutes ago
Details
1 more
John Otu's profile photo
John Otu
john.otu@meltwater.org

Show details

def open_file(file):
    f = open(file)
    words = f.read()
    return words

def cipher(words,key):
    f = open("cipher_text.txt", "w")
    numbers =[]
    for i in words:
        num = ord(i) + key
        f.write(str(num)+",")
    f.close()

def decipher(file,key):
    ciphered = open_file(file)
    f = open("decipher_text.txt", "w")
    c=[]
    c = ciphered.split(",")
    for i in c:
        x = int(i)
        #print chr(x - key)
        f.write(chr(x-key))
    f.close()

text_file = open_file("text.txt")
cipher(text_file,5)
decipher("cipher_text.txt",6)
cipher.py
Open with Google Docs
Displaying cipher.py.
