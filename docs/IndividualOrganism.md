---
parent: Entities
title: biolink:IndividualOrganism
grand_parent: Classes
layout: default
---

# Class: IndividualOrganism




URI: [biolink:IndividualOrganism](https://w3id.org/biolink/vocab/IndividualOrganism)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ThingWithTaxon],[OrganismalEntity],[OrganismTaxon],[IndividualOrganism%7Cid(i):string;category(i):category_type%20%2B;iri(i):iri_type%20%3F;name(i):label_type%20%3F;source(i):label_type%20%3F]uses%20-.-%3E[ThingWithTaxon],[IndividualOrganism]%5E-[Case],[OrganismalEntity]%5E-[IndividualOrganism],[Case],[Attribute])

---


## Parents

 *  is_a: [OrganismalEntity](OrganismalEntity.md) - A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding molecular entities

## Uses Mixins

 *  mixin: [ThingWithTaxon](ThingWithTaxon.md) - A mixin that can be used on any entity with a taxon

## Children

 * [Case](Case.md) - An individual (human) organism that has a patient role in some clinical context.

## Referenced by class


## Attributes


### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `bl:Protein`, `bl:GeneProduct`, `bl:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {bl:GenomicEntity, bl:MolecularEntity, bl:NamedThing}
    * range: [CategoryType](types/CategoryType.md)
    * in subsets: (translator_minimal)

### Inherited from organismal entity:

 * [organismal entity➞has attribute](organismal_entity_has_attribute.md)  <sub>0..*</sub>
    * Description: may be an organism attribute
    * range: [Attribute](Attribute.md)

### Inherited from resource mixin:

 * [iri](iri.md)  <sub>OPT</sub>
    * Description: An IRI for the node. This is determined by the id using expansion rules.
    * range: [IriType](types/IriType.md)
    * in subsets: (translator_minimal,samples)
 * [name](name.md)  <sub>OPT</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal,samples)
 * [source](source.md)  <sub>OPT</sub>
    * Description: a lightweight analog to the association class 'has provider' slot, which is the string name, or the authoritative (i.e. database) namespace, designating the origin of the entity to which the slot belongs.
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects a thing to a class representing a taxon
    * range: [OrganismTaxon](OrganismTaxon.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | SIO:010000 |
|  | | UMLSSC:T001 |
|  | | UMLSST:orgm |
| **Narrow Mappings:** | | WIKIDATA:Q795052 |
|  | | foaf:Person |

