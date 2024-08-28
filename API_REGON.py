#Pobieranie danych  API REGON
from zeep import Client, Settings
from zeep.transports import Transport
from requests import Session
import xml.etree.ElementTree as ET
wsdl ='https://wyszukiwarkaregontest.stat.gov.pl/wsBIR/wsdl/UslugaBIRzewnPubl-ver11-test.wsdl'

session = Session()
transport = Transport(session=session)
settings = Settings(strict=False, xml_huge_tree=True)
client = Client(wsdl=wsdl, transport=transport, settings=settings)
sid = client.service.Zaloguj('abcde12345abcde12345')

if sid:
    client.transport.session.headers.update({'sid': sid})
sesja = client.service.GetValue('StatusSesji')
print(sesja)
if sesja != '1':  # Zakładając, że '1' oznacza aktywną sesję
    print("Sesja nie jest aktywna.")
else:
    response = client.service.DaneSzukajPodmioty({'Nip': '5261040828'})
    print(response)
    print("---------------------------------------")
    response1 = client.service.DanePobierzPelnyRaport("000331501", "BIR11OsPrawna")
    print(response1)