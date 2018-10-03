import pycurl
from io import BytesIO


query = ["PREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0D%0APREFIX+ns1%3A+%3Chttps%3A%2F%2Fhealth-lifesci.schema.org%2F%3E%0D%0A%0D%0Aselect+%28COUNT+%28%2A%29+as+%3Fcount%29+WHERE+%7B%0D%0A%09%3Fpatient+rdfs%3AType+ns1%3APatient+.%0D%0A++++%3Fpatient+ns1%3Adiagnosis+%3Fziekte.%0D%0A++++%3Fziekte+rdfs%3Alabel+%22cancer%22%0D%0A%7D%0D%0A"
         , "PREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0D%0APREFIX+ns1%3A+%3Chttps%3A%2F%2Fhealth-lifesci.schema.org%2F%3E%0D%0A%0D%0Aselect+%28COUNT+%28%2A%29+as+%3Fcount%29+WHERE+%7B%0D%0A%09%3Fpatient+rdfs%3AType+ns1%3APatient+.%0D%0A++++%3Fpatient+ns1%3Adiagnosis+%3Fziekte.%0D%0A++++%3Fziekte+rdfs%3Alabel+%22parkison%22%0D%0A%7D%0D%0A"
         ,"PREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0D%0APREFIX+ns1%3A+%3Chttps%3A%2F%2Fhealth-lifesci.schema.org%2F%3E%0D%0A%0D%0Aselect+%28COUNT+%28%2A%29+as+%3Fcount%29+WHERE+%7B%0D%0A%09%3Fpatient+rdfs%3AType+ns1%3APatient+.%0D%0A++++%3Fpatient+ns1%3AMedicalCondition+%3Fledematen+.%0D%0A++++%3Fledematen+rdfs%3Alabel+%22No+arms%22%0D%0A%7D"
         ,"PREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0D%0APREFIX+ns1%3A+%3Chttps%3A%2F%2Fhealth-lifesci.schema.org%2F%3E%0D%0A%0D%0Aselect+%28COUNT+%28%2A%29+as+%3Fcount%29+WHERE+%7B%0D%0A%09%3Fpatient+rdfs%3AType+ns1%3APatient+.%0D%0A++++%3Fpatient+ns1%3AMedicalCondition+%3Fledematen+.%0D%0A++++%3Fledematen+rdfs%3Alabel+%22No+benen%22%0D%0A%7D%0D%0A"
         ,"PREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0D%0APREFIX+ns1%3A+%3Chttps%3A%2F%2Fhealth-lifesci.schema.org%2F%3E%0D%0A%0D%0Aselect+%28COUNT+%28%2A%29+as+%3Fcount%29+WHERE+%7B%0D%0A%09%3Fpatient+rdfs%3AType+ns1%3APatient+.%0D%0A++++%3Fpatient+ns1%3Adiagnosis+%3Fziekte.%0D%0A++++%3Fziekte+rdfs%3Alabel+%22cancer%22+.%0D%0A++++%3Fpatient+ns1%3AMedicalCondition+%3Fledematen+.%0D%0A++++%3Fledematen+rdfs%3Alabel+%22No+arms%22%0D%0A%7D"
         , "PREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0D%0APREFIX+ns1%3A+%3Chttps%3A%2F%2Fhealth-lifesci.schema.org%2F%3E%0D%0A%0D%0Aselect+%28COUNT+%28%2A%29+as+%3Fcount%29+WHERE+%7B%0D%0A%09%3Fpatient+rdfs%3AType+ns1%3APatient+.%0D%0A++++%3Fpatient+ns1%3Adiagnosis+%3Fziekte.%0D%0A++++%3Fziekte+rdfs%3Alabel+%22parkison%22+.%0D%0A++++%3Fpatient+ns1%3AMedicalCondition+%3Fledematen+.%0D%0A++++%3Fledematen+rdfs%3Alabel+%22No+legs%22%0D%0A%7D%0D%0A"]
#query zoekt naar de hoeveelheid patienten met kanker
#query zoekt naar de hoeveelheid patienten met parkison
#query zoekt naar de hoeveelheid patienten zonder armen
#query zoekt naar de hoeveelheid patienten zonder benen
#query zoekt naar de hoeveelheid patienten met kanker en geen armen
#query zoekt naar de hoeveelheid patienten met parkison en geen benen

registry = [
    "http://localhost:7200/repositories/420"
]


for r in registry:
    for q in query:
        url = r + "?name=&infer=true&sameAs=false&" \
            "query="+q+"&execute="
        response_buffer = BytesIO()

        curl = pycurl.Curl()
        curl.setopt(curl.URL, url)
        curl.setopt(curl.USERPWD, '%s:%s' % (' ', ' '))
        curl.setopt(curl.WRITEDATA, response_buffer)

        curl.perform()
        curl.close()

        response_value = response_buffer.getvalue()
        print(response_value.decode("UTF-8"))



# PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# PREFIX ns1: <https://health-lifesci.schema.org/>
#
# select ?derp where {
# 	?derp rdfs:Type ns1:Patient
# } limit 100