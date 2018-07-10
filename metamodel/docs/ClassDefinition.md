# Class: class definition


A class or interface

URI: [http://bioentity.io/vocab/ClassDefinition](http://bioentity.io/vocab/ClassDefinition)

![img](images/ClassDefinition.png)
## Mappings

## Inheritance

 *  is_a: [Definition](Definition.md) - definition base class
## Children

## Used in

 *  class: **[ClassDefinition](ClassDefinition.md)** *[apply_to](apply_to.md)* **[ClassDefinition](ClassDefinition.md)**
 *  class: **[ClassDefinition](ClassDefinition.md)** *[class definition.is_a](class_definition_is_a.md)* **[ClassDefinition](ClassDefinition.md)**
 *  class: **[ClassDefinition](ClassDefinition.md)** *[class definition.mixins](class_definition_mixins.md)* **[ClassDefinition](ClassDefinition.md)**
 *  class: **[ClassDefinition](ClassDefinition.md)** *[class definition.union_of](class_definition_union_of.md)* **[ClassDefinition](ClassDefinition.md)**
 *  class: **[SchemaDefinition](SchemaDefinition.md)** *[classes](classes.md)* **[ClassDefinition](ClassDefinition.md)**
 *  class: **[SlotDefinition](SlotDefinition.md)** *[domain](domain.md)* **[ClassDefinition](ClassDefinition.md)**
## Fields

 * _[apply_to](apply_to.md)_
    * _Used to extend an existing class definition. For example, if we have a core schema where a gene has two slots for identifier and symbol, and we have a specialized schema for my_organism where we wish to add a slot systematic_name, we can avoid subclassing by defining a class gene_my_organism, adding the slot to this class, and then adding an apply_to pointing to the gene class. The new slot will be 'injected into' the gene class._
    * range: [ClassDefinition](ClassDefinition.md)
    * __Local__
 * _[class definition.is_a](class_definition_is_a.md)_
    * _specifies single-inheritance between classes and slots. While multiple inheritance is not allowed, mixins can be provided effectively providing the same thing. The semantics are the same when translated to formalisms that allow MI (e.g. RDFS/OWL). When translating to a SI framework (e.g. java classes, python classes) then is_a is used. When translating a framework without polymorphism (e.g. json-schema, solr document schema) then is_a and mixins are recursively unfolded_
    * range: [ClassDefinition](ClassDefinition.md)
    * __Local__
 * _[class definition.mixins](class_definition_mixins.md)_
    * _List of definitions to be mixed in. Targets may be any definition of the same type_
    * range: [ClassDefinition](ClassDefinition.md)*
    * __Local__
 * _[class definition.union_of](class_definition_union_of.md)_
    * _list of class or slot definitions that are combined to create the union class_
    * range: [ClassDefinition](ClassDefinition.md)*
    * __Local__
 * _[defining_slots](defining_slots.md)_
    * _The combination of is_a plus defining slots form a genus-differentia definition, or the set of necessary and sufficient conditions that can be transformed into an OWL equivalence axiom_
    * range: [SlotDefinition](SlotDefinition.md)*
    * __Local__
 * _[entity](entity.md)_
    * range: **boolean**
    * __Local__
 * _[slot_usage](slot_usage.md)_
    * _Additional info on how a slot is used in the context of a class. Many slots may be re-used across different classes, but the meaning of the slot may be refined by context. For example, a generic association model may use slots subject/predicate/object with generic semantics and minimal constraints. When this is subclasses, e.g. to disease-phenotype associations then slot_usage may specify both local naming (e.g. subject=disease) and local constraints_
    * range: [SlotDefinition](SlotDefinition.md)*
    * __Local__
 * _[slots](slots.md)_
    * _list of slot names that are applicable to a class. slots are by default inherited over is_a and mixins._
    * range: [SlotDefinition](SlotDefinition.md)*
    * __Local__
 * _[abstract](abstract.md)_
    * _An abstract class is a high level class or slot that is typically used to group common slots together and is generally not instantiated. When generating golr-views, abstract classes are ignored_
    * range: **boolean**
    * inherited from: [Definition](Definition.md)
 * _[aliases](aliases.md)_
    * range: **string***
    * inherited from: [Element](Element.md)
 * _[alt_descriptions](alt_descriptions.md)_
    * range: **string***
    * inherited from: [Element](Element.md)
 * _[comment](comment.md)_
    * _Comment about an element_
    * range: **string**
    * inherited from: [Element](Element.md)
 * _[description](description.md)_
    * _a description_
    * range: **string**
    * inherited from: [Element](Element.md)
 * _[examples](examples.md)_
    * _Example of usage for a slot or class_
    * range: [Example](Example.md)*
    * inherited from: [Element](Element.md)
 * _[flags](flags.md)_
    * _State information and other details_
    * range: **string***
    * inherited from: [Element](Element.md)
 * _[from_schema](from_schema.md)_
    * _id of the schema that the element was derived from.  Supplied by the loader._
    * range: **string**
    * inherited from: [Element](Element.md)
 * _[id_prefixes](id_prefixes.md)_
    * range: **string***
    * inherited from: [Element](Element.md)
 * _[in_subset](in_subset.md)_
    * _used to indicate membership of a term in a defined subset of biolink terms used for a particular domain or application (e.g. the translator_minimal subset holding the minimal set of predicates used in a translator knowledge graph)_
    * range: **string***
    * inherited from: [Element](Element.md)
 * _[local_names](local_names.md)_
    * _map from local identifier to slot_
    * range: **string***
    * inherited from: [Definition](Definition.md)
 * _[mappings](mappings.md)_
    * _list of equivalent or skos exact mappings to an ontology class_
    * range: **string***
    * inherited from: [Element](Element.md)
 * _[mixin](mixin.md)_
    * _Used only as a mixin -- cannot be instantiated on its own._
    * range: **boolean**
    * inherited from: [Definition](Definition.md)
 * _[name](name.md)_
    * _a unique key that identifies a slot, type or class in a schema_
    * range: **string**
    * inherited from: [Element](Element.md)
 * _[note](note.md)_
    * _Notes about an element_
    * range: **string**
    * inherited from: [Element](Element.md)
 * _[see_also](see_also.md)_
    * range: **string**
    * inherited from: [Element](Element.md)
 * _[singular_name](singular_name.md)_
    * _a name that is used in the singular form_
    * range: **string**
    * inherited from: [Element](Element.md)
 * _[subclass_of](subclass_of.md)_
    * _Ontolgy property which this is a subclass of. Not to be confused with is_a which links datamodel classes_
    * range: **uri**
    * inherited from: [Definition](Definition.md)
 * _[symmetric](symmetric.md)_
    * _Symmetric slot_
    * range: **boolean**
    * inherited from: [Definition](Definition.md)
 * _[values_from](values_from.md)_
    * _identifies the possible uri's of the range_
    * range: **string***
    * inherited from: [Definition](Definition.md)