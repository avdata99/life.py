from life import Gene
from life.sequence.charts import histogram

g = Gene('ATCGCTATATATCGCGCGTTGAGAGATTA')
histogram.show_histogram_from_dataframe(g.as_dataframe())
