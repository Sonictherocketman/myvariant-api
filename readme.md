MyVariant-Api
=============

A simple Python wrapper for the MyVariant API.

For extensive API documentation, see the [MyVariant](http://myvariant.info) site.

Install me from PyPi! `pip install myvariant-api`

*Basic Example*

Find a given SNP with the rsID: rs11931074.

```python
""" Use the query API to find a variant with 
the given rsID.
"""
from myvariant.variant import Variant

results = Variant.find_by(q='rs11931074')
for r in result:
    print r._id, r.cadd['chrom']

>>> chr4:g.9069515G>T, 4
```

*Detailed Example*

Given an known variant, get it's begin and end coordinates. 

```python
""" Use the annotation API to find the full 
details of a given variant.
"""
from myvariant.variant import Variant

variant = Variant.get('chr4:g.90639515G>T')
print variant._id, variant.dbsnp['hg19']['start'], variant.dbsnp['hg19']['end']

>>> chr4:g.90639515G>T, 90639515, 90639516
```

This library also supports the metadata API.

```python
from myvariant.metadata import Metadata

metadata = Metadata.get_metadata()
print metadata.stats['cadd']

>>> 163690986
```



