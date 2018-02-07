define(function(require, exports, module) {
"use strict";

var oop = require("../lib/oop");
var TextHighlightRules = require("./text_highlight_rules").TextHighlightRules;

var tupyHighlightRules = function() {

    var keywordControls = (
        "parar|avancar|senao|para|passo|se|" +
        "retornar|enquanto|inclusive"
    );
    
    var storageType = (
        "logico|caracter|real|inteiro|cadeia|tipo|visual"
    );

    var storageModifiers = (
        "val|ref|oculto|oculta"
    );

    var keywordOperators = (
        "e|ou|nao|mod|div|xor"
    );

    var builtinConstants = (
        "nulo|verdadeiro|falso|pi|este|esta"
    );
    
    var builtinFunctions = (
        "escrever|ler|ler_linha|binario|octal|hexadecimal|aleatorio|inteiro_aleatorio|" +
        "log|ln|raiz|exp|abs|min|max|sinal|piso|teto|arredondar|juntar|copiar|"+
        "graus|radianos|sen|cos|tg|arcsen|arccos|arctg|arctg2|" +
        "senh|cosh|tgh|arsenh|arcosh|artgh|lista|inserir|remover|embaralhar|" +
        "grafo_MA|grafo_LA|digrafo_MA|digrafo_LA|arvore|matriz|vetor|pilha|fila|lista_encadeada|" +
        "grafo_valorado_MA|digrafo_valorado_MA|grafo_valorado_LA|digrafo_valorado_LA|heap|" +
        "comprimento|assercao|escrita"
    );

    var keywordMapper = this.$keywords = this.createKeywordMapper({
        "keyword.control" : keywordControls,
        "support.function" : builtinFunctions,
        "storage.type" : storageType,
        "storage.modifier" : storageModifiers,
        "keyword.operator" : keywordOperators,
        "variable.language": "this",
        "constant.language": builtinConstants
    }, "identifier");

    var identifierRe = "[a-zA-Z\\$_\u00a1-\uffff][a-zA-Z\\d\\$_\u00a1-\uffff]*\\b";
    var escapeRe = /\\(?:['"?\\abfnrtv]|[0-7]{1,3}|x[a-fA-F\d]{2}|u[a-fA-F\d]{4}U[a-fA-F\d]{8}|.)/.source;
    var formatRe = "%"
          + /(\d+\$)?/.source // field (argument #)
          + /[#0\- +']*/.source // flags
          + /[,;:_]?/.source // separator character (AltiVec)
          + /((-?\d+)|\*(-?\d+\$)?)?/.source // minimum field width
          + /(\.((-?\d+)|\*(-?\d+\$)?)?)?/.source // precision
          + /(hh|h|ll|l|j|t|z|q|L|vh|vl|v|hv|hl)?/.source // length modifier
          + /(\[[^"\]]+\]|[diouxXDOUeEfFgGaACcSspn%])/.source; // conversion type
          
    // regexp must not have capturing parentheses. Use (?:) instead.
    // regexps are ordered -> the first match is used

    this.$rules = { 
        "start" : [
            {
                token : "comment",
                regex : "#|~~",
                next : "singleLineComment"
            }, {
                token : "comment", //Trace offsetter
                regex : "\-{3,}"
            }, {
            ///////////////////////////////////// BEGIN BROKEN UNICODE RULES
                token : "keyword.control",
                regex : "senão|avançar|até|incl\\."
            }, {
                token : "keyword.operator",
                regex : "não"
            }, {
                token : "storage.type",
                regex : "lógico"
            }, {
                token : "support.function",
                regex : "binário|aleatório|inteiro_aleatório|mín|máx|árvore|asserção"
            }, {
                token : "constant.language",
                regex : "π"
            }, {
            ///////////////////////////////////// END BROKEN UNICODE RULES
                token : "string", // character
                regex : "'(?:" + escapeRe + "|.)?'"
            }, {
                token : "string.start",
                regex : '"', 
                stateName: "qqstring",
                next: [
                    { token: "string", regex: /\\\s*$/, next: "qqstring" },
                    { token: "constant.language.escape", regex: escapeRe },
                    { token: "constant.language.escape", regex: formatRe },
                    { token: "string.end", regex: '"|$', next: "start" },
                    { defaultToken: "string"}
                ]
            }, {
                token : "constant.numeric", // hex
                regex : "0[xX][0-9a-fA-F]+\\b"
            }, {
                token : "constant.numeric", // oct
                regex : "0[oO][0-7]+\\b"
            }, {
                token : "constant.numeric", // bin
                regex : "0[bB][01]+\\b"
            }, {
                token : "constant.numeric", // float
                regex : "[+-]?\\d+(?:(?:\\.\\d*)?)?\\b"
            }, {
                token : keywordMapper,
                regex : "[a-zA-Z_$][a-zA-Z0-9_$]*"
            }, {
                token : "keyword.operator",
                regex : /&&|\|\||[*\/+\-\^|~!<>=]=?/
            }, {
              token : "punctuation.operator",
              regex : "\\?|\\:|\\,|\\;|\\."
            }, {
                token : "paren.lparen",
                regex : "[[({]"
            }, {
                token : "paren.rparen",
                regex : "[\\])}]"
            }, {
                token : "text",
                regex : "\\s+"
            }
        ],
        "singleLineComment" : [
            {
                token : "comment",
                regex : /\\$/,
                next : "singleLineComment"
            }, {
                token : "comment",
                regex : /$/,
                next : "start"
            }, {
                defaultToken: "comment"
            }
        ],
    };

    this.normalizeRules();
};

oop.inherits(tupyHighlightRules, TextHighlightRules);

exports.tupyHighlightRules = tupyHighlightRules;
});
