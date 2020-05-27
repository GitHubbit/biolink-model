---
parent: Mixins
title: biolink:EntityToDiseaseAssociation
grand_parent: Browse Biolink Model
layout: default
---

# Type: EntityToDiseaseAssociation


mixin class for any association whose object (target node) is a disease

URI: [biolink:EntityToDiseaseAssociation](https://w3id.org/biolink/vocab/EntityToDiseaseAssociation)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[VariantToDiseaseAssociation]uses%20-.-%3E[EntityToDiseaseAssociation],%20[GeneToDiseaseAssociation]uses%20-.-%3E[EntityToDiseaseAssociation],%20[GeneAsAModelOfDiseaseAssociation]uses%20-.-%3E[EntityToDiseaseAssociation],%20[EntityToFeatureOrDiseaseQualifiers]%5E-[EntityToDiseaseAssociation])

---


## Parents

 *  is_a: [EntityToFeatureOrDiseaseQualifiers](EntityToFeatureOrDiseaseQualifiers.md) - Qualifiers for entity to disease or phenotype associations

## Mixin for

 * [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) (mixin) 
 * [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) (mixin) 
 * [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) (mixin) 

## Referenced by class


## Attributes


### Domain for slot:

 * [entity to disease association➞object](entity_to_disease_association_object.md)  <sub>REQ</sub>
    * range: [Disease](Disease.md)
