

#query zoekt naar de hoeveelheid patienten met kanker

PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ns1: <https://health-lifesci.schema.org/>

select (COUNT (*) as ?count) WHERE {
	?patient rdfs:Type ns1:Patient .
    ?patient ns1:diagnosis ?ziekte.
    ?ziekte rdfs:label "cancer"
}


#query zoekt naar de hoeveelheid patienten met parkison


PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ns1: <https://health-lifesci.schema.org/>

select (COUNT (*) as ?count) WHERE {
	?patient rdfs:Type ns1:Patient .
    ?patient ns1:diagnosis ?ziekte.
    ?ziekte rdfs:label "parkison"
}


#query zoekt naar de hoeveelheid patienten zonder armen


PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ns1: <https://health-lifesci.schema.org/>

select (COUNT (*) as ?count) WHERE {
	?patient rdfs:Type ns1:Patient .
    ?patient ns1:MedicalCondition ?ledematen .
    ?ledematen rdfs:label "No arms"
}



#query zoekt naar de hoeveelheid patienten zonder benen


PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ns1: <https://health-lifesci.schema.org/>

select (COUNT (*) as ?count) WHERE {
	?patient rdfs:Type ns1:Patient .
    ?patient ns1:MedicalCondition ?ledematen .
    ?ledematen rdfs:label "No benen"
}


#query zoekt naar de hoeveelheid patienten met kanker en geen armen


PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ns1: <https://health-lifesci.schema.org/>

select (COUNT (*) as ?count) WHERE {
	?patient rdfs:Type ns1:Patient .
    ?patient ns1:diagnosis ?ziekte.
    ?ziekte rdfs:label "cancer" .
    ?patient ns1:MedicalCondition ?ledematen .
    ?ledematen rdfs:label "No arms"
}

#query zoekt naar de hoeveelheid patienten met parkison en geen benen

PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ns1: <https://health-lifesci.schema.org/>

select (COUNT (*) as ?count) WHERE {
	?patient rdfs:Type ns1:Patient .
    ?patient ns1:diagnosis ?ziekte.
    ?ziekte rdfs:label "parkison" .
    ?patient ns1:MedicalCondition ?ledematen .
    ?ledematen rdfs:label "No legs"
}


