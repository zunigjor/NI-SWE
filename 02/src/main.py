from rdflib import Graph, Namespace, Literal, RDF, RDFS, XSD
from owlrl import DeductiveClosure, RDFS_Semantics

# Create a graph
g = Graph()

# Define namespaces
ex = Namespace("http://example.com/terms/")
data = Namespace("http://example.com/data/")

# Define Vocabulary
# Classes
g.add((ex.Person, RDF.type, RDFS.Class))        # Person
g.add((ex.Parent, RDF.type, RDFS.Class))        # Parent
g.add((ex.Child, RDF.type, RDFS.Class))         # Child
g.add((ex.Man, RDF.type, RDFS.Class))           # Man
g.add((ex.Father, RDF.type, RDFS.Class))        # Father
g.add((ex.Organisation, RDF.type, RDFS.Class))  # Organisation

# Class Hierarchy
g.add((ex.Parent, RDFS.subClassOf, ex.Person))  # Parent subclass of Person
g.add((ex.Child, RDFS.subClassOf, ex.Person))   # Child as subclass of Person
g.add((ex.Man, RDFS.subClassOf, ex.Person))     # Man as subclass of Person
g.add((ex.Father, RDFS.subClassOf, ex.Person))  # Father as subclass of Parent
g.add((ex.Father, RDFS.subClassOf, ex.Man))     # Father as subclass of Man

# Relationships
g.add((ex.worksFor, RDF.type, RDF.Property))        # worksFor - relationship between a person and an organisation
g.add((ex.worksFor, RDFS.domain, ex.Person))        # domain (subject) constraint
g.add((ex.worksFor, RDFS.range, ex.Organisation))   # range (object) constraint

g.add((ex.hasFather, RDF.type, RDF.Property))       # hasFather - relationship between a person and his/her father
g.add((ex.hasFather, RDFS.domain, ex.Person))
g.add((ex.hasFather, RDFS.range, ex.Father))

g.add((ex.officialName, RDF.type, RDF.Property))    # officialName - official name of company
g.add((ex.officialName, RDFS.domain, ex.Organisation))
g.add((ex.officialName, RDFS.range, XSD.string))

g.add((ex.age, RDF.type, RDF.Property))             # age - age of a Person
g.add((ex.age, RDFS.domain, ex.Person))
g.add((ex.age, RDFS.range, XSD.integer))

# Print the RDF graph
# provide an export (in the Turtle serialisation format) of the RDF graph containing only the vocabulary definitions
with open("../results/rdf_vocabulary.ttl", "wb") as f:
    g.serialize(format="turtle", destination=f)
########################################################################################################################
# Define data
# Carl is a Man
g.add((data.Carl, RDF.type, ex.Man))
# Anna hasFather Carl
g.add((data.Anna, ex.hasFather, data.Carl))
# Anna worksFor IBM
g.add((data.Anna, ex.worksFor, data.IBM))
# Anna is 25 years old
g.add((data.Anna, ex.age, Literal(25, datatype=XSD.integer)))
# the official name of IBM is International Business Machines Corporation
g.add((data.IBM, ex.officialName, Literal("International Business Machines Corporation", datatype=XSD.string)))

# Print the RDF graph
# provide an export (in the Turtle serialisation format) of the initial RDF graph
# (vocabulary and instance data) (before reasoning)
with open("../results/rdf_vocabulary_and_data.ttl", "wb") as f:
    g.serialize(format="turtle", destination=f)
########################################################################################################################
# Perform RDFS reasoning using owlrl
deductive_closure = DeductiveClosure(RDFS_Semantics)
deductive_closure.expand(g)
# Print the RDF graph
# provide an export (in the Turtle serialisation format) of the inferred RDF graph (after reasoning)
with open("../results/rdf_vocabulary_and_data_and_reasoning.ttl", "wb") as f:
    g.serialize(format="turtle", destination=f)
