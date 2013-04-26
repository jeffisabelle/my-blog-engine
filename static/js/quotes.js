var quotes = [
    "There are worse things than having people misunderstand your work. <br />A worse danger is that you will yourself misunderstand your work. <br /> -Paul Graham",
    "Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live. <br /> -Rick Osborne",
    "Perl – The only language that looks the same before and after RSA encryption. <br /> -Keith Bostic",
    "Talk is cheap. Show me the code. <br /> -Linus Torvalds",
    "In the future, computers may weigh no more than 1.5 tonnes.<br /> -Popular Mechanics, 1949",
    "The Internet? We are not interested in it.<br /> -Bill Gates, 1993",
    "UNIX is simple.  It just takes a genius to understand its simplicity.<br /> -Dennis Ritchie",
    "Some people, when confronted with a problem, think ‘I know, I’ll use regular expressions.’  Now they have two problems.<br /> -Jamie Zawinski",
    "I am not out to destroy Microsoft, that would be a completely unintended side effect.<br /> -Linus Torvalds",
    "Two years from now, spam will be solved.<br /> -Bill Gates, 2004",
    "Most good programmers do programming not because they expect to get paid or get adulation by the public, <br />but because it is fun to program.<br /> -Linus Torvalds",
    "The city’s central computer told you? R2D2, you know better than to trust a strange computer!<br /> -C3PO / Star Wars",
    "There are two major products that come out of Berkeley: LSD and UNIX. We don’t believe this to be a coincidence.<br /> -Jeremy S. Anderson",
    "Computer science education cannot make anybody an expert programmer any more than <br />studying brushes and pigment can make somebody an expert painter.<br /> -Eric Raymond",
    "There are only two kinds of programming languages: those people always bitch about and those nobody uses. <br /> -Bjarne Stroustrup",
    "Software is like sex: It’s better when it’s free. <br /> -Linus Torvalds",
    "The only people who have anything to fear from free software are those whose products are worth even less. <br /> -David Emery"
];

$(function() {
    var $rand = $('div#randomQuote > p');
    var random_quote = quotes[Math.floor(Math.random() * quotes.length)];
    $rand.html(random_quote);
    $rand.animate( {"opacity" : 0}, 0);
    $rand.animate( {"opacity" : 1}, 500);
    $rand.delay("10500");
    $rand.animate( { "opacity" : 0 }, 800 );
    // setTimeout("500");

});


function randomQuote () {
    var $rand = $('div#randomQuote > p');
    var random_quote = quotes[Math.floor(Math.random() * quotes.length)];
    $rand.html(random_quote);
    $rand.animate( {"opacity" : 1}, 500 );
    $rand.delay("10500");
    $rand.animate ( {"opacity" : 0}, 800 );
    setTimeout(arguments.callee, 13000);
}

$(function () {
    setTimeout(randomQuote, 13000);
});
