import pandas as pd
from life.files.base import GenFile
from life.sequence.charts import histogram

gf = GenFile('../dev/sample/fasta/mouse.fasta')
g = gf._up_class.genes[0]
code = g.code

groups = []
c = 0
for char in code:
    if c > 2:
        groups.append(f'{code[c-3]}{code[c-2]}{code[c-1]}{char}')
    c += 1

dataframe = pd.Series(groups)
histogram.show_histogram_from_dataframe(dataframe)
