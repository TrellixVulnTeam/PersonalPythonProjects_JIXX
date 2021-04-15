from envelopes import Envelope, GMailSMTP

envelope = Envelope(
    from_addr=(u'elijahrobomail000@gmail.com', u'From Example'),
    to_addr=(u'to@example.com', u'To Example'),
    subject=u'Envelopes demo',
    text_body=u"I'm a helicopter!"
)

# Send the envelope using an ad-hoc connection...
envelope.send('smtp.googlemail.com', login='elijahrobomail000@gmail.com',
              password='Amadeuppassword', tls=True)

# Or send the envelope using a shared GMail connection...
gmail = GMailSMTP('elijahrobomail000@gmail.com', 'Amadeuppassword')
gmail.send(envelope)

#elijahrobomail000@gmail.com
#Amadeuppassword