module.exports = grammar({
  name: 'filter',
  extras: $ => [/\s/],
  word: $ => $.identifier,

  rules: {
    query: $ => $._expr,

    _expr: $ => choice(
      $.comparison, $.and_expression, $.or_expression,
      $.not_expression, $.parenthesized,
    ),
    
    comparison: $ => seq($.identifier, choice('=', '!=', '>', '<', '>=', '<='), $._value),
    
    and_expression: $ => prec.left(2, seq($._expr, 'and', $._expr)),

    or_expression: $ => prec.left(1, seq($._expr, 'or', $._expr)),

    parenthesized: $ => seq('(', $._expr, ')'),

    not_expression: $ => prec(3, seq('not', $._expr)),

    _value: $ => choice($.string, $.number, $.boolean),
    boolean: $ => choice('true', 'false'),

    identifier: $ => /[a-zA-Z_][a-zA-Z0-9_.]*/,
    string: $ => /"[^"]*"/,
    number: $ => /\d+(\.\d+)?/,
  }
});