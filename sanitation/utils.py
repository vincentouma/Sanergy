import africastalking as af

def send_bill_receipt(bill):
        # Initialize SDK
    username='sanergy'
    api_key='7724f7cb28239d2244aa9af7c28313283732507bf9ebc30706951d8d1a011517'

    af.initialize(username, api_key)

    # Initialize a service e.g. SMS
    receipt = af.SMS
    # Use the service synchronously

    customers = [                          
        "+"+str(bill.phone_number),
    ]
    message=f'Confirmed you have payed Ksh{bill.amount} on {bill.timestamp} through {bill.phone_number} for your toilet . Thank you for being a faithfull customer.'
    response = receipt.send(message, customers)
    print(response)

