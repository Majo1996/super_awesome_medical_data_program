import pycurl
from io import BytesIO

registry = [
    "http://localhost:7200/repositories/420"
]
query = ["PREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0D%0APREFIX+ns1%3A+%3Chttps%3A%2F%2Fhealth-lifesci.schema.org%2F%3E%0D%0A%0D%0A" \
"select+%3Fderp+where+%7B+%0D%0A%09%3Fderp+rdfs%3AType+ns1%3APatient+%0D%0A%7D+limit+100+%0A"]

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