from zope.interface import Interface, implements


class IMailmanHandler(Interface):
    ''' Interface for mailman handler '''


class MailmanHandler(object):
    implements(IMailmanHandler)
    ''' utility class to comunicate with mailman server '''

    def subscribe(self, mail):
        print mail
        return True

    def unsubscribe(self, mail):
        print mail
        return True

    def sendMessage(self, message):
        # come posso tornare eccezioni all'interno dell'utility
        print message
        return True