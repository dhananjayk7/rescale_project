
data "aws_iam_role" "lamda_iam" {
  name = "${var.lambda_iam}"
}

resource "aws_lambda_function" "json_to_csv" {
    function_name = "${var.lambda_function_name}"
    filename="testrescale-072de1f0-3fbf-4bce-a86e-72b974853f87.zip"
    handler = "lambda_function.lambda_handler"
    role = "${data.aws_iam_role.lamda_iam.arn}"
    runtime = "python3.6"
    timeout = 300
}

resource "aws_cloudwatch_event_rule" "cloudwatch_event" {
    name = "lambda_execution_event"
    description = "Run according to the cron exepression"
    schedule_expression = "cron(10 0 * * ? *)"
}

resource "aws_cloudwatch_event_target" "cloudwatch_event_target" {
    rule = "${aws_cloudwatch_event_rule.cloudwatch_event.name}"
    target_id = "run_lambda"
    arn = "${aws_lambda_function.json_to_csv.arn}" 
}

resource "aws_lambda_permission" "cloudwatch_event" {
    statement_id = "Invoke_lambda"
    action = "lambda:InvokeFunction"
    function_name = "${aws_lambda_function.json_to_csv.function_name}"
    principal = "events.amazonaws.com"
    source_arn = "${aws_cloudwatch_event_rule.cloudwatch_event.arn}"
}