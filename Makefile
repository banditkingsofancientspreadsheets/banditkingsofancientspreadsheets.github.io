# Makefile to rerun the data transformation pipeline

.PHONY: clean

all: clean data

load_data:
	python banditkings/data/load.py

transform_data:
	python banditkings/data/transform.py

data: load_data transform_data

clean:
	rm -f data/02_intermediate/*.parquet
	rm -f data/03_primary/*.parquet
	rm -f data/04_feature/*.parquet