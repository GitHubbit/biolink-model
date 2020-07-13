---
parent: Classes
title: biolink:MaterialSampleToThingAssociation
grand_parent: Browse Biolink Model
layout: default
---

# Type: MaterialSampleToThingAssociation


An association between a material sample and something

URI: [biolink:MaterialSampleToThingAssociation](https://w3id.org/biolink/vocab/MaterialSampleToThingAssociation)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Provider]%3Cprovided%20by(i)%200..1-%20[MaterialSampleToThingAssociation%7Crelation(i):uriorcurie;id(i):identifier_type;negated(i):boolean%20%3F],%20[Publication]%3Cpublications(i)%200..*-%20[MaterialSampleToThingAssociation],%20[OntologyClass]%3Cqualifiers(i)%200..*-%20[MaterialSampleToThingAssociation],%20[OntologyClass]%3Cassociation%20type(i)%200..1-%20[MaterialSampleToThingAssociation],%20[NamedThing]%3Cobject(i)%201..1-%20[MaterialSampleToThingAssociation],%20[MaterialSample]%3Csubject%201..1-%20[MaterialSampleToThingAssociation],%20[MaterialSampleToDiseaseOrPhenotypicFeatureAssociation]uses%20-.-%3E[MaterialSampleToThingAssociation],%20[Association]%5E-[MaterialSampleToThingAssociation])

---


## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Mixin for

 * [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) (mixin)  - An association between a material sample and a disease or phenotype

## Referenced by class


## Attributes


### Own

 * [material sample to thing association➞subject](material_sample_to_thing_association_subject.md)  <sub>REQ</sub>
    * range: [MaterialSample](MaterialSample.md)

### Inherited from association:

 * [subject](subject.md)  <sub>REQ</sub>
    * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)
    * inherited from: [Association](Association.md)
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: the relationship type by which a subject is connected to an object in an association
    * range: [Uriorcurie](types/Uriorcurie.md)
    * inherited from: [Association](Association.md)
 * [object](object.md)  <sub>REQ</sub>
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)
    * inherited from: [Association](Association.md)
 * [association➞id](association_id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an association
    * range: [IdentifierType](types/IdentifierType.md)
    * inherited from: [Association](Association.md)
    * in subsets: (translator_minimal)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](types/Boolean.md)
    * inherited from: [Association](Association.md)
 * [association type](association_type.md)  <sub>OPT</sub>
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [OntologyClass](OntologyClass.md)
    * inherited from: [Association](Association.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)
    * inherited from: [Association](Association.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)
    * inherited from: [Association](Association.md)
 * [provided by](provided_by.md)  <sub>OPT</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Provider](Provider.md)
    * inherited from: [Association](Association.md)

### Domain for slot:

 * [material sample to thing association➞subject](material_sample_to_thing_association_subject.md)  <sub>REQ</sub>
    * range: [MaterialSample](MaterialSample.md)