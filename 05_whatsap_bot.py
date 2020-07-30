from twilio.rest import Client 
 
account_sid = 'AC18ed71c33f4207cf7803248aa92de66a' 
auth_token = '8034bd2d378707e73a8c84f4aaed2ac9' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Your Yummy Cupcakes Company order of 1 dozen frosted cupcakes has shipped and should be delivered on July 10, 2019. Details: http://www.yummycupcakes.com/',      
                              to='whatsapp:+17175992268' 
                          ) 
 
print(message.sid)


client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Hello! This is an editable text message. You are free to change it and write whatever you like.',      
                              to='whatsapp:+17175992268' 
                          ) 
 
print(message.sid)