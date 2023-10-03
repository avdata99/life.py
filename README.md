# life.py

Learning Genetics with Python

## Installation

```bash
pip install lifepy
```

## Usage

### Nucleotide

```python
from life import Nucleotide

nuc_a = Nucleotide('A')
nuc_t = Nucleotide('T')

nucs = nuc_a + nuc_t
type(nucs)
<class 'life.gene.Gene'>
print(nucs)
AT
```

### Gene


```python
from life import Gene
```