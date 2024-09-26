from melipayamak import Api

username = '9372064133'
password = 'MTC4Z'

def send_sms(to, text, bodyId):
    api = Api(username,password)
    sms_soap = api.sms('soap')
    sms_soap.send_by_base_number(text, to, bodyId)

    return