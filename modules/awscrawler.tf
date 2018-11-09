
data "aws_s3_bucket" "csv_data_bucket" {
  bucket = "${var.csv_data_bucket}"
}

resource "aws_glue_catalog_database" "glue_db" {
    name = "${var.glue_database_name}" 
}

data "aws_iam_role" "glue_role" {
  name = "${var.crawler_iam_role}"
}

resource "aws_glue_crawler" "example" {
  database_name = "${aws_glue_catalog_database.glue_db.name}"
  name          = "${var.rescale_crawler}"
  role          = "${data.aws_iam_role.glue_role.arn}"
  table_prefix = "${var.table_prefix}"
  schedule = "cron(15 0 * * ? *)"
  s3_target {
    path = "s3://${data.aws_s3_bucket.csv_data_bucket.bucket}"
  }
}