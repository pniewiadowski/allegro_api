import zeep

allegro_api_key = open('api_key.txt').readline()
sandbox_web_api = 'https://webapi.allegro.pl.webapisandbox.pl/service.php?wsdl'
prod_web_api = 'https://webapi.allegro.pl/service.php?wsdl'

client = zeep.Client(wsdl=prod_web_api)
filterOptionsList = {'item':
                         {'filterId': 'category',
                          'filterValueId': ['20782'] #Nieruchomosci
                          },
                     'item':
                         {'filterId': 'state',
                          'filterValueId': '2'
                          }
                     }

print(client.service.doGetItemsList(allegro_api_key, 1, filterOptions=filterOptionsList))
