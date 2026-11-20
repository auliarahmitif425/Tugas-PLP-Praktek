["and" "or" "not" "in" "contains"] @keyword
["=" "!=" ">" "<" ">=" "<="] @operator
(string) @string
(number) @number
(boolean) @constant
(comparison field: (identifier) @property)
(in_expression field: (identifier) @property)
(contains_expression field: (identifier) @property)
["(" ")" ","] @punctuation.bracket
