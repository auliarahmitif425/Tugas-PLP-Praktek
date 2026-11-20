(string) @string
(number) @number
(boolean) @constant.builtin
["=" "!=" ">" "<" ">=" "<="] @operator
(comparison field: (identifier) @property)
["and" "or" "not"] @keyword
["and" "or" "not" "in" "contains"] @keyword
(in_expression field: (identifier) @property)
(contains_expression field: (identifier) @property)
["(" ")" ","] @punctuation.bracket
