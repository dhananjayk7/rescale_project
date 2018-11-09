variable "profile" {
  default = "default"
}

variable "region" {
  default = "us-east-1"
}

variable "rescale_crawler" {
    default = "rescale_crawler"
    description = "Name of the crawler"
}

variable "table_prefix" {
    default = "data-pricing"
}

variable "glue_database_name" {
  default = "rescale_tf_db"
}

variable "crawler_iam_role" {
  default = "AWSGlueServiceRole-gluerole"
}

variable "csv_data_bucket" {
  default = "rescale"
}
