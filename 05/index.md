# HW5 - Knowledge Graphs Integration

## Task 1: Ontology/Vocabulary Integration
### Task 1.1: Define a Domain-specific Ontology/Vocabulary
#### Domain-specific Ontology: Healthcare
##### 1. Classes (Concepts):
```
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix snomed: <http://snomed.info/sct#> .

# Healthcare Ontology
### Classes
:Patient rdf:type owl:Class .
:HealthcareProvider rdf:type owl:Class .
:MedicalCondition rdf:type owl:Class .
:Treatment rdf:type owl:Class .
:Appointment rdf:type owl:Class .
:Medication rdf:type owl:Class .

### Properties
:hasName rdf:type owl:DatatypeProperty .
:hasAge rdf:type owl:DatatypeProperty .
:hasGender rdf:type owl:DatatypeProperty .
:hasAddress rdf:type owl:DatatypeProperty .
:hasContactInformation rdf:type owl:DatatypeProperty .
:hasSpecialty rdf:type owl:DatatypeProperty .
:hasDescription rdf:type owl:DatatypeProperty .
:hasSymptoms rdf:type owl:DatatypeProperty .
:hasDosage rdf:type owl:DatatypeProperty .
:hasDuration rdf:type owl:DatatypeProperty .
:hasDate rdf:type owl:DatatypeProperty .
:hasTime rdf:type owl:DatatypeProperty .
:hasLocation rdf:type owl:DatatypeProperty .

### Relationships
:Diagnosis rdf:type owl:ObjectProperty .
:Prescription rdf:type owl:ObjectProperty .
:PatientHistory rdf:type owl:ObjectProperty .
:ScheduledAppointment rdf:type owl:ObjectProperty .
```

### Task 1.2: Identify Other Related Existing Ontologies
#### **Existing Ontologies:**
* **SNOMED CT (Systematized Nomenclature of Medicine - Clinical Terms):**
    * Contains a comprehensive set of medical concepts and relationships.
* **FOAF (Friend of a Friend):**
    * Contains a basic representation of individuals and relationships, useful for representing patients and healthcare providers. 

### Task 1.3: Create Ontology Alignment Mappings
#### Ontology Alignment Mappings:
```
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

### Mappings
# Patient in Healthcare Ontology to Individual in FOAF
:Patient owl:equivalentClass foaf:Person .

# HealthcareProvider in Healthcare Ontology to Agent in FOAF
:HealthcareProvider owl:equivalentClass foaf:Agent .

# MedicalCondition in Healthcare Ontology to Disease in SNOMED CT
:MedicalCondition owl:equivalentClass snomed:Disease .

# Treatment in Healthcare Ontology to Procedure in SNOMED CT
:Treatment owl:equivalentClass snomed:Procedure .

# Diagnosis in Healthcare Ontology to Finding in SNOMED CT
:Diagnosis owl:equivalentClass snomed:Finding .

# Prescription in Healthcare Ontology to MedicinalProduct in SNOMED CT
:Prescription owl:equivalentClass snomed:MedicinalProduct .

# PatientHistory in Healthcare Ontology to ClinicalHistory in SNOMED CT
:PatientHistory owl:equivalentClass snomed:ClinicalHistory .

# ScheduledAppointment in Healthcare Ontology to Appointment in FOAF
:ScheduledAppointment owl:equivalentClass foaf:Appointment .
```

## Task 2: Data Integration
// todo