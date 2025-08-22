-- Export (Copy) Data from BigQuery to GCS
bq extract --destination_format=CSV --compression=GZIP project_id.dataset_id.table_id gs://your-bucket-name/your-file-name.csv.gz;
--Import (Copy) Data from GCS to BigQuery
bq load --source_format=CSV --autodetect project_id.dataset_id.table_id gs://your-bucket-name/your-file-name.csv.gz;

-- Datasets in a project:
bq ls your_dataset;
-- Show Table or Dataset Schema & Info
--Show table schema:
bq show --schema --format=prettyjson your_dataset.your_table
--Show full table metadata:
bq show your_dataset.your_table
--Create a dataset:
bq mk your_dataset;
--Create a table
bq mk --table your_dataset.your_table schema.json;
--Delete a table:
bq rm -t your_dataset.your_table;
--Delete a dataset (recursively):
bq rm -r -d your_dataset
--🧾 8. Update Schema or Table Description
bq update --description "This is my table" your_dataset.your_table
--Update schema (e.g., add columns):
bq update --schema new_schema.json your_dataset.your_table


