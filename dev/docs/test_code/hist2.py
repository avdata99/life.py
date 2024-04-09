from life.files.base import GenFile
from life.sequence.charts import histogram

gf = GenFile('dev/sample/fasta/mouse.fasta')
g = gf._up_class.genes[0]
histogram.show_histogram_from_dataframe(g.as_dataframe())
