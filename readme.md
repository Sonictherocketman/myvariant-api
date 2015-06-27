MyVariant-Api
=============

A simple Python wrapper for the MyVariant API.

For extensive API documentation, see the [MyVariant](http://myvariant.info) site.

Install me from PyPi! `pip install myvariant-api`

*Basic Example*

Find a given SNP with the rsID: rs11931074.

```python
from myvariant.variant import Variant

results = Variant.find_by(q='rs11931074')
for r in result:
    print r._id, r.cadd['chrom']

>>> chr4:g.9069515G>T, 4
```

*Detailed Example*

Given an known variant, get it's begin and end coordinates. 

```python
from myvariant.variant import Variant

variant = Variant.get('chr4:g.90639515G>T')
print variant.dbsnp['hg19']['start'], variant.dbsnp['hg19']['end']

>>> chr4:g.90639515G>T, 90639515, 90639516
```
